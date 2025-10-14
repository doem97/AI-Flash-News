#!/usr/bin/env python3
"""
AI 新闻简报自动生成脚本
使用 Claude API 抓取、分析和生成每日 AI 新闻简报（JSON格式）
"""

import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path


def get_historical_news_json(days=7):
    """
    读取最近N天的历史JSON新闻文件

    Args:
        days: 要回溯的天数

    Returns:
        包含历史新闻的列表
    """
    current_dir = Path(".")
    historical_data = []

    # 获取最近N天的日期
    for i in range(1, days + 1):
        date = datetime.now() - timedelta(days=i)
        filename = date.strftime("%Y-%m-%d.json")
        filepath = current_dir / filename

        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    historical_data.append({
                        "date": data.get("date", filename.replace(".json", "")),
                        "news": data.get("news", [])
                    })
            except json.JSONDecodeError:
                print(f"⚠️  警告: {filename} 格式错误，跳过")
                continue

    return historical_data


def format_historical_news(historical_data):
    """
    将历史新闻格式化为可读的字符串

    Args:
        historical_data: 历史新闻数据列表

    Returns:
        格式化后的字符串
    """
    if not historical_data:
        return "没有找到历史新闻文件。"

    formatted = []
    for day_data in historical_data:
        formatted.append(f"=== {day_data['date']} ===")
        for news_item in day_data['news']:
            content = news_item.get('content', '')
            keywords = ', '.join(news_item.get('keywords', []))
            formatted.append(f"- {content}")
            if keywords:
                formatted.append(f"  关键词: {keywords}")
        formatted.append("")

    return "\n".join(formatted)


def build_prompt(today_date_formatted, historical_news_text):
    """
    构建完整的Claude prompt

    Args:
        today_date_formatted: 今日日期（格式化后）
        historical_news_text: 历史新闻文本

    Returns:
        完整的prompt字符串
    """
    json_format_template = """{
  "date": "2025-10-14",
  "date_formatted": "25/10/14",
  "title": "早餐 AI 速读",
  "news": [
    {
      "id": 1,
      "title": "新闻标题（不超过15字）",
      "content": "新闻详细内容...",
      "importance": "critical",
      "reasoning": "判断理由...",
      "source": "来源网站",
      "url": "https://...",
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
}"""

    prompt = f"""你是一个资深的AI行业分析师，负责生成每日AI新闻简报。

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

## 第二步：去重检查
以下是最近7天已报道的新闻内容：

{historical_news_text}

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

### 每条新闻需要两个字段：

**1. title（标题）**
- **必须不超过15个字**
- 精炼概括核心要点
- 用冒号结尾（如："三星小模型颠覆认知："）
- 或用名词短语（如："AI模型中毒风险"）

**2. content（内容）**

### 字数分配
- **critical**: 50-80字
  - 包含：关键主体 + 核心内容 + 背景/原因 + 影响/意义

- **high**: 35-50字
  - 包含：关键主体 + 核心内容 + 简要影响

- **medium**: 20-35字
  - 包含：关键主体 + 核心事实

### 写作原则
1. **标题简洁**：title 字段不超过15字，高度提炼
2. **content 独立完整（重要！）**：content 必须 self-contained，不能依赖 title，必须包含完整主语和上下文，单独阅读也能完全理解
3. **中英文混排规范（重要！）**：中文和英文/数字交接处必须有空格，如"一个 AI 模型"、"OpenAI 发布"、"Meta 推出"
4. **信息密度优先**：content 不为凑字数加废话
5. **核心要素完整**："谁/什么/为什么/影响"
6. **客观中立**：避免过度夸张
7. **专业术语适度**：既要准确，也要易懂
8. **中文流畅**：避免翻译腔

## 第五步：输出JSON

按照以下格式输出（确保是有效的JSON）：

{json_format_template}

## 重要提醒
1. 必须输出有效的JSON格式
2. 所有新闻按importance排序（critical在前，medium在后）
3. 每条新闻都要提供reasoning，说明为什么判断为该级别
4. 尽可能提供原文URL
5. keywords要准确，用于去重和标签

请开始执行任务。你可以使用可用的工具（如WebFetch）来获取网页内容。最后请只输出纯JSON数据，不要包含其他说明文字。"""

    return prompt


