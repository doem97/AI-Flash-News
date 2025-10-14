# 🌅 AI 每日新闻简报生成系统

自动从多个AI新闻源抓取、分析和生成每日AI新闻简报的完整工具链。

## ✨ 核心特性

- 🤖 **AI驱动分析** - 使用Claude自主评估新闻重要性，无需预设规则
- 🎯 **智能去重** - 自动对比历史新闻，避免重复报道
- 📊 **JSON输出** - 结构化数据，易于扩展和集成
- 🎨 **Vue 3 + Vite** - 现代化前端框架，极简静态设计
- 🚀 **纯展示页面** - 无交互元素，专为截图优化
- 📱 **移动端优化** - 适配手机屏幕，优雅美观

## 📁 项目结构

```
aidaily/
├── src/                          # Vue 3 源代码
│   ├── components/               # Vue 组件
│   │   ├── NewsViewer.vue       # 新闻查看器主组件
│   │   ├── NewsCard.vue         # 新闻卡片组件
│   │   └── Toast.vue            # Toast提示组件
│   ├── assets/
│   │   └── style.css            # 全局样式
│   ├── App.vue                  # 根组件
│   └── main.js                  # 入口文件
├── public/                      # 静态资源目录
├── ai_news_config.md            # 配置文件：新闻源、评估框架、prompt模板
├── generate_news.py             # Python脚本：调用Claude API生成新闻JSON
├── package.json                 # Node.js 依赖配置
├── vite.config.js               # Vite 配置文件
├── index.html                   # HTML 入口
├── 2025-10-14.json              # 生成的新闻数据（示例）
├── 2025-10-14.txt               # 纯文本备份
└── README.md                    # 使用文档（本文件）
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# Python 依赖
pip install anthropic

# Node.js 依赖
npm install
```

### 2. 配置API Key

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

或在 `~/.bashrc` / `~/.zshrc` 中添加：

```bash
echo 'export ANTHROPIC_API_KEY="your-api-key"' >> ~/.bashrc
source ~/.bashrc
```

### 3. 生成今日简报

```bash
python generate_news.py
```

脚本会自动：
1. 从配置的新闻源抓取最新AI新闻（24-48小时内）
2. 读取历史JSON文件进行去重
3. 使用Claude API分析和筛选重要新闻
4. 生成JSON和TXT两种格式

### 4. 启动开发服务器

```bash
npm run dev
```

Vite会启动开发服务器，输出类似：
```
VITE v5.0.0  ready in 500 ms

➜  Local:   http://localhost:5173/
➜  Network: http://192.168.1.100:5173/
```

**远程服务器访问**：
- 如果在远程服务器上开发，VSCode会自动转发端口
- 或使用 Network 地址在局域网内访问
- 或配置SSH隧道：`ssh -L 5173:localhost:5173 user@server`

### 5. 浏览器中查看和截图

- 访问开发服务器地址（http://localhost:5173）
- 使用浏览器截图工具（Chrome: `Ctrl+Shift+S` / Mac: `Cmd+Shift+5`）
- 或使用"复制文本"按钮复制内容

## 📋 工作流程

```
┌─────────────────────────────────────────────────┐
│  1. 运行 Python 脚本                             │
│     python generate_news.py                     │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  2. 抓取多个新闻源                               │
│     - AI Breakfast                              │
│     - The Neuron Daily                          │
│     - TechCrunch AI                             │
│     - The Verge AI                              │
│     - MIT Tech Review                           │
│     + 更多...                                   │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  3. AI 智能分析                                  │
│     - 对比历史新闻去重                           │
│     - 评估影响范围、创新度、时效性等维度          │
│     - 自主判断重要性（critical/high/medium）      │
│     - 根据重要性调整描述详细程度（20-80字）        │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  4. 生成结构化数据                               │
│     - yyyy-mm-dd.json (供前端使用)              │
│     - yyyy-mm-dd.txt  (纯文本备份)              │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  5. 启动开发服务器                               │
│     npm run dev                                 │
│     ➜ Local: http://localhost:5173/            │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  6. Vue 3 前端渲染                               │
│     - 美观的卡片式布局                           │
│     - 重要性视觉区分                             │
│     - 支持查看历史日期                           │
│     - 热重载，实时预览                           │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  7. 截图分享                                     │
│     - 浏览器截图工具                             │
│     - 或复制纯文本                               │
│     - 分享到社交媒体                             │
└─────────────────────────────────────────────────┘
```

