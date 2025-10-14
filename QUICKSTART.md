# 🚀 快速开始指南

## 第一次使用

### 1. 克隆或下载项目
```bash
cd /your/workspace/
git clone <your-repo> aidaily
cd aidaily
```

### 2. 安装依赖

```bash
# Python依赖
pip install anthropic

# Node.js依赖
npm install
```

### 3. 配置API Key

```bash
# 临时设置（当前终端有效）
export ANTHROPIC_API_KEY="sk-ant-xxx"

# 或永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export ANTHROPIC_API_KEY="sk-ant-xxx"' >> ~/.bashrc
source ~/.bashrc
```

### 4. 生成第一条新闻

```bash
python generate_news.py
```

等待1-2分钟，会生成：
- `2025-10-14.json` - 结构化新闻数据
- `2025-10-14.txt` - 纯文本备份

### 5. 启动开发服务器

```bash
npm run dev
```

你会看到类似输出：
```
VITE v5.0.0  ready in 500 ms

➜  Local:   http://localhost:5173/
➜  Network: http://192.168.1.100:5173/
```

### 6. 打开浏览器

**本地访问**：
- 浏览器打开 `http://localhost:5173/`

**远程服务器（VSCode）**：
- VSCode会自动转发端口5173
- 在PORTS面板找到转发的地址
- 或者点击VSCode底部状态栏的端口号

**远程服务器（SSH隧道）**：
```bash
# 在本地机器运行
ssh -L 5173:localhost:5173 user@your-server
# 然后浏览器打开 http://localhost:5173/
```

---

## 日常使用

### 每天早上生成新闻

```bash
# 1. 生成今日新闻（1-2分钟）
python generate_news.py

# 2. 如果开发服务器未运行，启动它
npm run dev

# 3. 刷新浏览器页面即可看到最新新闻
```

### 查看历史新闻

- 在浏览器界面点击 ◀ / ▶ 按钮
- 或点击"今天"按钮回到当日

---

## 常用命令

```bash
# 生成新闻（默认今天）
python generate_news.py

# 生成指定日期的新闻
python generate_news.py --date 2025-10-13

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览构建结果
npm run preview
```

---

## 截图分享

### Chrome / Edge
1. 按 `F12` 打开开发者工具
2. `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
3. 输入 `screenshot`
4. 选择 "Capture full size screenshot" 或 "Capture node screenshot"

或直接：
- `Ctrl+Shift+S` (Windows)
- `Cmd+Shift+5` (Mac)

### Firefox
1. 右键点击页面
2. 选择"截取屏幕截图"
3. 选择"保存完整网页"或"保存可见区域"

---

## 故障排查

### 问题：npm install 失败

**解决**：
```bash
# 清除缓存
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### 问题：端口5173已被占用

**解决**：
```bash
# 方法1：修改端口
# 编辑 vite.config.js，改为其他端口如5174

# 方法2：杀掉占用的进程
lsof -ti:5173 | xargs kill -9
```

### 问题：页面显示"未找到数据"

**解决**：
```bash
# 确保已生成JSON文件
ls -l *.json

# 如果没有，运行生成脚本
python generate_news.py

# 刷新浏览器
```

### 问题：VSCode端口转发不work

**解决**：
1. 打开VSCode的"PORTS"面板（底部）
2. 点击"Forward a Port"
3. 输入 `5173`
4. 右键端口 → "Port Visibility" → "Public"

---

## 自动化（可选）

### 每天自动生成新闻

**Linux/Mac (cron)**：
```bash
# 编辑crontab
crontab -e

# 添加（每天早上8点）
0 8 * * * cd /path/to/aidaily && /usr/bin/python3 generate_news.py >> /var/log/ai_news.log 2>&1
```

**Windows (任务计划程序)**：
1. 打开"任务计划程序"
2. 创建基本任务
3. 触发器：每天 08:00
4. 操作：启动程序
   - 程序：`python.exe`
   - 参数：`generate_news.py`
   - 起始于：`C:\path\to\aidaily`

---

## 下一步

- 📝 查看 `ai_news_config.md` 了解如何自定义新闻源和评估框架
- 🎨 修改 `src/assets/style.css` 自定义样式
- 🔧 编辑 `src/components/*.vue` 修改界面布局
- 📊 扩展JSON格式添加更多元数据

**Enjoy your AI news breakfast! 🌅☕**
