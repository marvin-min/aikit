# 邮件 AI 总结工具 - 产品方向

## 概述

使用 AI 自动总结 Outlook 邮件，帮助用户快速处理大量邮件，提升工作效率。

## 核心价值

### 解决的问题

1. **邮件过载**
   - 每天收到大量邮件
   - 重要邮件被淹没
   - 处理邮件占用大量时间

2. **效率问题**
   - 需要逐个打开邮件阅读
   - 长邮件难以快速抓住要点
   - 重复性邮件（日报、周报）浪费时间

3. **错失风险**
   - 忙碌时错过重要邮件
   - 没有统一的优先级视图
   - 容易忘记跟进

### 用户价值

- **5 分钟浏览 50+ 封邮件**
- **自动标记重要邮件**
- **智能分类和标签**
- **生成回复建议**

## 产品功能

### 核心功能

✅ **邮件获取**
   - 连接 Outlook 账户（OAuth）
   - 自动同步新邮件
   - 支持多个账户

✅ **AI 总结**
   - 总结邮件正文
   - 提取关键信息（时间、地点、人物、任务）
   - 生成简洁摘要

✅ **智能分类**
   - 自动分类（工作、个人、促销、通知）
   - 打标签（紧急、待办、阅读）
   - 识别邮件类型（会议邀请、任务分配、报告等）

✅ **优先级标记**
   - AI 判断邮件重要性
   - 高亮紧急和重要邮件
   - 智能排序（优先展示重要邮件）

✅ **回复建议**
   - 基于邮件内容生成回复草稿
   - 支持多语气（正式、随意）
   - 一键发送

### 增强功能（Phase 2）

- 邮件趋势分析
- 发件人活跃度分析
- 智能提醒（待办事项、跟进）
- 多语言总结
- 附件内容提取和总结

## 技术架构

### 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                  前端界面                              │
│         CLI / Web / Mobile / Outlook Add-in               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  API 网关                               │
│                  FastAPI                                │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌───────────┐ ┌───────────┐ ┌───────────┐
│ 邮件服务  │ │ AI 处理  │ │ 通知服务  │
│  Service  │ │  Service  │ │  Service  │
└─────┬─────┘ └─────┬─────┘ └─────┬─────┘
      │               │               │
      ▼               ▼               ▼
┌─────────────────────────────────────────────────────────┐
│                   数据存储                             │
│         SQLite / PostgreSQL / Redis                     │
└─────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│              Microsoft Graph API                          │
│              (Outlook 数据访问)                           │
└─────────────────────────────────────────────────────────┘
```

### 技术栈

**后端：**
- Python 3.10+
- FastAPI（API 服务）
- Microsoft Graph SDK（Outlook API）
- APScheduler（定时同步）

**前端：**
- Vue 3 / React（Web 界面）
- Outlook Add-in（Outlook 插件）

**AI 能力：**
- LangChain（RAG 框架）
- 通义千问 / 硅基流动（LLM）
- 邮件内容理解

### 数据模型

```python
# 用户账户
class Account:
    id: UUID
    user_id: UUID
    email: str
    provider: str  # outlook, gmail
    access_token: str
    refresh_token: str
    active: bool
    last_sync: datetime

# 邮件记录
class Email:
    id: UUID
    account_id: UUID
    outlook_id: str
    subject: str
    sender: str
    recipients: List[str]
    body: str
    summary: str
    category: str  # work, personal, promo, notification
    priority: int  # 1-5, AI 评分
    tags: List[str]
    is_read: bool
    is_important: bool
    received_at: datetime
    processed_at: datetime

# 回复建议
class ReplySuggestion:
    id: UUID
    email_id: UUID
    content: str
    tone: str  # formal, casual
    created_at: datetime
```

### 核心流程

```
1. 邮件同步
   ├─ 用户授权 OAuth
   ├─ 定时同步新邮件
   └─ 增量更新（避免重复）

2. AI 处理
   ├─ 提取邮件正文
   ├─ AI 总结
   ├─ 分类和打标
   ├─ 优先级评分
   └─ 生成回复建议

3. 用户展示
   ├─ 按优先级排序
   ├─ 按分类过滤
   ├─ 展示总结
   └─ 一键回复

4. 用户操作
   ├─ 标记已读/重要
   ├─ 发送回复
   ├─ 归档/删除
   └─ 修改分类
```

## Microsoft Graph API 集成

### OAuth 2.0 授权流程

```
1. 用户点击"连接 Outlook"
2. 重定向到 Microsoft 授权页面
3. 用户授权应用
4. 获取 access_token 和 refresh_token
5. 使用 access_token 调用 API
6. 定时刷新 token
```

### 主要 API 调用

```python
# 获取邮件
GET /me/mailMessages?$filter=isRead eq false&$orderby=receivedDateTime desc

# 获取邮件详情
GET /me/messages/{message_id}

# 发送回复
POST /me/messages/{message_id}/reply

# 标记已读
PATCH /me/messages/{message_id}
{
  "isRead": true
}

