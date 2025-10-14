# AI 新闻简报生成配置

## 新闻源配置

### 主要新闻源
以下是需要抓取的AI新闻网站，按优先级排序：

1. **AI Breakfast** - https://aibreakfast.beehiiv.com
   - 每日AI新闻汇总，信息密度高
   - 抓取方法：获取首页最新一期内容

2. **The Neuron Daily** - https://www.theneurondaily.com
   - 专业AI简报，覆盖面广
   - 抓取方法：获取最新文章列表

3. **Artificial Intelligence News** - https://www.artificialintelligence-news.com
   - AI行业深度报道
   - 抓取方法：获取首页头条和最新文章

4. **TechCrunch AI** - https://techcrunch.com/category/artificial-intelligence/
   - 科技媒体AI专栏，关注创业和产品
   - 抓取方法：获取分类页面最新10篇文章

5. **The Verge AI** - https://www.theverge.com/ai-artificial-intelligence
   - 主流科技媒体AI报道
   - 抓取方法：获取专题页面最新内容

6. **VentureBeat AI** - https://venturebeat.com/category/ai/
   - 企业AI应用和投融资
   - 抓取方法：获取最新文章

7. **MIT Technology Review AI** - https://www.technologyreview.com/topic/artificial-intelligence/
   - 学术和前沿技术报道
   - 抓取方法：获取AI话题最新文章

### 补充新闻源
- **Hacker News** - https://news.ycombinator.com （搜索"AI"相关热门话题）
- **Reddit r/artificial** - https://www.reddit.com/r/artificial/
- **AI Twitter圈** - 关键意见领袖的最新动态

---

## AI 思考评估框架

### 核心原则
**不预设优先级分类**，让AI根据多个维度自主评估每条新闻的重要性，然后自然排序。

### 评估维度

#### 1. 影响范围（Impact Scope）
- **行业级影响**：改变整个AI行业格局（如：新法规、重大突破）
- **赛道级影响**：影响特定AI细分领域（如：某个垂直应用的突破）
- **公司级影响**：单个公司/产品的动态（如：功能更新、融资）

#### 2. 创新程度（Innovation Level）
- **范式转变**：全新的技术路径或方法论
- **显著突破**：在现有框架内的重要进展
- **渐进改进**：常规性的优化和迭代
- **常规发布**：预期内的产品更新

#### 3. 时效紧迫性（Urgency）
- **突发事件**：今日发生的重大事件
- **近期热点**：最近1-2天的重要动态
- **持续话题**：正在发酵的长期议题

#### 4. 实际应用价值（Practical Value）
- **可落地性**：技术是否已经可以实际应用
- **用户影响**：对终端用户的直接影响
- **商业价值**：对产业的实际推动作用

#### 5. 话题性和争议度（Engagement Potential）
- **引发讨论**：是否可能引起广泛讨论
- **存在争议**：是否涉及伦理、安全等敏感话题
- **意外性**：是否出乎预期

### 判断流程

```
对每条候选新闻：
1. 评估上述5个维度
2. 综合判断重要性等级：critical > high > medium
3. 根据重要性决定描述详细程度：
   - critical: 50-80字（包含背景、核心内容、影响分析）
   - high: 35-50字（核心要点 + 简要影响）
   - medium: 20-35字（精炼事实陈述）
4. 提取关键词（2-4个）
5. 记录判断理由
```

### 字数分配策略

**不要硬凑字数**，根据信息量自然调整：

- **信息丰富的重大新闻**：充分展开，可用到70-80字
- **要点明确的重要新闻**：适度精炼，35-50字即可
- **事实性更新**：简洁陈述，20-30字足够

**写作原则**：
- 信息密度 > 字数要求
- 宁可少一点说清楚，不要为了凑字数加废话
- 每个字都要有信息量

---

## 去重逻辑

