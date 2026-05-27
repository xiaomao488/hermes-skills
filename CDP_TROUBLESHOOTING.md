# CDP 浏览器连接故障排查指南

## 问题描述
执行 `/browser connect` 后，浏览器工具无法连接到CDP端口，报错：
```
CDP WebSocket connect failed: HTTP error: 200 OK
```

## 已完成的修复

### 1. 配置文件已更新
文件位置：`C:\Users\ZhuanZ\AppData\Local\hermes\config.yaml`

已将：
```yaml
cdp_url: ''
```

修改为：
```yaml
cdp_url: 'http://localhost:9222'
```

备份文件：`config.yaml.backup`

## 需要手动完成的步骤

### 方案1：重启Hermes（推荐）

1. 退出当前Hermes会话
2. 重新启动Hermes
3. 启动Edge调试模式：
   ```bash
   msedge --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir="$TEMP/edge-debug"
   ```
4. 在Hermes中执行：
   ```
   /browser connect
   ```
5. 测试连接：
   ```
   访问 https://github.com/xiaomao488/hermes-skills
   ```

### 方案2：使用命令行工具完成GitHub配置

如果浏览器连接仍有问题，可以直接在浏览器中手动完成以下配置：

#### 1. 添加 Topics
访问：https://github.com/xiaomao488/hermes-skills

1. 点击右侧 **About** 区域的 ⚙️ 齿轮图标
2. 在 **Topics** 框中输入并回车添加：
   - `hermes-agent`
   - `documentation`
   - `github`
   - `learning`
   - `knowledge-base`
   - `ai-agent`
   - `automation`
   - `python`
3. 点击 **Save changes**

#### 2. 启用 Discussions
访问：https://github.com/xiaomao488/hermes-skills/settings

1. 在左侧菜单找到 **General**
2. 向下滚动到 **Features** 部分
3. 勾选 ✅ **Discussions**
4. 点击 **Set up discussions**

#### 3. 创建 Release
访问：https://github.com/xiaomao488/hermes-skills/releases/new

1. **Choose a tag:** 选择 `v1.0.0`
2. **Release title:** 输入 `v1.0.0 - 首次发布`
3. **Describe this release:** 复制 `QUICK_SETUP_CHECKLIST.md` 中的内容
4. 勾选 ✅ **Set as the latest release**
5. 点击 **Publish release**

## 验证CDP连接

### 检查CDP端口
```bash
curl http://localhost:9222/json/version
```

应该返回包含 `webSocketDebuggerUrl` 的JSON。

### 检查配置
```bash
grep "cdp_url:" "$LOCALAPPDATA/hermes/config.yaml"
```

应该显示：
```
cdp_url: 'http://localhost:9222'
```

### 测试WebSocket连接
```bash
curl -i -N -H "Connection: Upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Version: 13" -H "Sec-WebSocket-Key: test" http://localhost:9222/devtools/browser/d1df0499-0231-4158-a36e-1f24dc8dd9fa
```

应该返回 `101 Switching Protocols`。

## 常见问题

### Q: 为什么修改配置后还是连接失败？
A: Hermes需要重启才能加载新的配置文件。

### Q: Edge浏览器关闭后CDP端口还开着吗？
A: 不会，关闭Edge后CDP端口会关闭。需要重新启动调试模式。

### Q: 可以用Chrome代替Edge吗？
A: 可以，使用：
```bash
chrome --remote-debugging-port=9222 --remote-allow-origins=*
```

### Q: 如何确认Edge是否在调试模式？
A: 访问 http://localhost:9222/json 应该能看到打开的页面列表。

## 技术细节

### CDP协议
Chrome DevTools Protocol (CDP) 允许外部工具通过WebSocket连接控制浏览器。

### 连接流程
1. Hermes读取 `config.yaml` 中的 `cdp_url`
2. 向 `http://localhost:9222/json` 发送HTTP请求获取页面列表
3. 选择目标页面的 `webSocketDebuggerUrl`
4. 建立WebSocket连接
5. 通过CDP协议发送命令

### 错误 "HTTP error: 200 OK"
这个错误很奇怪，因为200是成功状态码。可能的原因：
- Hermes的CDP客户端期望不同的响应格式
- WebSocket握手失败
- 配置未生效（需要重启）

## 下一步

完成上述配置后，你的GitHub仓库将具备：
- ✅ 专业的项目标签（提高可发现性）
- ✅ 社区讨论区（用户交流）
- ✅ 正式版本发布（版本管理）

---

**创建时间：** 2025-05-27  
**状态：** 待验证