# 分类邮件
PATCH /me/messages/{message_id}
{
  "categories": ["important", "work"]
}
```

## 实现路线图

### Phase 1：MVP（1-2 周）

**目标：** 验证核心概念

- [ ] OAuth 授权（Outlook）
- [ ] 邮件获取和存储
- [ ] AI 总结单个邮件
- [ ] 命令行查看
- [ ] SQLite 数据存储

**交付物：**
- CLI 工具
- 支持手动和定时同步
- 基本的邮件总结

### Phase 2：自动化（1 周）

**目标：** 提升稳定性和智能化

- [ ] 定时同步（每 5 分钟）
- [ ] 批量邮件处理
- [ ] 智能分类
- [ ] 优先级评分
- [ ] 标签系统

**交付物：**
- 自动同步系统
- 智能分类和排序

### Phase 3：Web 界面（2-3 周）

**目标：** 提升用户体验

- [ ] FastAPI 后端
- [ ] 前端界面（Vue 3）
- [ ] 邮件列表视图
- [ ] 邮件详情视图
- [ ] 用户认证

**交付物：**
- 完整的 Web 应用
- 用户友好的界面

### Phase 4：Outlook 插件（2-3 周）

**目标：** 深度集成

- [ ] Outlook Add-in 开发
- [ ] 邮件列表内显示总结
- [ ] 一键生成回复
- [ ] 右键菜单集成

**交付物：**
- Outlook 插件
- 无缝集成体验

### Phase 5：增强功能（按需）

- [ ] 多账户支持
- [ ] 回复建议
- [ ] 邮件趋势分析
- [ ] 待办事项提取
- [ ] 移动端适配
- [ ] Gmail 支持

## MVP 设计

### 快速验证版本

**功能范围：**
1. OAuth 授权（Outlook）
2. 获取最近 10 封邮件
3. AI 总结
4. 命令行查看

**用户流程：**
```bash
# 授权连接
aikit-mail auth --provider outlook

# 同步邮件
aikit-mail sync

# 查看总结
aikit-mail summary --today

# 查看详情
aikit-mail show --id xxx
```

### 验证指标

- [ ] 能否成功授权和获取邮件
- [ ] 总结质量是否可接受
- [ ] 能否准确分类邮件
- [ ] 能否提升邮件处理效率

## 与订阅工具的整合

### 作为功能模块

可以将邮件总结作为**订阅工具的一个模块**：

```
订阅工具
├── RSS 订阅
├── 博客订阅
├── 新闻订阅
└── 邮件订阅 ← 新增
```

### 统一的数据模型

```python
# 统一的"信息源"概念
class SubscriptionSource:
    id: UUID
    type: SourceType  # rss, blog, news, email
    name: str
    config: dict  # 针对不同类型的配置

# 统一的"内容项"概念
class ContentItem:
    id: UUID
    source_id: UUID
    title: str
    summary: str
    category: str
    priority: int
    created_at: datetime
```

### 统一的用户界面

```
信息总览
├── RSS 更新
├── 博客文章
├── 新闻推送
└── 邮件更新
    └── AI 总结
    └── 智能分类
    └── 优先级标记
```

## 竞品分析

### 现有解决方案

1. **Outlook 内置功能**
   - 优点：无需第三方
   - 缺点：没有 AI 总结，分类有限

2. **Gmail Smart Reply**
   - 优点：回复建议
   - 缺点：仅限 Gmail，没有总结

3. **SaneBox / Superhuman**
   - 优点：智能分类
   - 缺点：付费，没有 AI 总结

### 差异化优势

- **开源**：完全可控，可私有部署
- **AI 总结**：真正的智能，不是规则引擎
- **优先级评分**：基于内容理解
- **多源统一**：邮件 + 订阅统一管理

## 风险和挑战

### 技术风险

1. **API 限制**
   - Microsoft Graph API 限流
   - 解决方案：合理请求频率，缓存机制

2. **隐私和安全**
   - 邮件内容敏感
   - 解决方案：加密存储，用户控制

3. **权限复杂**
   - OAuth 授权流程
   - Token 刷新
   - 解决方案：封装 SDK，完善文档

### 产品风险

1. **用户接受度**
   - 用户担心隐私
   - 解决方案：透明说明，可选部署

2. **准确度依赖**
   - 总结质量
   - 分类准确度
   - 解决方案：用户反馈，持续优化

## 隐私和安全

### 数据保护

1. **加密存储**
   - 邮件内容加密
   - Token 安全存储
   - 传输 HTTPS

2. **用户控制**
   - 随时删除数据
   - 随时撤销授权
   - 数据导出功能

3. **透明度**
   - 明确的数据使用政策
   - 开源代码审计
   - 可选私有部署

## 商业模式

### 免费版

- 单账户
- 每天 50 封邮件
- 基础总结
- 社区支持

### 专业版（付费）

- 多账户
- 无限邮件
- 高级 AI 功能
- 优先支持
- Outlook 插件

### 企业版

- 私有部署
- 自定义配置
- API 访问
- 专属支持

## 下一步行动

### 技术验证

1. **Microsoft Graph API 研究**
   - 注册应用
   - OAuth 测试
   - API 调用测试

2. **邮件总结测试**
   - 收集样本邮件
   - 测试总结质量
   - 测试分类准确度

3. **性能评估**
   - 批量处理能力
   - API 限流影响
   - 优化方案

### 产品验证

1. **用户调研**
   - 目标用户访谈
   - 痛点确认
   - 功能优先级

2. **MVP 开发**
   - 1-2 周 MVP
   - 内部测试
   - 小范围试用

3. **反馈迭代**
   - 收集用户反馈
   - 优化功能
   - 决定方向

---

**文档创建日期：** 2026-01-08
**版本：** v1.0
**状态：** 探讨中
