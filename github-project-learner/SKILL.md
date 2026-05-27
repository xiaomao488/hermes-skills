---
name: github-project-learner
description: "深入学习GitHub项目：README、文档、代码结构、Issues、Wiki"
platforms: [linux, macos, windows]
tags: [github, learning, code-analysis, documentation]
---

# GitHub Project Learner

## 使用场景

当用户想要：
- 深入学习某个GitHub开源项目
- 理解项目架构和设计思路
- 提取项目文档和最佳实践
- 分析代码结构和依赖关系
- 建立项目知识库

## 核心功能

### 1. 项目基本信息

使用GitHub API获取项目元数据：

```bash
# 获取仓库信息
curl -s "https://api.github.com/repos/owner/repo" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(f'项目: {data[\"full_name\"]}')
print(f'描述: {data[\"description\"]}')
print(f'Stars: {data[\"stargazers_count\"]}')
print(f'语言: {data[\"language\"]}')
print(f'许可证: {data.get(\"license\", {}).get(\"name\", \"N/A\")}')
print(f'最后更新: {data[\"updated_at\"]}')
"
```

### 2. 读取README和文档

```bash
# 读取README
curl -s "https://raw.githubusercontent.com/owner/repo/main/README.md"

# 读取其他常见文档
for doc in README.md CONTRIBUTING.md CHANGELOG.md LICENSE; do
  echo "=== $doc ==="
  curl -s "https://raw.githubusercontent.com/owner/repo/main/$doc" 2>/dev/null || echo "文件不存在"
done
```

### 3. 获取文档目录结构

```bash
# 列出docs目录的所有文件
curl -s "https://api.github.com/repos/owner/repo/contents/docs" | \
  python3 -c "
import sys, json
try:
    files = json.load(sys.stdin)
    for f in files:
        if f['type'] == 'file':
            print(f'{f[\"name\"]} - {f[\"download_url\"]}')
        elif f['type'] == 'dir':
            print(f'{f[\"name\"]}/ (目录)')
except:
    print('docs目录不存在或为空')
"
```

### 4. 分析项目结构

```bash
# 获取根目录文件列表
curl -s "https://api.github.com/repos/owner/repo/contents" | \
  python3 -c "
import sys, json
files = json.load(sys.stdin)
print('项目结构:')
for f in files:
    icon = '📁' if f['type'] == 'dir' else '📄'
    print(f'{icon} {f[\"name\"]}')
"
```

### 5. 读取Wiki

```bash
# GitHub Wiki是独立的git仓库
# 克隆Wiki
git clone "https://github.com/owner/repo.wiki.git" /tmp/repo-wiki

# 或直接读取Wiki页面
curl -s "https://raw.githubusercontent.com/wiki/owner/repo/Home.md"
```

### 6. 分析Issues和讨论

```bash
# 获取最近的Issues
curl -s "https://api.github.com/repos/owner/repo/issues?state=all&per_page=10" | \
  python3 -c "
import sys, json
issues = json.load(sys.stdin)
print('最近的Issues:')
for issue in issues:
    print(f'#{issue[\"number\"]}: {issue[\"title\"]}')
    print(f'  状态: {issue[\"state\"]} | 评论: {issue[\"comments\"]}')
    print()
"
```

### 7. 获取依赖信息

```bash
# 读取package.json (Node.js)
curl -s "https://raw.githubusercontent.com/owner/repo/main/package.json" | \
  python3 -c "
import sys, json
try:
    pkg = json.load(sys.stdin)
    print('依赖:')
    for dep, ver in pkg.get('dependencies', {}).items():
        print(f'  {dep}: {ver}')
except:
    print('无package.json')
"

# 读取requirements.txt (Python)
curl -s "https://raw.githubusercontent.com/owner/repo/main/requirements.txt"

# 读取Cargo.toml (Rust)
curl -s "https://raw.githubusercontent.com/owner/repo/main/Cargo.toml"
```

## 完整学习工作流

### Python脚本示例

