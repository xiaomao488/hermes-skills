---
name: web-documentation-reader
description: "阅读和提取网页技术文档、API文档、教程的结构化内容"
platforms: [linux, macos, windows]
tags: [web, documentation, learning, research]
---

# Web Documentation Reader

## 使用场景

当用户需要：
- 阅读技术文档网站（如官方文档、API参考）
- 学习GitHub README或Wiki
- 提取教程和指南的关键信息
- 分析网页结构化内容
- 建立知识库

## 核心功能

### 1. 读取网页内容

使用curl获取网页HTML：

```bash
# 基本读取
curl -s "https://example.com/docs" -H "User-Agent: Mozilla/5.0"

# 跟随重定向
curl -sL "https://example.com/docs"

# 读取GitHub raw文件
curl -s "https://raw.githubusercontent.com/user/repo/main/README.md"
```

### 2. 提取Markdown文档

对于GitHub、GitLab等平台的Markdown文档：

```bash
# 直接读取raw markdown
curl -s "https://raw.githubusercontent.com/user/repo/main/docs/guide.md"

# 读取多个文档
for doc in README.md INSTALL.md API.md; do
  echo "=== $doc ==="
  curl -s "https://raw.githubusercontent.com/user/repo/main/$doc"
done
```

### 3. 解析HTML文档

使用Python提取关键内容：

```python
from bs4 import BeautifulSoup
import requests

def extract_documentation(url):
    """提取网页文档的主要内容"""
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 移除脚本和样式
    for script in soup(['script', 'style', 'nav', 'footer']):
        script.decompose()
    
    # 提取主要内容
    # 常见的文档容器类名
    main_content = (
        soup.find('main') or 
        soup.find('article') or 
        soup.find(class_=['content', 'documentation', 'markdown-body']) or
        soup.find('body')
    )
    
    return main_content.get_text(separator='\n', strip=True)

# 使用
content = extract_documentation('https://example.com/docs')
print(content)
```

### 4. 提取代码示例

```python
def extract_code_blocks(soup):
    """提取文档中的所有代码块"""
    code_blocks = []
    
    # 查找pre/code标签
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            language = code.get('class', [''])[0].replace('language-', '')
            code_blocks.append({
                'language': language,
                'code': code.get_text()
            })
    
    return code_blocks
```

## 工作流程

### 标准流程

1. **识别文档类型**
   - GitHub/GitLab: 直接读取raw markdown
   - 技术文档网站: 使用HTML解析
   - API文档: 提取结构化内容

2. **提取内容**
   - 标题层级
   - 正文内容
   - 代码示例
   - 链接和引用

3. **结构化整理**
   - 按章节组织
   - 提取关键概念
   - 整理代码示例
   - 建立索引

4. **保存到知识库**
   - 创建Markdown文件
   - 添加元数据
   - 建立链接关系

## 常见文档平台

### GitHub文档

```bash
# README
curl -s "https://raw.githubusercontent.com/user/repo/main/README.md"

# Wiki页面
curl -s "https://raw.githubusercontent.com/wiki/user/repo/Page-Name.md"

# 文档目录
curl -s "https://api.github.com/repos/user/repo/contents/docs" | \
  python3 -c "import sys, json; [print(f['download_url']) for f in json.load(sys.stdin) if f['name'].endswith('.md')]"
```

### Read the Docs

```python
# 通常有良好的HTML结构
url = "https://project.readthedocs.io/en/latest/"
# 使用BeautifulSoup提取
```

### 官方文档网站

```bash
# 很多文档网站提供JSON API
curl -s "https://docs.example.com/api/content/page-slug"
```

## 实用技巧

### 批量下载文档

```bash
# 下载整个文档目录
mkdir -p docs
cd docs

# 从GitHub下载所有markdown文件
curl -s "https://api.github.com/repos/user/repo/contents/docs" | \
  python3 -c "
import sys, json, urllib.request
for f in json.load(sys.stdin):
    if f['name'].endswith('.md'):
        print(f'Downloading {f[\"name\"]}...')
        urllib.request.urlretrieve(f['download_url'], f['name'])
"
```

### 提取目录结构

```python
def extract_toc(soup):
    """提取文档的目录结构"""
    toc = []
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        level = int(heading.name[1])
        text = heading.get_text(strip=True)
        anchor = heading.get('id', '')
        toc.append({
            'level': level,
            'text': text,
            'anchor': anchor
        })
    return toc
```

### 处理分页文档

```python
def fetch_paginated_docs(base_url, page_pattern):
    """获取分页文档"""
    page = 1
    all_content = []
    
    while True:
        url = base_url + page_pattern.format(page=page)
        response = requests.get(url)
        
        if response.status_code != 200:
            break
            
        soup = BeautifulSoup(response.content, 'html.parser')
        content = extract_documentation(soup)
        
        if not content:
            break
            
        all_content.append(content)
        page += 1
    
    return '\n\n'.join(all_content)
```

## 保存到知识库

### 创建结构化笔记

```python
def save_to_obsidian(title, content, metadata, output_dir):
    """保存为Obsidian格式的markdown"""
    
    # 构建frontmatter
    frontmatter = "---\n"
    for key, value in metadata.items():
        frontmatter += f"{key}: {value}\n"
    frontmatter += "---\n\n"
    
    # 完整内容
    full_content = frontmatter + f"# {title}\n\n" + content
    
    # 保存文件
    filename = f"{output_dir}/{title.replace(' ', '-')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    return filename
```

### 元数据示例

```yaml
---
source: https://example.com/docs
date: 2026-05-27
tags: [documentation, api, tutorial]
category: technical-docs
---
```

## 错误处理

### 常见问题

1. **403/401错误**: 需要认证或User-Agent
2. **404错误**: URL不存在或已移动
3. **超时**: 网络问题或服务器响应慢
4. **编码问题**: 使用正确的字符编码

### 解决方案

```python
def robust_fetch(url, max_retries=3):
    """带重试的健壮获取"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # 指数退避
```

## 最佳实践

1. **尊重robots.txt**: 检查网站的爬取规则
2. **添加延迟**: 避免过快请求导致被封
3. **缓存内容**: 避免重复下载相同内容
4. **保留来源**: 记录文档的原始URL和日期
5. **定期更新**: 技术文档经常更新，需要定期同步

## 示例：完整工作流

```python
import requests
from bs4 import BeautifulSoup
import time

def learn_from_documentation(url, output_dir):
    """从文档网站学习并保存到知识库"""
    
    print(f"正在读取: {url}")
    
    # 1. 获取内容
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 2. 提取标题
    title = soup.find('h1')
    title_text = title.get_text(strip=True) if title else 'Untitled'
    
    # 3. 提取主要内容
    main_content = extract_documentation(soup)
    
    # 4. 提取代码示例
    code_blocks = extract_code_blocks(soup)
    
    # 5. 构建markdown
    markdown = f"# {title_text}\n\n"
    markdown += f"**来源:** {url}\n\n"
    markdown += main_content + "\n\n"
    
    if code_blocks:
        markdown += "## 代码示例\n\n"
        for i, block in enumerate(code_blocks, 1):
            markdown += f"### 示例 {i} ({block['language']})\n\n"
            markdown += f"```{block['language']}\n{block['code']}\n```\n\n"
    
    # 6. 保存
    filename = f"{output_dir}/{title_text.replace(' ', '-')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"已保存到: {filename}")
    return filename
```

## 相关技能

- `youtube-content`: 处理视频内容
- `arxiv`: 学术论文检索
- `obsidian`: 管理知识库笔记