### 历史数据检查
1. 读取最近 **7天** 的历史JSON文件（`yyyy-mm-dd.json`）
2. 提取所有已报道新闻的关键词和核心内容
3. 建立"已报道内容指纹库"

### 去重判断标准

#### 完全重复（直接过滤）
- 相同的产品发布
- 相同的公司动态
- 相同的研究成果

#### 延续报道（需谨慎处理）
如果是同一事件的后续进展：
- **有实质新进展**：作为新新闻报道，但说明"最新进展"
- **仅观点rehash**：过滤掉
- **数据更新**：如果有新数据，简要报道

#### 相似话题（区别对待）
- 不同公司的相似产品：都可报道，但要突出差异
- 同一技术的不同应用：都可报道

### 去重实施方法
```python
# 伪代码
for new_item in candidate_news:
    for history_file in recent_7_days:
        similarity = calculate_similarity(new_item, history_file.news)
        if similarity > 0.85:  # 高度相似
            skip new_item
        elif similarity > 0.60:  # 中度相似
            check if has_new_development(new_item, history_item)
            if not has_new_development:
                skip new_item
```

---

## JSON 输出格式规范

### 完整数据结构

```json
{
  "date": "2025-10-14",
  "date_formatted": "25/10/14",
  "title": "早餐 AI 速读",
  "news": [
    {
      "id": 1,
      "content": "新闻内容描述（20-80字，根据重要性调整）",
      "importance": "critical",
      "reasoning": "AI判断此新闻为critical的理由：影响范围（行业级）+ 创新程度（范式转变）+ 时效性（突发）",
      "source": "TechCrunch",
      "url": "https://...",
      "keywords": ["关键词1", "关键词2", "关键词3"],
      "category": "技术突破/产品发布/政策法规/投融资/行业动态/安全伦理"
    }
  ],
  "metadata": {
    "generated_at": "2025-10-14T08:00:00Z",
    "total_news": 10,
    "sources_checked": ["AI Breakfast", "TechCrunch", "The Verge", "..."],
    "duplicates_removed": 15,
    "generation_time_seconds": 45.2
  }
}
```

### 字段说明

- **date**: ISO格式日期 `YYYY-MM-DD`
- **date_formatted**: 显示格式 `YY/MM/DD`
- **title**: 固定为"早餐 AI 速读"
- **news[]**: 新闻数组（8-12条，根据当日重要新闻数量调整）
  - **id**: 排序序号（1-based）
  - **content**: 新闻描述（中文，20-80字）
  - **importance**: 重要性级别（"critical" | "high" | "medium"）
  - **reasoning**: AI的判断理由（供调试用，前端不显示）
  - **source**: 新闻来源网站
  - **url**: 原文链接（可选，优先提供）
  - **keywords**: 2-4个关键词（用于去重和标签显示）
  - **category**: 新闻分类（可选）
- **metadata**: 元数据
  - **generated_at**: 生成时间（ISO 8601）
  - **total_news**: 新闻总数
  - **sources_checked**: 已检查的新闻源列表
  - **duplicates_removed**: 去重数量
  - **generation_time_seconds**: 生成耗时

---

## 完整生成 Prompt 模板

以下是用于Claude API的完整prompt：

