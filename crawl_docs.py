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
MKDOCS_FILE = Path(__file__).parent / "mkdocs.yml"

# 并发控制
MAX_CONCURRENT = 3
DELAY_BETWEEN = 2.0  # 秒

# 目录名中文映射
DIR_NAME_MAP = {
    "overview": "基本介绍",
    "quick-start": "快速开始",
    "feature-set": "功能集",
    "api-reference": "API 参考",
    "debug": "调试",
    "dock-to-cloud": "机场上云",
    "pilot-to-cloud": "Pilot 上云",
    "dock-feature-set": "机场功能集",
    "pilot-feature-set": "Pilot 功能集",
    "basic-concept": "基础概念",
    "mqtt": "MQTT",
    "https": "HTTPS",
    "websocket": "WebSocket",
    "jsbridge": "JSBridge",
    "dji-wpml": "DJI WPML",
    "aircraft": "飞行器",
    "dock": "机场",
    "dock1": "大疆机场 1",
    "dock2": "大疆机场 2",
    "dock3": "大疆机场 3",
    "rc-pro": "RC Pro",
    "dji-rc-plus-2": "DJI RC Plus 2",
    "m3-series": "M3 系列",
    "m4-series": "M4 系列",
    "matrice-400": "Matrice 400",
    "others": "其他",
    "map-elements": "地图元素",
    "media-management": "媒体管理",
    "situation-awareness": "态势感知",
    "waypoint-management": "航线管理",
    "topic-definition": "Topic 定义",
    "rc": "遥控器",
}

FILE_NAME_MAP = {
    "index": "版本发布记录",
    "tutorial-map": "文档阅读指引",
    "flight-safety-notification": "安全飞行须知",
    "error-code": "错误码",
    "faq": "常见问题",
    "product-introduction": "产品介绍",
    "product-architecture": "产品架构",
    "product-support": "产品支持",
    "proper-noun": "专有名词",
    "thing-model": "物模型",
    "environment-prepare-list": "环境准备清单",
    "source-code-deployment-steps": "源码部署步骤",
    "docker-deployment-steps": "Docker 部署步骤",
    "function-display-video": "功能演示视频",
    "pilot-access-to-cloud": "Pilot 接入云端",
    "pilot-situation-awareness": "Pilot 态势感知",
    "pilot-livestream": "Pilot 直播",
    "pilot-map-elements": "Pilot 地图元素",
    "pilot-media-management": "Pilot 媒体管理",
    "pilot-wayline-management": "Pilot 航线管理",
    "pilot-third-party-app": "Pilot 第三方应用",
    "pull-pilot-log": "拉取 Pilot 日志",
    "dock-access-to-cloud": "机场接入云端",
    "dock-livestream": "机场直播",
    "dock-device-management": "机场设备管理",
    "dock-media-management": "机场媒体管理",
    "dock-wayline-management": "机场航线管理",
    "custom-flight-area": "自定义飞行区",
    "ai-target-recognition": "AI 目标识别",
    "firmware-upgrade": "固件升级",
    "multi-dock": "多机场",
    "remote-debug": "远程调试",
    "remote-log": "远程日志",
    "drc": "指令飞行",
    "hms": "HMS",
    "properties": "设备属性",
    "device": "设备管理",
    "live": "直播",
    "wayline": "航线管理",
    "file": "文件管理",
    "log": "日志",
    "config": "配置更新",
    "cmd": "远程调试",
    "flysafe": "飞行安全",
    "airsense": "AirSense",
    "organization": "组织管理",
    "firmware": "固件升级",
    "media": "媒体管理",
    "psdk": "PSDK",
    "psdk-transmit-custom-data": "PSDK 自定义数据传输",
    "esdk-transmit-custom-data": "ESDK 自定义数据传输",
    "remote-control": "远程控制",
    "custom-fly-region": "自定义飞行区",
    "create": "创建",
    "delete": "删除",
    "obtain": "获取",
    "update": "更新",
    "fast-upload": "快速上传",
    "group-upload-callback": "分组上传回调",
    "mediafile-upload-result-report": "媒体文件上传结果上报",
    "obtain-exited-tiny-fingerprint": "获取已退出缩略图指纹",
    "obtain-temporary-credential": "获取临时凭证",
    "obtain-device-topology-list": "获取设备拓扑列表",
    "cancel-collect": "取消采集",
    "collect-waypointfile-in-batch": "批量采集航线文件",
    "get-duplicated-waypointfile-name": "获取重复航线文件名",
    "get-waypointfile-download-location": "获取航线文件下载地址",
    "obtain-waypointfile-list": "获取航线文件列表",
    "waypointfile-upload-result-report": "航线文件上传结果上报",
    "message-push": "消息推送",
    "dji-pilot2-webview-debug": "DJI Pilot2 WebView 调试",
    "log-export": "日志导出",
    "mqttx": "MQTTX 调试",
    "overview": "概述",
    "template-kml": "模板 KML",
    "common-element": "通用元素",
    "waylines-wpml": "航线 WPML",
    "m30-properties": "M30 属性",
    "m3d-properties": "M3D 属性",
    "m4d-properties": "M4D 属性",
}


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