```python
import requests
import json
from pathlib import Path

class GitHubProjectLearner:
    def __init__(self, owner, repo, output_dir):
        self.owner = owner
        self.repo = repo
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}"
        self.raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main"
    
    def get_repo_info(self):
        """获取仓库基本信息"""
        response = requests.get(self.base_url)
        return response.json()
    
    def get_readme(self):
        """获取README内容"""
        for filename in ['README.md', 'README.rst', 'README.txt']:
            url = f"{self.raw_url}/{filename}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        return None
    
    def get_documentation_files(self):
        """获取所有文档文件"""
        docs = []
        
        # 常见文档文件
        doc_files = [
            'README.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
            'LICENSE', 'INSTALL.md', 'USAGE.md', 'API.md'
        ]
        
        for filename in doc_files:
            url = f"{self.raw_url}/{filename}"
            response = requests.get(url)
            if response.status_code == 200:
                docs.append({
                    'filename': filename,
                    'content': response.text
                })
        
        # docs目录
        docs_url = f"{self.base_url}/contents/docs"
        response = requests.get(docs_url)
        if response.status_code == 200:
            for file in response.json():
                if file['type'] == 'file' and file['name'].endswith('.md'):
                    content = requests.get(file['download_url']).text
                    docs.append({
                        'filename': f"docs/{file['name']}",
                        'content': content
                    })
        
        return docs
    
    def get_directory_structure(self, path=''):
        """获取目录结构"""
        url = f"{self.base_url}/contents/{path}"
        response = requests.get(url)
        
        if response.status_code != 200:
            return []
        
        structure = []
        for item in response.json():
            structure.append({
                'name': item['name'],
                'type': item['type'],
                'path': item['path']
            })
        
        return structure
    
    def analyze_and_save(self):
        """分析项目并保存到知识库"""
        print(f"正在学习项目: {self.owner}/{self.repo}")
        
        # 1. 获取基本信息
        info = self.get_repo_info()
        
        # 2. 创建主文档
        main_doc = f"# {info['full_name']}\n\n"
        main_doc += f"**描述:** {info['description']}\n\n"
        main_doc += f"**Stars:** ⭐{info['stargazers_count']}\n"
        main_doc += f"**语言:** {info['language']}\n"
        main_doc += f"**许可证:** {info.get('license', {}).get('name', 'N/A')}\n"
        main_doc += f"**GitHub:** {info['html_url']}\n\n"
        
        # 3. 添加README
        readme = self.get_readme()
        if readme:
            main_doc += "## README\n\n"
            main_doc += readme + "\n\n"
        
        # 4. 获取项目结构
        structure = self.get_directory_structure()
        main_doc += "## 项目结构\n\n"
        for item in structure:
            icon = '📁' if item['type'] == 'dir' else '📄'
            main_doc += f"- {icon} {item['name']}\n"
        main_doc += "\n"
        
        # 5. 保存主文档
        main_file = self.output_dir / f"{self.repo}.md"
        with open(main_file, 'w', encoding='utf-8') as f:
            f.write(main_doc)
        
        print(f"主文档已保存: {main_file}")
        
        # 6. 保存其他文档
        docs = self.get_documentation_files()
        for doc in docs:
            doc_file = self.output_dir / doc['filename'].replace('/', '-')
            with open(doc_file, 'w', encoding='utf-8') as f:
                f.write(doc['content'])
            print(f"文档已保存: {doc_file}")
        
        return main_file

# 使用示例
learner = GitHubProjectLearner('snapcast', 'snapcast', 'E:/Obsidian笔记/GitHub项目')
learner.analyze_and_save()
```

## 快速命令

### 一键学习项目

```bash
#!/bin/bash
# learn_github_project.sh

OWNER=$1
REPO=$2
OUTPUT_DIR=$3

echo "学习项目: $OWNER/$REPO"

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 获取README
echo "=== README ===" > "$OUTPUT_DIR/$REPO.md"
curl -s "https://raw.githubusercontent.com/$OWNER/$REPO/main/README.md" >> "$OUTPUT_DIR/$REPO.md"

# 获取其他文档
for doc in CONTRIBUTING.md CHANGELOG.md LICENSE INSTALL.md; do
  echo "获取 $doc..."
  curl -s "https://raw.githubusercontent.com/$OWNER/$REPO/main/$doc" > "$OUTPUT_DIR/$doc" 2>/dev/null
done

# 获取docs目录
echo "获取文档目录..."
curl -s "https://api.github.com/repos/$OWNER/$REPO/contents/docs" | \
  python3 -c "
import sys, json, urllib.request
try:
    files = json.load(sys.stdin)
    for f in files:
        if f['type'] == 'file' and f['name'].endswith('.md'):
            print(f'下载: {f[\"name\"]}')
            urllib.request.urlretrieve(f['download_url'], '$OUTPUT_DIR/docs-' + f['name'])
except:
    pass
"

echo "完成！文档保存在: $OUTPUT_DIR"
```