def generate_ai_news_brief(args):
    """
    生成今日AI新闻简报

    Args:
        args: 命令行参数

    Returns:
        生成的新闻简报JSON数据
    """
    try:
        import anthropic
    except ImportError:
        print("❌ 错误: 未安装 anthropic 库")
        print("请运行: pip install anthropic")
        return None

    # 检查API Key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量")
        print("请运行: export ANTHROPIC_API_KEY='your-api-key'")
        return None

    # 初始化 Claude 客户端
    client = anthropic.Anthropic(api_key=api_key)

    # 获取日期
    if args.date:
        try:
            target_date = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            print("❌ 错误: 日期格式错误，请使用 YYYY-MM-DD")
            return None
    else:
        target_date = datetime.now()

    today = target_date.strftime("%Y-%m-%d")
    today_formatted = target_date.strftime("%y/%m/%d")

    # 获取历史新闻
    print(f"📅 生成日期: {today_formatted}")
    print("📚 读取历史新闻...")
    historical_data = get_historical_news_json(days=7)
    historical_text = format_historical_news(historical_data)
    print(f"✓ 已读取最近 {len(historical_data)} 天的历史记录")

    # 构建 prompt
    prompt = build_prompt(today_formatted, historical_text)

    # 调用 Claude API
    print("🤖 正在调用 Claude API 生成新闻简报...")
    print("⏳ 这可能需要1-2分钟，请耐心等待...")
    print("-" * 60)

    start_time = datetime.now()

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        generation_time = (datetime.now() - start_time).total_seconds()

        # 提取生成的内容
        response_text = message.content[0].text

        # 尝试提取JSON（可能包含在markdown代码块中）
        json_text = response_text
        if "```json" in response_text:
            json_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_text = response_text.split("```")[1].split("```")[0].strip()

        # 解析JSON
        news_data = json.loads(json_text)

        # 更新metadata中的生成时间
        if "metadata" in news_data:
            news_data["metadata"]["generation_time_seconds"] = round(generation_time, 2)

        print(f"✓ 生成完成！耗时 {generation_time:.1f} 秒")
        print("-" * 60)

        # 显示摘要
        total_news = news_data.get("metadata", {}).get("total_news", len(news_data.get("news", [])))
        sources = news_data.get("metadata", {}).get("sources_checked", [])
        duplicates = news_data.get("metadata", {}).get("duplicates_removed", 0)

        print(f"📊 新闻总数: {total_news}")
        print(f"🌐 数据源: {len(sources)} 个")
        print(f"🗑️  去重: {duplicates} 条")

        # 按重要性统计
        news_list = news_data.get("news", [])
        critical_count = sum(1 for n in news_list if n.get("importance") == "critical")
        high_count = sum(1 for n in news_list if n.get("importance") == "high")
        medium_count = sum(1 for n in news_list if n.get("importance") == "medium")

        print(f"🔥 重要程度: Critical({critical_count}) | High({high_count}) | Medium({medium_count})")
        print("-" * 60)

        return news_data, today

    except anthropic.APIError as e:
        print(f"❌ API 错误: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析错误: {e}")
        print("响应内容:")
        print(response_text[:500])
        return None
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return None


def save_news_data(news_data, today, args):
    """
    保存新闻数据到JSON和TXT文件

    Args:
        news_data: 新闻JSON数据
        today: 日期字符串
        args: 命令行参数
    """
    # 保存 JSON 文件
    json_file = f"{today}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)
    print(f"✓ JSON 已保存: {json_file}")

    # 同时保存为 TXT 格式（用于快速查看）
    txt_file = f"{today}.txt"
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(f"{news_data['title']} - {news_data['date_formatted']}\n")
        f.write("=" * 60 + "\n\n")

        for news_item in news_data.get('news', []):
            importance_icon = {
                'critical': '🔥',
                'high': '📌',
                'medium': '·'
            }.get(news_item.get('importance', 'medium'), '·')

            f.write(f"{importance_icon} {news_item['content']}\n")
            if news_item.get('url'):
                f.write(f"   {news_item['url']}\n")
            f.write("\n")

        f.write("-" * 60 + "\n")
        metadata = news_data.get('metadata', {})
        f.write(f"生成时间: {metadata.get('generated_at', '')}\n")
        f.write(f"新闻总数: {metadata.get('total_news', 0)}\n")
        f.write(f"数据源: {', '.join(metadata.get('sources_checked', []))}\n")

    print(f"✓ TXT 已保存: {txt_file}")

    # 提示用户使用开发服务器
    if not args.no_browser:
        print("\n" + "=" * 60)
        print("📱 现在可以通过开发服务器查看新闻:")
        print("   npm run dev")
        print("=" * 60)


def main():
    """
    主函数
    """
    parser = argparse.ArgumentParser(
        description='AI 新闻简报生成器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python generate_news.py                    # 生成今日简报
  python generate_news.py --date 2025-10-13  # 生成指定日期简报
  python generate_news.py --no-browser       # 生成但不打开浏览器
  python generate_news.py --count 15         # 自定义新闻数量
        """
    )

    parser.add_argument(
        '--date',
        type=str,
        help='指定日期 (YYYY-MM-DD)，默认为今天'
    )

    parser.add_argument(
        '--no-browser',
        action='store_true',
        help='不自动打开浏览器预览'
    )

    parser.add_argument(
        '--count',
        type=int,
        default=10,
        help='目标新闻数量 (默认: 10)'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("🌅 AI 新闻简报生成器")
    print("=" * 60)

    # 生成新闻简报
    result = generate_ai_news_brief(args)

    if result:
        news_data, today = result
        save_news_data(news_data, today, args)
        print("=" * 60)
        print("✅ 生成完成！")
        print("=" * 60)
    else:
        print("❌ 生成失败")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