## 🎯 AI 评估框架

系统不预设优先级，让Claude根据以下维度**自主判断**新闻重要性：

### 评估维度

| 维度 | 说明 |
|------|------|
| **影响范围** | 行业级 > 赛道级 > 公司级 |
| **创新程度** | 范式转变 > 显著突破 > 渐进改进 > 常规发布 |
| **时效紧迫性** | 突发事件 > 近期热点 > 持续话题 |
| **实际应用价值** | 可落地性、用户影响、商业价值 |
| **话题性** | 讨论度、争议性、意外性 |

### 重要性分级

- **Critical** (1-3条) - 行业级影响，50-80字详细描述
- **High** (3-5条) - 赛道级影响或高话题性，35-50字
- **Medium** (2-4条) - 值得关注的更新，20-35字

### 字数分配策略

> **信息密度 > 字数要求**
>
> 不硬凑字数，根据信息量自然调整。宁可少一点说清楚，不要为了凑字数加废话。

## 📊 JSON 数据格式

```json
{
  "date": "2025-10-14",
  "date_formatted": "25/10/14",
  "title": "早餐 AI 速读",
  "news": [
    {
      "id": 1,
      "content": "新闻内容（20-80字）",
      "importance": "critical",
      "reasoning": "AI的判断理由",
      "source": "新闻来源",
      "url": "原文链接",
      "keywords": ["关键词1", "关键词2"],
      "category": "技术突破"
    }
  ],
  "metadata": {
    "generated_at": "2025-10-14T08:00:00Z",
    "total_news": 10,
    "sources_checked": ["来源列表"],
    "duplicates_removed": 5,
    "generation_time_seconds": 45.2
  }
}
```

## 🎨 前端功能

### 主要功能

- ✅ 自动加载最新或指定日期的新闻
- ✅ 日期导航（前一天/后一天/今天）
- ✅ 根据重要性区分视觉样式（颜色、字重）
- ✅ 显示关键词标签
- ✅ 链接到原文
- ✅ 复制纯文本到剪贴板
- ✅ 刷新当前页面
- ✅ 分享功能（支持浏览器）
- ✅ 响应式设计（移动端友好）

### 视觉设计

- 🎨 现代化渐变背景
- 💎 卡片式新闻布局
- 🎯 重要性视觉区分（边框颜色、背景）
- ✨ 平滑动画和过渡效果
- 📱 移动端优化

## 🔧 命令行选项

```bash
# 基本用法
python generate_news.py

# 生成指定日期的简报
python generate_news.py --date 2025-10-13

# 不自动打开浏览器
python generate_news.py --no-browser

# 自定义新闻数量（默认10条）
python generate_news.py --count 15

# 查看帮助
python generate_news.py --help
```

## 📰 新闻源配置

当前配置的新闻源（可在 `ai_news_config.md` 中修改）：

| 新闻源 | URL | 特点 |
|--------|-----|------|
| AI Breakfast | https://aibreakfast.beehiiv.com | 每日AI汇总，信息密度高 |
| The Neuron Daily | https://www.theneurondaily.com | 专业AI简报 |
| AI News | https://www.artificialintelligence-news.com | 深度报道 |
| TechCrunch AI | https://techcrunch.com/category/artificial-intelligence/ | 创业和产品 |
| The Verge AI | https://www.theverge.com/ai-artificial-intelligence | 主流科技媒体 |
| VentureBeat AI | https://venturebeat.com/category/ai/ | 企业应用 |
| MIT Tech Review | https://www.technologyreview.com/topic/artificial-intelligence/ | 学术前沿 |

