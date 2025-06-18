AGENTS.md
项目多智能体（AI Agents）分工说明
本项目包含以下四类智能Agent，分别覆盖亚马逊运营的主要AI场景，每个Agent可独立调用，也可组合联动，支持后续功能扩展与微服务架构升级。

1. CustomerServiceAgent
功能描述：
自动处理买家常见问题咨询（如订单查询、物流追踪、退换货政策、售后服务），支持多语言回复、智能FAQ、订单mock查询，集成情感分析自动分类用户情绪（好评/差评/抱怨等）。

核心能力：

FAQ智能回复（基于知识库+大模型）

订单/物流查询（mock或API接入）

情感分析，自动标注客服对话
多语言自动切换
调用示例：
agent = CustomerServiceAgent()
agent.reply(user_question)
agent.analyze_sentiment(user_message)
扩展方向：

实时对接Amazon SP-API/ERP

支持邮件/WhatsApp/微信等多渠道

2. ListingOptimizerAgent
功能描述：
针对输入的产品listing（标题、五点、描述、图片ALT等），自动生成优化建议和新文案，结合AI对listing内容打分，自动推荐关键词和标签，辅助A+页面内容策划。

核心能力：

自动生成/优化Title、Bullet Points、Description

关键词/标签智能推荐

图片ALT标签建议（基于图片识别）

文案质量评分与对比

调用示例：

agent = ListingOptimizerAgent()
agent.optimize_listing(listing_data)
agent.suggest_keywords(listing_data)
agent.score(listing_data)
扩展方向：

与第三方内容优化平台API互通

A/B测试文案迭代优化

3. ReviewAnalysisAgent
功能描述：
自动采集/接收产品评论、退货原因、客服对话内容，进行情感分析、分词、关键词提取，生成产品改进建议与负面热点预警，支持词云、趋势图等可视化输出。

核心能力：

评论、退货内容批量处理

情感分析+自动标签

高频关键词/痛点词提取

智能总结痛点/改进点

调用示例：

agent = ReviewAnalysisAgent()
agent.analyze_reviews(reviews)
agent.generate_wordcloud(reviews)
agent.summarize_trends(reviews)
扩展方向：

融合产品Q&A内容、视频review等多模态分析

自动推送负面舆情报警

4. CompetitorMonitorAgent
功能描述：
针对输入的竞品ASIN/链接，自动抓取其listing、review、价格、排名等信息，监控竞品关键指标变化，结合AI分析市场趋势、做销量/价格/关键词等多维度预测和报告。

核心能力：

竞品数据采集与变化监控

自动化趋势/价格/关键词预测

市场分析报告智能生成

可视化（价格/销量曲线、对比图等）

调用示例：

agent = CompetitorMonitorAgent()
agent.fetch_competitor_data(asin)
agent.analyze_trends(competitor_data)
agent.generate_report(competitor_data)
扩展方向：

与Keepa/SerpAPI等数据平台深度对接

AI驱动的市场预警和竞品策略优化

模块/Agent协作说明
每个Agent支持独立调用，也支持流水线串联（如竞品数据采集后，自动传递到ReviewAnalysisAgent做评论分析，再传到ListingOptimizerAgent给出listing优化建议）。

统一日志记录与状态追踪，便于异常排查和多Agent集成开发。

支持热插拔、微服务模式后续演化。

Agent能力对比表
Agent名称	核心输入	核心输出	典型应用
CustomerServiceAgent	用户问题、对话内容	智能回复、情感分类	智能客服、自动答疑
ListingOptimizerAgent	Listing结构化信息/图片	优化建议、文案、标签	Listing优化
ReviewAnalysisAgent	评论/退货/Q&A内容	情感分析、痛点、词云	用户洞察、改进建议
CompetitorMonitorAgent	竞品ASIN/链接	监控数据、趋势报告	市场分析、竞品监控



1. 整体技术架构说明
前端：

推荐用 Vue3（生态活跃，开源组件多，UI好看，文档友好，也容易对接各种后端API）。

前端负责：页面输入（ASIN或URL）、功能选区（四大模块）、数据可视化（折线图、词云、趋势图、摘要等）。

后端：

用 Python，Flask 或 FastAPI，API接口与前端交互。

后端负责：爬取Amazon商品数据、调用大模型分析、情感分析、数据整理和可视化API输出。

功能划分：

四大核心功能模块分别写好接口，前端用tab或按钮切换。

项目结构上建议每个功能独立service或agent（参见AGENTS.md）。

2. 第一个功能落地步骤（“商品信息智能采集”）
需求再细化：
输入：商品ASIN或亚马逊商品URL

后端API功能：

自动爬取该商品的全部Listing信息，包括：

标题

五点描述（bullet points）

产品主图与全部图片的 alt 属性（ALT文本）

A+页面内容（可选，优先主信息）

价格、品牌、类目（如需）

Review简要统计（如评分、条数、近10条内容）

返回数据：结构化JSON（便于AI分析和前端展示）

前端：结果可直接展示为表格、卡片或高亮区域

技术实现建议
A. 后端（Python部分）
推荐用 Flask 或 FastAPI，
爬虫推荐先用 requests + bs4（如果被风控再考虑selenium/playwright）

图片ALT字段一般在 #imgTagWrapperId img，多个图片ALT可以遍历 #altImages img 或相关图片列表。

错误处理（如遇到验证码，直接返回“需要手工采集”提示）


B. 前端（Vue部分）
输入框输入ASIN或URL，按钮触发API请求

展示结果：JSON表格、卡片、各字段高亮

四个功能Tab/菜单切换

C. 演示建议
现场输入一个竞品ASIN或URL，点击“采集”，3秒内返回全部listing结构化信息

展示“图片ALT”内容和原图，让听众看到“以前人工找alt，现在一键出”

后续可直接把这个结果传给AI，做listing优化、review分析等

3. 你要注意的“难点”
Amazon反爬机制，建议多做异常捕获，接口有“请求失败请重试/切换代理”提示

ALT有时候图片多、样式多，写代码要兼容多种DOM结构

多站点（.de/.com/.co.uk）url适配，建议asin和url都能解析


商品基本信息、图片ALT等核心字段采集+前端可视化展示，采集review、Q&A等更多内容，结果对接AI做内容优化、情感分析等

5. 后续升级
爬虫采集稳定后，可以考虑接Keepa/SerpAPI/API加快采集/规避风险

上生产建议配代理池、风控重试机制

做成微服务，每个功能一个API

