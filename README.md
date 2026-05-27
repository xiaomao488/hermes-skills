# Hermes Skills - 网页文档学习技能集

[![GitHub stars](https://img.shields.io/github/stars/xiaomao488/hermes-skills?style=social)](https://github.com/xiaomao488/hermes-skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xiaomao488/hermes-skills?style=social)](https://github.com/xiaomao488/hermes-skills/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

这是一套用于Hermes Agent的技能集，专注于从网页和GitHub学习技术文档并建立知识库。

## 📚 技能列表

### 1. web-documentation-reader
**阅读和提取网页技术文档、API文档、教程的结构化内容**

功能特点：
- 📖 读取各类技术文档网站
- 📝 提取Markdown文档
- 🔍 解析HTML结构化内容
- 💻 提取代码示例
- 💾 保存到知识库（Obsidian格式）

支持的文档平台：
- GitHub文档和Wiki
- Read the Docs
- 官方技术文档网站
- API参考文档

### 2. github-project-learner
**深入学习GitHub项目：README、文档、代码结构、Issues、Wiki**

功能特点：
- ℹ️ 获取项目基本信息和统计
- 📄 读取README和所有文档
- 🗂️ 分析项目结构
- 📦 获取依赖信息
- 💬 分析Issues和讨论
- 🔄 批量学习多个项目

支持的功能：
- 项目元数据提取
- 文档自动下载
- 代码语言统计
- 贡献者分析
- Release信息获取

## 🚀 快速开始

### 安装

将技能复制到Hermes技能目录：

```bash
# Linux/macOS
cp -r web-documentation-reader ~/.hermes/skills/research/
cp -r github-project-learner ~/.hermes/skills/research/

# Windows
copy web-documentation-reader %LOCALAPPDATA%\hermes\skills\research\
copy github-project-learner %LOCALAPPDATA%\hermes\skills\research\
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 使用示例

#### 提取网页文档

```bash
python3 web-documentation-reader/scripts/extract_docs.py https://docs.python.org/3/tutorial/
```

#### 学习GitHub项目

```bash
python3 github-project-learner/scripts/learn_project.py snapcast/snapcast
```

更多示例请查看 [EXAMPLES.md](EXAMPLES.md)

## 📖 文档

- [使用示例](EXAMPLES.md) - 详细的使用指南和API文档
- [贡献指南](CONTRIBUTING.md) - 如何为项目做贡献
- [许可证](LICENSE) - MIT开源许可证

## 🛠️ 依赖

### Python包
```bash
pip install requests beautifulsoup4 lxml
```

### 系统工具
- curl
- git
- python3 (3.8+)

## ⚙️ 配置

### GitHub API Token（可选）

为了避免API限流，建议配置GitHub Personal Access Token：

```bash
export GITHUB_TOKEN="your_token_here"
```

**速率限制：**
- 未认证：60次/小时
- 已认证：5000次/小时

## 📊 输出格式

所有学到的内容都会保存为Markdown格式，包含：

- 元数据（来源、日期、标签）
- 结构化内容
- 代码示例
- 链接和引用

适合导入到Obsidian等知识管理工具。

## 🎯 实际应用案例

我使用这些技能从GitHub学习了嵌入式音频相关的知识，并建立了完整的知识库：

1. **Snapcast多房间音频同步系统** - 学习了工作原理、架构设计、配置方法
2. **A133音频系统** - 整理了完整的服务架构和配置
3. **PulseAudio音频路由** - 理解了核心概念和蓝牙路由机制
4. **ALSA Loopback** - 掌握了虚拟声卡的工作原理

## 🤝 贡献

我们欢迎所有形式的贡献！

- 🐛 [报告Bug](https://github.com/xiaomao488/hermes-skills/issues/new?template=bug_report.md)
- 💡 [提出新功能](https://github.com/xiaomao488/hermes-skills/issues/new?template=feature_request.md)
- 📝 改进文档
- 🔧 提交代码

请阅读 [贡献指南](CONTRIBUTING.md) 了解详情。

### 贡献者

感谢所有贡献者！

<!-- 这里会自动显示贡献者头像 -->
<a href="https://github.com/xiaomao488/hermes-skills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=xiaomao488/hermes-skills" />
</a>

## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源。

## 🔗 相关链接

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - 主项目
- [Obsidian](https://obsidian.md/) - 知识管理工具
- [GitHub API](https://docs.github.com/en/rest) - GitHub API文档

## 💬 联系方式

- GitHub Issues: [提问或反馈](https://github.com/xiaomao488/hermes-skills/issues)
- GitHub Discussions: [讨论和交流](https://github.com/xiaomao488/hermes-skills/discussions)

## ⭐ Star History

如果这个项目对你有帮助，请给它一个Star！

[![Star History Chart](https://api.star-history.com/svg?repos=xiaomao488/hermes-skills&type=Date)](https://star-history.com/#xiaomao488/hermes-skills&Date)

---

**Made with ❤️ for Hermes Agent**