### 添加新闻源

编辑 `ai_news_config.md` 中的新闻源列表，添加：

```markdown
8. **新网站名称** - https://example.com
   - 描述
   - 抓取方法：...
```

然后在 `generate_news.py` 的prompt中添加对应URL即可。

## ⚙️ 自定义配置

### 调整历史回溯天数

编辑 `generate_news.py`：

```python
historical_data = get_historical_news_json(days=7)  # 改为你需要的天数
```

### 修改AI模型

编辑 `generate_news.py`：

```python
message = client.messages.create(
    model="claude-sonnet-4-20250514",  # 改为其他模型
    ...
)
```

### 调整去重阈值

编辑 `ai_news_config.md` 中的去重逻辑部分，修改相似度阈值。

### 自定义样式

编辑 `styles.css`：

```css
:root {
    --color-primary: #6366f1;  /* 主色调 */
    --color-critical: #ef4444; /* critical级别颜色 */
    /* ... */
}
```

## 🤖 自动化运行

### Linux/Mac (cron)

每天早上8点自动生成：

```bash
# 编辑 crontab
crontab -e

# 添加任务
0 8 * * * cd /path/to/aidaily && /usr/bin/python3 generate_news.py --no-browser >> /var/log/ai_news.log 2>&1
```

### Windows (任务计划程序)

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器：每天早上8点
4. 操作：启动程序
   - 程序：`python.exe`
   - 参数：`generate_news.py --no-browser`
   - 起始于：`C:\path\to\aidaily`

## 🐛 故障排查

### 问题：API Key 错误

```
❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量
```

**解决**：

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

### 问题：无法访问某些网站

**解决**：
- 检查网络连接
- 使用代理或VPN
- 临时移除无法访问的新闻源（编辑 `ai_news_config.md`）

### 问题：JSON解析错误

```
❌ JSON 解析错误
```

**解决**：
- Claude有时可能返回包含说明文字的响应，脚本会尝试提取JSON
- 如果仍失败，查看错误日志中的响应内容
- 可能需要调整prompt或重试

### 问题：历史文件加载失败

**解决**：
- 确保JSON文件格式正确
- 删除损坏的历史文件
- 脚本会自动跳过格式错误的文件

### 问题：浏览器未自动打开

**解决**：
- 手动打开 `news_viewer.html`（双击或拖到浏览器）
- 或使用 `--no-browser` 选项，然后手动打开

### 问题：前端显示"未找到数据"

**解决**：
- 确保已运行 `generate_news.py` 生成JSON文件
- 检查JSON文件是否存在于同一目录
- 查看浏览器控制台的错误信息

## 📸 截图分享最佳实践

### Chrome/Edge

1. 按 `Ctrl+Shift+S` (Mac: `Cmd+Shift+S`) 或 `F12` → 更多工具 → 截取屏幕截图
2. 选择"捕获完整大小的屏幕截图"或手动选择区域
3. 保存图片

### Firefox

1. 右键点击页面 → "截取屏幕截图"
2. 选择"保存完整网页"或"保存可见区域"

### Safari

1. `Cmd+Shift+4` 手动选择区域
2. 或使用截图工具应用

### 移动端

- iOS: 长按电源键+音量加
- Android: 电源键+音量减

## 🔮 未来扩展

可能的功能扩展：

- [ ] 支持多语言输出（英文、日文等）
- [ ] 邮件订阅自动发送
- [ ] Telegram/微信机器人推送
- [ ] 历史趋势分析和可视化
- [ ] 关键词词云生成
- [ ] RSS订阅源输出
- [ ] PDF导出功能
- [ ] 语音播报（TTS）
- [ ] 与Notion/飞书等集成

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可

MIT License

## 🙏 致谢

- [Anthropic Claude](https://www.anthropic.com/) - 强大的AI分析能力
- 各大AI新闻源 - 提供优质内容

---

**Enjoy your AI news breakfast! 🌅☕**
