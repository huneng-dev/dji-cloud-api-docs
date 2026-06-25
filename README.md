# DJI 上云 API 文档镜像

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=flat&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

这是一个 **DJI 上云 API（Cloud API）官方文档的社区镜像站点**，将官方基于 VuePress 的 SPA 文档站转换为**静态 HTML**，方便：

- **开发者离线查阅** — 不受官网访问速度影响
- **AI 读取与分析** — 内容是真正的静态 HTML / Markdown，AI 可以直接抓取
- **全文搜索** — 基于 MkDocs Material 内置搜索，支持中英文

> 📌 官方文档地址：https://developer.dji.com/doc/cloud-api-tutorial/cn/  
> 📌 本镜像内容版权归 DJI 大疆创新所有，如有侵权请联系删除。

---

## 在线访问

站点通过 **GitHub Pages** 部署：

```
https://huneng-dev.github.io/dji-cloud-api-docs/
```

> 部署完成后，将上述 URL 中的 `huneng-dev` 替换为你的真实用户名即可访问。

---

## 项目结构

```
.
├── output/                 # 文档源文件（Markdown）
│   ├── index.md            # 版本发布记录（首页）
│   ├── overview/           # 基本介绍
│   ├── quick-start/        # 快速开始
│   ├── feature-set/        # 功能集
│   ├── api-reference/      # API 参考（核心）
│   └── debug/              # 调试指南
├── crawl_docs.py           # 从官网爬取最新文档的脚本
├── test_crawl.py           # 爬取测试脚本
├── mkdocs.yml              # MkDocs 站点配置
├── README.md               # 本文件
└── .venv/                  # Python 虚拟环境（不提交到 Git）
```

---

## 本地使用

### 1. 克隆仓库

```bash
git clone https://github.com/huneng-dev/dji-cloud-api-docs.git
cd dji-cloud-api-docs
```

### 2. 激活虚拟环境

```bash
source .venv/bin/activate
```

### 3. 本地预览

```bash
mkdocs serve
```

然后打开 http://127.0.0.1:8000 即可预览。

### 4. 构建静态站点

```bash
mkdocs build
```

构建结果在 `site/` 目录下。

---

## 如何更新文档

当 DJI 官方文档更新后，可以重新运行爬取脚本获取最新内容：

```bash
# 激活虚拟环境
source .venv/bin/activate

# 重新爬取（约 5-10 分钟，154 个页面）
python crawl_docs.py

# 本地预览确认
mkdocs serve

# 确认无误后部署到 GitHub Pages
mkdocs gh-deploy
```

爬取脚本会：

1. 用 Playwright 渲染官方 VuePress SPA
2. 从首页侧边栏提取全部 154 个文档链接
3. 逐页抓取并转换为 Markdown
4. 保持与官方一致的目录结构保存到 `output/`

> ⚠️ 请合理控制爬取频率，避免对 DJI 服务器造成压力。

---

## 给 AI 使用

本镜像包含两种 AI 友好的内容形式：

### 方式一：直接读取 Markdown 源文件

每个 `.md` 文件都包含完整的文档内容，路径清晰：

```
output/api-reference/dock-to-cloud/mqtt/dock/dock3/wayline.md
output/api-reference/pilot-to-cloud/mqtt/topic-definition.md
output/feature-set/dock-feature-set/dock-livestream.md
```

你可以将 `output/` 目录作为知识库导入到 Cursor、Cherry Studio、Dify、AnythingLLM 等工具。

### 方式二：抓取静态 HTML 页面

部署后的 GitHub Pages 每个页面都是完整的静态 HTML，内容在 HTML 源码中，不像官方 VuePress 那样返回空壳。AI 可以直接用 curl 或爬虫抓取：

```bash
curl -s https://huneng-dev.github.io/dji-cloud-api-docs/api-reference/dock-to-cloud/mqtt/dock/dock3/wayline/
```

---

## 部署到 GitHub Pages

### 首次部署

确保你已经在 GitHub 上创建了同名仓库 `dji-cloud-api-docs`，然后：

```bash
# 初始化并提交
mkdocs gh-deploy --remote-name origin --remote-branch gh-pages
```

这条命令会：

1. 自动构建站点
2. 将 `site/` 内容推送到仓库的 `gh-pages` 分支
3. 在 GitHub 上开启 Pages 后即可通过 `https://<用户名>.github.io/dji-cloud-api-docs/` 访问

### 后续更新

```bash
mkdocs gh-deploy
```

---

## 技术栈

- [crawl4ai](https://github.com/unclecode/crawl4ai) — 渲染 VuePress SPA 并提取 Markdown
- [MkDocs](https://www.mkdocs.org/) — 静态站点生成器
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — 主题与搜索

---

## 免责声明

- 本站所有文档内容来自 DJI 官方，仅做格式转换与镜像，**不修改任何技术内容**。
- 内容版权归 DJI 大疆创新所有。
- 本站与 DJI 官方无关，如官方要求下架，将立即配合删除。
- 使用本站内容产生的任何问题，由使用者自行承担。

---

## License

本站点的构建脚本和配置文件采用 MIT 许可证。  
文档内容版权归 DJI 大疆创新所有，不在本仓库的 MIT 许可范围内。
