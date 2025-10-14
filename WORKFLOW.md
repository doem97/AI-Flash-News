# 🎯 AI 新闻生成工作流

> 这是项目的唯一核心配置文件。使用时只需告诉 Claude Code："按照 WORKFLOW.md 生成今天的新闻"

---

## 📰 新闻源列表

从以下网站抓取最近 24-48 小时的 AI 相关新闻：

| 新闻源 | URL | 优先级 |
|--------|-----|--------|
| AI Breakfast | https://aibreakfast.beehiiv.com | ⭐⭐⭐ |
| The Neuron Daily | https://www.theneurondaily.com | ⭐⭐⭐ |
| Artificial Intelligence News | https://www.artificialintelligence-news.com | ⭐⭐ |
| TechCrunch AI | https://techcrunch.com/category/artificial-intelligence/ | ⭐⭐⭐ |
| The Verge AI | https://www.theverge.com/ai-artificial-intelligence | ⭐⭐ |
| VentureBeat AI | https://venturebeat.com/category/ai/ | ⭐⭐ |
| MIT Technology Review | https://www.technologyreview.com/topic/artificial-intelligence/ | ⭐⭐ |
| Hacker News | https://news.ycombinator.com | ⭐⭐ |

**补充源（可选）：**
- Reddit r/artificial: https://www.reddit.com/r/artificial/

---

## ⚖️ 新闻评估标准

### 评估维度

对每条新闻，从以下 5 个维度综合评估：

1. **影响范围**
   - 行业级：改变整个 AI 行业格局（如新法规、重大突破）
   - 赛道级：影响特定 AI 细分领域
   - 公司级：单个公司/产品动态

2. **创新程度**
   - 范式转变：全新的技术路径或方法论
   - 显著突破：现有框架内的重要进展
   - 渐进改进：常规性的优化和迭代
   - 常规发布：预期内的产品更新

3. **时效紧迫性**
   - 突发事件：今日发生的重大事件
   - 近期热点：最近 1-2 天的重要动态
   - 持续话题：正在发酵的长期议题

4. **实际应用价值**
   - 可落地性：技术是否已经可以实际应用
   - 用户影响：对终端用户的直接影响
   - 商业价值：对产业的实际推动作用

5. **话题性和争议度**
   - 引发讨论：是否可能引起广泛讨论
   - 存在争议：是否涉及伦理、安全等敏感话题
   - 意外性：是否出乎预期

### 重要性分级

- **critical**：满足多个高分维度，行业级影响（1-3 条）
- **high**：满足部分高分维度，赛道级影响或高话题性（3-5 条）
- **medium**：值得关注的常规更新（2-4 条）

### 字数要求

根据重要性调整描述详细程度：

- **critical**：50-80 字
  - 包含：关键主体 + 核心内容 + 背景/原因 + 影响/意义

- **high**：35-50 字
  - 包含：关键主体 + 核心内容 + 简要影响

- **medium**：20-35 字
  - 包含：关键主体 + 核心事实

**原则：信息密度优先，不要为凑字数加废话**

### 写作规范

1. **标题（title）**：不超过 15 字，高度提炼
2. **内容（content）**：必须独立完整，包含完整主语和上下文
3. **中英文混排规则（重要！）**：中文和英文/数字交接处**必须有空格**
   - ✅ 正确：`OpenAI 发布`、`AI 简讯`、`GPT-4 模型`、`10 月 15 日`
   - ❌ 错误：`OpenAI发布`、`AI简讯`、`GPT-4模型`、`10月15日`
   - ✅ 正确：`Meta 推出 Llama 3.2 轻量版`
   - ❌ 错误：`Meta推出Llama 3.2轻量版`
4. **客观中立**：避免过度夸张
5. **中文流畅**：避免翻译腔

---

## 🗑️ 去重规则

### 历史数据检查

1. 读取最近 **7 天**的历史 JSON 文件（`data/YYYY-MM-DD.json`）
2. 提取所有已报道新闻的 `content` 和 `keywords`
3. 与新抓取的内容对比

### 去重判断

- **完全重复**（相似度 > 85%）→ 直接过滤
- **延续报道**（相似度 60-85%）→ 仅保留有实质新进展的
- **相似话题**（相似度 < 60%）→ 保留，但突出差异

