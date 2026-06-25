"""快速测试：crawl4AI 能否渲染 DJI VuePress SPA 并提取内容"""
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def test():
    config = CrawlerRunConfig(
        wait_until="networkidle",
        page_timeout=60000,
        verbose=True,
    )

    async with AsyncWebCrawler() as crawler:
        print("🔍 正在抓取 DJI 上云API 首页...")
        result = await crawler.arun(
            url="https://developer.dji.com/doc/cloud-api-tutorial/cn/",
            config=config,
        )

        if result.success:
            md = result.markdown or ""
            print(f"✅ 成功！内容长度: {len(result.html)} 字符")
            print(f"   Markdown 长度: {len(md)} 字符")
            print(f"\n--- 前 1000 字符 Markdown ---\n{md[:1000]}")
            print(f"\n--- 页面内链接数量 ---")
            if result.links:
                internal = result.links.get("internal", [])
                external = result.links.get("external", [])
                print(f"   内部链接: {len(internal)}")
                print(f"   外部链接: {len(external)}")
                # 只打印文档相关的前20个链接
                doc_links = [l["href"] for l in internal if "/doc/cloud-api-tutorial/cn/" in l.get("href", "")]
                print(f"   文档链接: {len(doc_links)}")
                for link in doc_links[:20]:
                    print(f"     - {link}")
        else:
            print(f"❌ 失败: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(test())