async def extract_page_links(crawler: AsyncWebCrawler) -> tuple[list[str], dict[str, str]]:
    """从首页提取所有文档页面链接和中文标题"""
    config = CrawlerRunConfig(
        wait_until="networkidle",
        page_timeout=60000,
    )

    print("📋 提取文档导航链接...")
    result = await crawler.arun(url=BASE_URL, config=config)

    if not result.success or not result.links:
        print("❌ 无法提取链接")
        return [], {}

    links = []
    title_map = {}
    seen = set()
    internal = result.links.get("internal", [])

    for link in internal:
        href = link.get("href", "")
        text = link.get("text", "").strip()
        if not href:
            continue

        if "/doc/cloud-api-tutorial/cn/" not in href:
            continue

        href = href.split("#")[0]
        if not href.endswith(".html"):
            continue

        text = text.replace("open in new window", "").strip()

        if href not in seen:
            seen.add(href)
            links.append(href)
            if text:
                title_map[href] = text
        else:
            if text and len(text) < len(title_map.get(href, text)):
                title_map[href] = text

    print(f"   找到 {len(links)} 个独立文档页面，提取到 {len(title_map)} 个中文标题")
    return sorted(links), title_map


def extract_fallback_title(md_path: Path) -> str | None:
    """从 Markdown 文件中提取第一个中文标题作为兜底"""
    text = md_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("#"):
            continue
        m = re.match(r"^#+\s+(.+)", line)
        if not m:
            continue
        title = m.group(1).strip()
        if any("\u4e00" <= ch <= "\u9fff" for ch in title):
            return title
    return None


def build_nav_tree(docs_dir: Path, title_map: dict[str, str]) -> list[dict]:
    """根据目录结构和标题映射生成 MkDocs nav 树"""

    def rel_url(md_path: Path) -> str:
        return str(md_path.relative_to(docs_dir).with_suffix(""))

    def url_for(rel: str) -> str:
        return BASE_URL + rel + ".html"

    def label_for_dir(name: str) -> str:
        return DIR_NAME_MAP.get(name, name.replace("-", " ").replace("_", " ").title())

    def label_for_file(md_path: Path) -> str:
        rel = rel_url(md_path)
        url = url_for(rel)
        if url in title_map:
            return title_map[url]

        stem = md_path.stem
        if stem in FILE_NAME_MAP:
            return FILE_NAME_MAP[stem]

        fallback = extract_fallback_title(md_path)
        if fallback:
            return fallback

        return stem.replace("-", " ").replace("_", " ").title()

    def walk(path: Path) -> list[dict]:
        items = []
        entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name))
        for entry in entries:
            if entry.name.startswith("_") or entry.name == "index.md":
                continue
            if entry.is_dir():
                children = walk(entry)
                if children:
                    items.append({label_for_dir(entry.name): children})
            elif entry.suffix == ".md":
                items.append({label_for_file(entry): rel_url(entry) + ".md"})
        return items

    root_items = []
    index_file = docs_dir / "index.md"
    if index_file.exists():
        root_items.append({label_for_file(index_file): "index.md"})

    root_items.extend(walk(docs_dir))
    return root_items


def update_mkdocs_nav(nav: list[dict]) -> None:
    """更新 mkdocs.yml 的 nav 段"""
    import yaml

    text = MKDOCS_FILE.read_text(encoding="utf-8")
    config = yaml.load(text, Loader=yaml.Loader) or {}
    config["nav"] = nav
    MKDOCS_FILE.write_text(
        yaml.dump(config, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )
    print(f"💾 导航已更新: {MKDOCS_FILE}")


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
        all_links, title_map = await extract_page_links(crawler)

        if not all_links:
            print("没有找到任何文档链接，退出")
            return

        index_file = OUTPUT_DIR / "_index.json"
        index_file.write_text(json.dumps(all_links, ensure_ascii=False, indent=2))
        print(f"💾 链接索引已保存: {index_file}")

        title_file = OUTPUT_DIR / "_titles.json"
        title_file.write_text(json.dumps(title_map, ensure_ascii=False, indent=2))
        print(f"💾 标题映射已保存: {title_file}")

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

        nav = build_nav_tree(OUTPUT_DIR, title_map)
        update_mkdocs_nav(nav)

        print(f"\n{'='*50}")
        print(f"📊 完成！成功: {success_count}, 失败/空: {fail_count}, 总计: {len(all_links)}")
        print(f"📁 输出目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
