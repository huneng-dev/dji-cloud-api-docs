"""
DJI 上云API 文档离线爬取脚本
使用 crawl4AI + Playwright 渲染 VuePress SPA，逐页提取 Markdown
"""
import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, urljoin

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

BASE_URL = "https://developer.dji.com/doc/cloud-api-tutorial/cn/"
OUTPUT_DIR = Path(__file__).parent / "output"

# 并发控制
MAX_CONCURRENT = 3
DELAY_BETWEEN = 2.0  # 秒


def url_to_path(url: str) -> Path:
    """将文档 URL 转换为本地文件路径"""
    parsed = urlparse(url)
    path = parsed.path

    # 去掉 /doc/cloud-api-tutorial/cn/ 前缀
    prefix = "/doc/cloud-api-tutorial/cn/"
    if path.startswith(prefix):
        path = path[len(prefix):]

    if not path or path == "/":
        path = "index"
    if path.endswith("/"):
        path = path[:-1]
    if not path.endswith(".html"):
        # 如果是目录，加 index
        path = path + "/index" if "/" not in path.rsplit("/", 1)[-1] else path

    # 确保 .md 后缀
    if path.endswith(".html"):
        path = path[:-5] + ".md"

    return OUTPUT_DIR / path


def clean_markdown(md: str, url: str) -> str:
    """清理提取的 Markdown 内容"""
    lines = md.split("\n")
    cleaned = []

    # 获取页面相对路径作为标题
    rel_path = urlparse(url).path.replace("/doc/cloud-api-tutorial/cn/", "").strip("/")
    if rel_path.endswith(".html"):
        rel_path = rel_path[:-5]

    # 用 HTML 注释保留元数据，避免渲染到页面
    cleaned.append(f"<!-- source: {url} -->")
    cleaned.append(f"<!-- path: {rel_path} -->")
    cleaned.append("")

    skip_nav = False
    for line in lines:
        # 跳过导航/侧边栏重复内容（首页已经包含了完整的导航）
        stripped = line.strip()

        # 跳过空的导航链接行和冗余的搜索框
        if stripped in ("搜索`K`", "[ v1.15 ](https://developer.dji.com/doc/cloud-api-tutorial/cn/)",
                         "LanguagesLanguages", "[ English ]", "[ 中文 ]"):
            continue

        # 跳过首页顶部 logo 和导航（重复出现）
        if stripped.startswith("[![上云API]") or stripped.startswith("[上云API]("):
            continue

        # 确保主要内容
        if stripped:
            cleaned.append(line)

    # 移除开头的空行
    while cleaned and cleaned[0] == "":
        cleaned.pop(0)

    return "\n".join(cleaned)


async def extract_page_links(crawler: AsyncWebCrawler) -> list[str]:
    """从首页提取所有文档页面链接"""
    config = CrawlerRunConfig(
        wait_until="networkidle",
        page_timeout=60000,
    )

    print("📋 提取文档导航链接...")
    result = await crawler.arun(url=BASE_URL, config=config)

    if not result.success or not result.links:
        print("❌ 无法提取链接")
        return []

    links = []
    seen = set()
    internal = result.links.get("internal", [])

    for link in internal:
        href = link.get("href", "")
        if not href:
            continue

        # 只保留文档页面链接
        if "/doc/cloud-api-tutorial/cn/" not in href:
            continue

        # 去除尾部 hash 和末尾斜杠不一致
        href = href.split("#")[0]
        if not href.endswith(".html"):
            continue

        if href not in seen:
            seen.add(href)
            links.append(href)

    print(f"   找到 {len(links)} 个独立文档页面")
    return sorted(links)


async def crawl_page(crawler: AsyncWebCrawler, url: str, sem: asyncio.Semaphore) -> tuple[str, str | None]:
    """爬取单个页面，返回 (url, markdown)"""
    async with sem:
        config = CrawlerRunConfig(
            wait_until="networkidle",
            page_timeout=30000,
            css_selector=".theme-default-content",  # VuePress 内容区域
        )

        try:
            result = await crawler.arun(url=url, config=config)
            if result.success and result.markdown:
                md = clean_markdown(result.markdown, url)
                rel = urlparse(url).path.replace("/doc/cloud-api-tutorial/cn/", "")
                print(f"   ✅ {rel}")
                await asyncio.sleep(DELAY_BETWEEN)
                return url, md
            else:
                rel = urlparse(url).path.replace("/doc/cloud-api-tutorial/cn/", "")
                print(f"   ⚠️  {rel} - 空内容")
                await asyncio.sleep(DELAY_BETWEEN)
                return url, None
        except Exception as e:
            rel = urlparse(url).path.replace("/doc/cloud-api-tutorial/cn/", "")
            print(f"   ❌ {rel} - {e}")
            await asyncio.sleep(DELAY_BETWEEN)
            return url, None


async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sem = asyncio.Semaphore(MAX_CONCURRENT)

    async with AsyncWebCrawler() as crawler:
        # 第一步：提取所有链接
        all_links = await extract_page_links(crawler)

        if not all_links:
            print("没有找到任何文档链接，退出")
            return

        # 保存链接索引
        index_file = OUTPUT_DIR / "_index.json"
        index_file.write_text(json.dumps(all_links, ensure_ascii=False, indent=2))
        print(f"💾 链接索引已保存: {index_file}")

        # 第二步：逐页爬取
        print(f"\n🚀 开始爬取 {len(all_links)} 个页面 (并发={MAX_CONCURRENT})...\n")

        tasks = [crawl_page(crawler, url, sem) for url in all_links]
        results = await asyncio.gather(*tasks)

        # 第三步：写入文件
        success_count = 0
        fail_count = 0

        for url, md in results:
            if md:
                filepath = url_to_path(url)
                filepath.parent.mkdir(parents=True, exist_ok=True)
                filepath.write_text(md, encoding="utf-8")
                success_count += 1
            else:
                fail_count += 1

        print(f"\n{'='*50}")
        print(f"📊 完成！成功: {success_count}, 失败/空: {fail_count}, 总计: {len(all_links)}")
        print(f"📁 输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