```
你是一个资深的AI行业分析师，负责生成每日AI新闻简报。

## 今日任务
生成 {today_date_formatted} 的AI新闻简报，输出为JSON格式。

## 第一步：抓取和收集新闻
从以下新闻源获取最近24-48小时的AI相关新闻：
- AI Breakfast: https://aibreakfast.beehiiv.com
- The Neuron Daily: https://www.theneurondaily.com
- AI News: https://www.artificialintelligence-news.com
- TechCrunch AI: https://techcrunch.com/category/artificial-intelligence/
- The Verge AI: https://www.theverge.com/ai-artificial-intelligence
- VentureBeat AI: https://venturebeat.com/category/ai/
- MIT Tech Review: https://www.technologyreview.com/topic/artificial-intelligence/

请使用可用的工具（如WebFetch）访问这些网站，提取最新的AI新闻标题和内容。

## 第二步：去重检查
以下是最近7天已报道的新闻内容：

{historical_news_json}

请对比新抓取的新闻，过滤掉：
1. 完全重复的内容（相似度 > 85%）
2. 无实质新进展的延续报道（相似度 60-85%）
3. 保留：不同角度的相似话题、有新进展的后续报道

## 第三步：评估和筛选
对每条候选新闻，根据以下框架进行评估：

### 评估维度
1. **影响范围**：行业级 > 赛道级 > 公司级
2. **创新程度**：范式转变 > 显著突破 > 渐进改进 > 常规发布
3. **时效紧迫性**：突发事件 > 近期热点 > 持续话题
4. **实际应用价值**：可落地性、用户影响、商业价值
5. **话题性**：讨论度、争议性、意外性

### 重要性分级
- **critical**: 满足多个高分维度，行业级影响
- **high**: 满足部分高分维度，赛道级影响或高话题性
- **medium**: 值得关注的常规更新

### 筛选目标
选出 8-12 条最值得关注的新闻，其中：
- critical 级别：1-3条
- high 级别：3-5条
- medium 级别：2-4条

**注意**：如果某日重大新闻特别多，可以全部选critical/high级别，不必硬凑medium。

## 第四步：撰写新闻描述

### 字数分配
- **critical**: 50-80字
  - 包含：关键主体 + 核心内容 + 背景/原因 + 影响/意义
  - 示例：三星用"递归"小模型颠覆认知：在特定逻辑推理上，它击败了比自己大一万倍的巨型模型，证明了"更大不一定更好"。（60字）

- **high**: 35-50字
  - 包含：关键主体 + 核心内容 + 简要影响
  - 示例：AI模型"中毒"风险被量化：Anthropic证实，向训练数据中混入仅250份"毒数据"，就足以给大模型植入后门。（50字）

- **medium**: 20-35字
  - 包含：关键主体 + 核心事实
  - 示例：谷歌Gemini-3传闻或于10月22日发布，支持原创音乐生成。（28字）

### 写作原则
1. **信息密度优先**：不为凑字数加废话
2. **核心要素完整**："谁/什么/为什么/影响"
3. **客观中立**：避免"震惊"、"颠覆"等夸张词汇（除非真的震惊）
4. **专业术语适度**：既要准确，也要易懂
5. **中文流畅**：避免翻译腔

## 第五步：输出JSON

按照以下格式输出（确保是有效的JSON）：

{json_format_template}

## 重要提醒
1. 必须输出有效的JSON格式（可以先在reasoning中思考，最后输出纯JSON）
2. 所有新闻按importance排序（critical在前，medium在后）
3. 每条新闻都要提供reasoning，说明为什么判断为该级别
4. 尽可能提供原文URL
5. keywords要准确，用于去重和标签

请开始执行任务，输出今日AI新闻简报的JSON数据。
```

---

## 质量检查清单

生成后自我检查：

- [ ] 是否有重复/高度相似的新闻？
- [ ] critical级别的新闻是否真的够重要？
- [ ] 字数是否符合importance级别？
- [ ] 每条新闻的信息密度是否足够？
- [ ] 是否所有新闻都来自最近24-48小时？
- [ ] JSON格式是否有效？
- [ ] 是否提供了reasoning说明？
- [ ] keywords是否准确？

---

## 调整和优化

### 如果新闻质量不佳
- 扩大抓取范围（增加新闻源）
- 放宽时间范围（48小时→72小时）
- 降低去重阈值（允许更多相似内容）

### 如果新闻过多
- 提高重要性筛选标准
- 增加去重严格程度
- 限制medium级别数量

### 如果某类新闻过多
- 保证类型多样性（技术/产品/政策/融资等均衡）
- 避免单一公司刷屏（同一公司最多2条）