---

## 📋 JSON 输出格式

```json
{
  "date": "2025-10-15",
  "date_formatted": "25/10/15",
  "title": "AI 闪电快讯",
  "news": [
    {
      "id": 1,
      "title": "新闻标题（≤15字）",
      "content": "新闻详细内容（20-80字，根据重要性调整）",
      "importance": "critical",
      "reasoning": "判断为 critical 的理由：影响范围（行业级）+ 创新程度（范式转变）",
      "source": "TechCrunch",
      "url": "https://...",
      "keywords": ["关键词1", "关键词2", "关键词3"],
      "category": "技术突破"
    }
  ],
  "metadata": {
    "generated_at": "2025-10-15T08:00:00Z",
    "total_news": 10,
    "sources_checked": ["AI Breakfast", "TechCrunch", "..."],
    "duplicates_removed": 5,
    "generation_time_seconds": 120.5
  }
}
```

### 字段说明

- **date**: ISO 格式日期（YYYY-MM-DD）
- **date_formatted**: 显示格式（YY/MM/DD）
- **title**: 固定为 "AI 闪电快讯"
- **news[]**: 新闻数组（8-12 条）
  - **id**: 排序序号（1-based）
  - **title**: 新闻标题（≤15 字）
  - **content**: 新闻描述（20-80 字）
  - **importance**: "critical" | "high" | "medium"
  - **reasoning**: AI 判断理由（供参考）
  - **source**: 新闻来源网站
  - **url**: 原文链接（必填）
  - **keywords**: 2-4 个关键词
  - **category**: 技术突破/产品发布/政策法规/投融资/行业动态/安全伦理
- **metadata**: 元数据
  - **generated_at**: 生成时间（ISO 8601）
  - **total_news**: 新闻总数
  - **sources_checked**: 已检查的新闻源列表
  - **duplicates_removed**: 去重数量
  - **generation_time_seconds**: 生成耗时

---

## ✅ 质量检查清单

生成后自我检查：

- [ ] 是否有重复/高度相似的新闻？
- [ ] critical 级别的新闻是否真的够重要？
- [ ] 字数是否符合 importance 级别？
- [ ] 每条新闻的信息密度是否足够？
- [ ] 是否所有新闻都来自最近 24-48 小时？
- [ ] JSON 格式是否有效？
- [ ] 是否提供了 reasoning 说明？
- [ ] keywords 是否准确？
- [ ] title 是否不超过 15 字？
- [ ] content 是否独立完整（包含主语）？
- [ ] **中英文之间是否都有空格？**（如 `AI 简讯`、`OpenAI 发布`）

---

## 📂 文件结构

生成的文件应保存在以下位置：

```
data/
├── raw/
│   └── 2025-10-15-raw.txt        # 原始抓取数据（可选）
└── 2025-10-15.json                # 前端使用的 JSON
```

前端会自动从根目录或 `data/` 目录加载最新的 JSON 文件。

---

## 📝 附录：内部执行流程

> 本章节供 Claude Code 参考，用户不需要关心具体步骤

当用户说："按照 WORKFLOW.md 生成今天（YYYY-MM-DD）的 AI 新闻简报"时，Claude Code 会自动执行以下步骤：

1. **抓取新闻源**
   - 使用 WebFetch 工具访问所有配置的新闻源
   - 提取最近 24-48 小时的 AI 相关新闻

2. **保存原始数据（可选）**
   - 将抓取的原始内容保存到 `data/raw/YYYY-MM-DD-raw.txt`
   - 用于后续追溯和调试

3. **读取历史数据去重**
   - 读取 `data/` 目录下最近 7 天的 JSON 文件
   - 提取已报道新闻的关键词和内容
   - 对比新抓取的内容，过滤重复新闻

4. **分析和筛选**
   - 根据评估标准（影响范围、创新程度等）评估每条新闻
   - 判断重要性等级（critical/high/medium）
   - 筛选出 8-12 条最值得关注的新闻

5. **撰写和生成**
   - 根据重要性级别撰写相应长度的描述（20-80 字）
   - 确保中英文混排规范（添加空格）
   - 生成符合格式的 `data/YYYY-MM-DD.json`

6. **质量检查**
   - 对照质量检查清单自我检查
   - 确保所有规范都已满足
