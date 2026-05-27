# Hermes Skills - Web Documentation Learning Toolkit

[![GitHub stars](https://img.shields.io/github/stars/xiaomao488/hermes-skills?style=social)](https://github.com/xiaomao488/hermes-skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xiaomao488/hermes-skills?style=social)](https://github.com/xiaomao488/hermes-skills/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[中文文档](README.md) | English

A collection of skills for Hermes Agent focused on learning technical documentation from web pages and GitHub, and building knowledge bases.

## 📚 Skills

### 1. web-documentation-reader
**Read and extract structured content from web technical documentation, API docs, and tutorials**

Features:
- 📖 Read various technical documentation websites
- 📝 Extract Markdown documents
- 🔍 Parse structured HTML content
- 💻 Extract code examples
- 💾 Save to knowledge base (Obsidian format)

Supported platforms:
- GitHub documentation and Wiki
- Read the Docs
- Official technical documentation sites
- API reference documentation

### 2. github-project-learner
**Deep learning of GitHub projects: README, docs, code structure, Issues, Wiki**

Features:
- ℹ️ Get project basic info and statistics
- 📄 Read README and all documentation
- 🗂️ Analyze project structure
- 📦 Get dependency information
- 💬 Analyze Issues and discussions
- 🔄 Batch learning of multiple projects

Supported functions:
- Project metadata extraction
- Automatic documentation download
- Code language statistics
- Contributor analysis
- Release information retrieval

## 🚀 Quick Start

### Installation

Copy skills to Hermes skills directory:

```bash
# Linux/macOS
cp -r web-documentation-reader ~/.hermes/skills/research/
cp -r github-project-learner ~/.hermes/skills/research/

# Windows
copy web-documentation-reader %LOCALAPPDATA%\hermes\skills\research\
copy github-project-learner %LOCALAPPDATA%\hermes\skills\research\
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage Examples

#### Extract Web Documentation

```bash
python3 web-documentation-reader/scripts/extract_docs.py https://docs.python.org/3/tutorial/
```

#### Learn GitHub Project

```bash
python3 github-project-learner/scripts/learn_project.py snapcast/snapcast
```

For more examples, see [EXAMPLES.md](EXAMPLES.md)

## 📖 Documentation

- [Usage Examples](EXAMPLES.md) - Detailed usage guide and API documentation
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project
- [License](LICENSE) - MIT Open Source License
- [Setup Guide](SETUP_GUIDE.md) - Complete setup instructions
- [CDP Troubleshooting](CDP_TROUBLESHOOTING.md) - Browser connection troubleshooting

## 🛠️ Dependencies

### Python Packages
```bash
pip install requests beautifulsoup4 lxml
```

### System Tools
- curl
- git
- python3 (3.8+)

## ⚙️ Configuration

### GitHub API Token (Optional)

To avoid API rate limiting, it's recommended to configure a GitHub Personal Access Token:

```bash
export GITHUB_TOKEN="your_token_here"
```

**Rate Limits:**
- Unauthenticated: 60 requests/hour
- Authenticated: 5000 requests/hour

## 📊 Output Format

All learned content is saved in Markdown format, including:

- Metadata (source, date, tags)
- Structured content
- Code examples
- Links and references

Suitable for importing into knowledge management tools like Obsidian.

## 🎯 Real-World Use Cases

I used these skills to learn embedded audio knowledge from GitHub and built a complete knowledge base:

1. **Snapcast Multi-room Audio Sync** - Learned working principles, architecture design, configuration methods
2. **A133 Audio System** - Organized complete service architecture and configuration
3. **PulseAudio Audio Routing** - Understood core concepts and Bluetooth routing mechanisms
4. **ALSA Loopback** - Mastered virtual sound card working principles

## 🤝 Contributing

We welcome all forms of contributions!

- 🐛 [Report Bugs](https://github.com/xiaomao488/hermes-skills/issues/new?template=bug_report.md)
- 💡 [Suggest Features](https://github.com/xiaomao488/hermes-skills/issues/new?template=feature_request.md)
- 📝 Improve documentation
- 🔧 Submit code

Please read the [Contributing Guide](CONTRIBUTING.md) for details.

### Contributors

Thanks to all contributors!

<!-- Contributors will be automatically displayed here -->
<a href="https://github.com/xiaomao488/hermes-skills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=xiaomao488/hermes-skills" />
</a>

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 🔗 Related Links

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Main project
- [Obsidian](https://obsidian.md/) - Knowledge management tool
- [GitHub API](https://docs.github.com/en/rest) - GitHub API documentation

## 💬 Contact

- GitHub Issues: [Questions or Feedback](https://github.com/xiaomao488/hermes-skills/issues)
- GitHub Discussions: [Discussion and Communication](https://github.com/xiaomao488/hermes-skills/discussions)

## ⭐ Star History

If this project helps you, please give it a Star!

[![Star History Chart](https://api.star-history.com/svg?repos=xiaomao488/hermes-skills&type=Date)](https://star-history.com/#xiaomao488/hermes-skills&Date)

---

**Made with ❤️ for Hermes Agent**