### 使用方法

```bash
chmod +x learn_github_project.sh
./learn_github_project.sh snapcast snapcast "E:/Obsidian笔记/GitHub项目"
```

## 高级功能

### 1. 分析代码统计

```bash
# 使用GitHub API获取语言统计
curl -s "https://api.github.com/repos/owner/repo/languages" | \
  python3 -c "
import sys, json
langs = json.load(sys.stdin)
total = sum(langs.values())
print('代码语言分布:')
for lang, bytes in sorted(langs.items(), key=lambda x: x[1], reverse=True):
    percent = (bytes / total) * 100
    print(f'  {lang}: {percent:.1f}%')
"
```

### 2. 获取贡献者信息

```bash
curl -s "https://api.github.com/repos/owner/repo/contributors?per_page=10" | \
  python3 -c "
import sys, json
contributors = json.load(sys.stdin)
print('主要贡献者:')
for c in contributors:
    print(f'  {c[\"login\"]}: {c[\"contributions\"]} commits')
"
```

### 3. 分析提交历史

```bash
curl -s "https://api.github.com/repos/owner/repo/commits?per_page=10" | \
  python3 -c "
import sys, json
commits = json.load(sys.stdin)
print('最近提交:')
for c in commits:
    print(f'  {c[\"commit\"][\"message\"].split(chr(10))[0]}')
    print(f'    作者: {c[\"commit\"][\"author\"][\"name\"]}')
    print(f'    日期: {c[\"commit\"][\"author\"][\"date\"]}')
    print()
"
```

### 4. 获取Release信息

```bash
curl -s "https://api.github.com/repos/owner/repo/releases/latest" | \
  python3 -c "
import sys, json
release = json.load(sys.stdin)
print(f'最新版本: {release[\"tag_name\"]}')
print(f'发布日期: {release[\"published_at\"]}')
print(f'说明:\n{release[\"body\"]}')
"
```

## 批量学习多个项目

```python
def learn_multiple_projects(projects, output_base_dir):
    """批量学习多个GitHub项目"""
    
    for owner, repo in projects:
        print(f"\n{'='*50}")
        print(f"学习项目: {owner}/{repo}")
        print('='*50)
        
        output_dir = f"{output_base_dir}/{repo}"
        learner = GitHubProjectLearner(owner, repo, output_dir)
        
        try:
            learner.analyze_and_save()
            print(f"✓ {repo} 学习完成")
        except Exception as e:
            print(f"✗ {repo} 学习失败: {e}")
        
        # 避免API限流
        time.sleep(2)

# 使用示例
projects = [
    ('snapcast', 'snapcast'),
    ('HEnquist', 'camilladsp'),
    ('mikebrady', 'shairport-sync'),
]

learn_multiple_projects(projects, 'E:/Obsidian笔记/GitHub项目')
```

## 注意事项

### API限流

GitHub API有速率限制：
- 未认证: 60次/小时
- 认证: 5000次/小时

**使用Personal Access Token:**

```bash
# 设置token
export GITHUB_TOKEN="your_token_here"

# 使用token
curl -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/owner/repo"
```

### 最佳实践

1. **缓存结果**: 避免重复请求相同内容
2. **批量处理**: 使用延迟避免触发限流
3. **错误处理**: 优雅处理404和API错误
4. **保留元数据**: 记录学习时间和来源URL
5. **定期更新**: 项目会持续更新，需要定期同步

## 相关技能

- `web-documentation-reader`: 通用网页文档阅读
- `github-repo-management`: GitHub仓库管理
- `obsidian`: 知识库管理
