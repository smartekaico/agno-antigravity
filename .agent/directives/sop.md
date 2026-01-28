# Standard Operating Procedure (SOP)

## AI-Powered Lead Generation System using Agno Agentic Framework

---

## Document Control

| **Version** | **Date** | **Author**       | **Description**     |
| ----------- | -------- | ---------------- | ------------------- |
| 1.0         | 2025     | System Architect | Initial SOP Release |

---

## 1. Executive Summary

### 1.1 Purpose

This SOP outlines the complete plan for building a cost-effective, AI-powered lead generation system using the Agno Agentic Framework. The system automates lead discovery, enrichment, personalization, and email outreach while minimizing operational costs.

### 1.2 Scope

- Automated lead search and extraction
- Lead enrichment and personalization
- AI-generated icebreakers and email hooks
- Automated email outreach and follow-ups
- Centralized data management in Google Sheets

### 1.3 Cost-Effectiveness Principles

- Use free-tier services where possible
- Implement intelligent caching to reduce API calls
- Batch processing to optimize rate limits
- Local LLM options for non-critical tasks
- Smart deduplication to avoid redundant operations

---

## 2. System Architecture Overview

### 2.1 High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AGNO ORCHESTRATOR (Main Agent)                       │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Search    │  │ Enrichment  │  │  Content    │  │  Outreach   │        │
│  │   Agent     │  │   Agent     │  │   Agent     │  │   Agent     │        │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘        │
│         │                │                │                │               │
└─────────┼────────────────┼────────────────┼────────────────┼───────────────┘
          │                │                │                │
          ▼                ▼                ▼                ▼
   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
   │ Serper.dev  │  │  Crawl4AI   │  │  Local/API  │  │MailRelay.com│
   │    API      │  │   Scraper   │  │     LLM     │  │     API     │
   └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Google Sheets     │
                    │   (Central Data)    │
                    └─────────────────────┘
```

### 2.2 Agent Hierarchy

```
Orchestrator Agent (Coordinator)
├── Lead Search Agent
│   └── Tools: Serper Search, Email Extractor, Data Parser
├── Enrichment Agent
│   └── Tools: Crawl4AI Scraper, Content Analyzer, Social Finder
├── Content Generation Agent
│   └── Tools: Icebreaker Generator, Hook Creator, Email Composer
├── Outreach Agent
│   └── Tools: MailRelay Sender, Response Tracker, Follow-up Scheduler
└── Data Management Agent
    └── Tools: Sheets Reader, Sheets Writer, Deduplicator
```

---

## 3. Component Specifications

### 3.1 Agno Framework Configuration

#### 3.1.1 Agent Definitions

| **Agent Name**   | **Role**                                 | **Model Recommendation**                  | **Cost Tier** |
| ---------------- | ---------------------------------------- | ----------------------------------------- | ------------- |
| Orchestrator     | Coordinates all agents, manages workflow | GPT-4o-mini / Claude Haiku                | Low           |
| Search Agent     | Executes searches, extracts lead data    | GPT-4o-mini                               | Low           |
| Enrichment Agent | Scrapes websites, analyzes content       | GPT-4o-mini / Local Ollama                | Very Low      |
| Content Agent    | Generates personalized content           | GPT-4o / Claude Sonnet (quality critical) | Medium        |
| Outreach Agent   | Manages email campaigns                  | GPT-4o-mini                               | Low           |
| Data Agent       | Handles all Google Sheets operations     | Rule-based (no LLM needed)                | Free          |

#### 3.1.2 Agno Team Structure

```
Team Configuration:
├── Mode: Sequential with Conditional Branching
├── Memory: Shared Session Memory (SQLite for persistence)
├── Knowledge Base: Vector store for successful templates
└── Delegation: Enabled for specialized tasks
```

### 3.2 Tool Specifications

#### 3.2.1 Serper.dev Integration Tool

**Purpose:** Search for leads based on industry, position, and location

**Configuration:**

- API Key: Stored in environment variables
- Rate Limiting: 100 searches/day (free tier awareness)
- Caching: 24-hour cache for identical queries

**Input Parameters:**

```
- industry: string (e.g., "SaaS", "Healthcare")
- position: string (e.g., "CEO", "Marketing Director")
- location: string (e.g., "New York, USA")
- additional_keywords: list (optional)
- num_results: integer (default: 10)
```

**Output Schema:**

```
- search_results: list
  - name: string
  - job_title: string
  - company: string
  - website_url: string
  - linkedin_url: string (if found)
  - snippet: string (context from search)
```

#### 3.2.2 Email Extraction Tool

**Purpose:** Extract email addresses from search results and websites

**Methods:**

1. Pattern matching from search snippets
2. Common email format generation (firstname.lastname@domain.com)
3. Hunter.io free tier verification (optional)

**Cost Optimization:**

- Generate probable emails using patterns
- Verify only high-priority leads
- Cache verified emails permanently

#### 3.2.3 Crawl4AI Integration Tool

**Purpose:** Deep website scraping for enrichment data

**Configuration:**

```
- Headless Browser: Playwright (bundled)
- JavaScript Rendering: Enabled
- Timeout: 30 seconds
- Retry Logic: 3 attempts with exponential backoff
```

**Extraction Targets:**

```
Company Information:
├── About page content
├── Team/Leadership pages
├── Recent news/blog posts
├── Product/Service descriptions
├── Company values/mission
├── Recent achievements/awards
└── Technology stack (if visible)

Individual Information:
├── Bio/Profile text
├── Recent articles/posts
├── Speaking engagements
├── Published content
└── Social media links
```

#### 3.2.4 MailRelay.com Integration Tool

**Purpose:** Send and track outreach emails

**Configuration:**

```
- SMTP Settings: Via MailRelay API
- Daily Limit: Respect free tier limits (75,000/month = ~2,500/day)
- Sending Schedule: Distributed throughout business hours
- Tracking: Open rates, click rates, replies
```

**Features:**

```
- Template management
- Personalization tokens
- Unsubscribe handling
- Bounce management
- Reply detection
```

#### 3.2.5 Google Sheets Integration Tool

**Purpose:** Central data storage and management

**Sheets Structure:**

```
Workbook: "Lead_Generation_System"
├── Sheet 1: "Leads_Master"
├── Sheet 2: "Enrichment_Data"
├── Sheet 3: "Email_Templates"
├── Sheet 4: "Outreach_Tracking"
├── Sheet 5: "Follow_Up_Queue"
├── Sheet 6: "Responses"
├── Sheet 7: "Campaign_Analytics"
└── Sheet 8: "System_Config"
```

---

## 4. Data Schema Design

### 4.1 Leads_Master Sheet

| Column         | Type     | Description                                |
| -------------- | -------- | ------------------------------------------ |
| lead_id        | UUID     | Unique identifier                          |
| created_date   | DateTime | When lead was found                        |
| full_name      | String   | Lead's full name                           |
| first_name     | String   | First name (for personalization)           |
| job_title      | String   | Current position                           |
| company_name   | String   | Company name                               |
| industry       | String   | Industry classification                    |
| location       | String   | Geographic location                        |
| website_url    | String   | Company website                            |
| linkedin_url   | String   | LinkedIn profile URL                       |
| email_primary  | String   | Primary email address                      |
| email_verified | Boolean  | Verification status                        |
| lead_score     | Integer  | Quality score (1-100)                      |
| status         | Enum     | new/enriched/contacted/responded/converted |
| source_query   | String   | Original search query                      |

### 4.2 Enrichment_Data Sheet

| Column                 | Type     | Description                   |
| ---------------------- | -------- | ----------------------------- |
| lead_id                | UUID     | Reference to Leads_Master     |
| enrichment_date        | DateTime | When enrichment occurred      |
| company_description    | Text     | About the company             |
| company_size           | String   | Employee count range          |
| company_funding        | String   | Funding information           |
| recent_news            | Text     | Recent company news           |
| pain_points_identified | Text     | AI-identified pain points     |
| tech_stack             | Text     | Technologies used             |
| personal_bio           | Text     | Lead's biography              |
| recent_posts           | Text     | Recent social/blog content    |
| mutual_connections     | Text     | Any shared connections        |
| personalization_hooks  | Text     | Identified hooks for outreach |

### 4.3 Email_Templates Sheet

| Column                 | Type    | Description                                 |
| ---------------------- | ------- | ------------------------------------------- |
| template_id            | UUID    | Unique identifier                           |
| template_name          | String  | Template name                               |
| template_type          | Enum    | initial/follow_up_1/follow_up_2/follow_up_3 |
| subject_line           | String  | Email subject (with tokens)                 |
| body_content           | Text    | Email body (with tokens)                    |
| icebreaker_placeholder | Boolean | Requires AI icebreaker                      |
| performance_score      | Float   | Historical performance                      |

### 4.4 Outreach_Tracking Sheet

| Column               | Type     | Description               |
| -------------------- | -------- | ------------------------- |
| outreach_id          | UUID     | Unique identifier         |
| lead_id              | UUID     | Reference to lead         |
| campaign_name        | String   | Campaign identifier       |
| email_type           | Enum     | initial/follow_up_1/2/3   |
| sent_date            | DateTime | When email was sent       |
| subject_used         | String   | Actual subject line       |
| icebreaker_used      | Text     | AI-generated icebreaker   |
| opened               | Boolean  | Email opened              |
| open_date            | DateTime | When opened               |
| clicked              | Boolean  | Link clicked              |
| replied              | Boolean  | Reply received            |
| reply_date           | DateTime | When replied              |
| reply_sentiment      | Enum     | positive/neutral/negative |
| mailrelay_message_id | String   | MailRelay tracking ID     |

### 4.5 Follow_Up_Queue Sheet

| Column           | Type     | Description                 |
| ---------------- | -------- | --------------------------- |
| queue_id         | UUID     | Unique identifier           |
| lead_id          | UUID     | Reference to lead           |
| outreach_id      | UUID     | Previous outreach reference |
| follow_up_number | Integer  | 1, 2, or 3                  |
| scheduled_date   | DateTime | When to send                |
| status           | Enum     | pending/sent/cancelled      |
| priority         | Integer  | Processing priority         |

### 4.6 Responses Sheet

| Column            | Type     | Description                                         |
| ----------------- | -------- | --------------------------------------------------- |
| response_id       | UUID     | Unique identifier                                   |
| lead_id           | UUID     | Reference to lead                                   |
| outreach_id       | UUID     | Which email was replied to                          |
| received_date     | DateTime | When response received                              |
| response_content  | Text     | Full response text                                  |
| ai_classification | Enum     | interested/not_interested/more_info/meeting_request |
| suggested_action  | Text     | AI-suggested next step                              |
| handled           | Boolean  | Response has been handled                           |

---

## 5. Workflow Procedures

### 5.1 Lead Search Workflow

```
PROCEDURE: Lead Discovery
TRIGGER: Manual initiation or scheduled (daily/weekly)
RESPONSIBLE: Search Agent

STEPS:
1. INPUT COLLECTION
   ├── Read search parameters from System_Config sheet
   ├── Parameters: industry, positions[], locations[]
   └── Validate inputs are complete

2. SEARCH EXECUTION
   ├── For each combination of (industry, position, location):
   │   ├── Check cache for recent identical search
   │   ├── If cache hit → use cached results
   │   ├── If cache miss → execute Serper.dev search
   │   │   └── Query format: "{position} {industry} {location} email contact"
   │   └── Parse search results
   │
   └── Rate limiting: Max 10 searches per minute

3. DATA EXTRACTION
   ├── For each search result:
   │   ├── Extract name using NLP/pattern matching
   │   ├── Extract job title
   │   ├── Extract company name
   │   ├── Extract website URL
   │   ├── Extract/generate email addresses
   │   └── Extract LinkedIn URL if present
   │
   └── Validate extracted data completeness

4. DEDUPLICATION
   ├── Check against existing Leads_Master
   ├── Match on: email OR (name + company)
   ├── Skip duplicates
   └── Log duplicate count

5. DATA STORAGE
   ├── Assign unique lead_id
   ├── Calculate initial lead_score
   ├── Set status = "new"
   ├── Write to Leads_Master sheet
   └── Return count of new leads added

OUTPUT: List of new lead_ids for enrichment
```

### 5.2 Enrichment Workflow

```
PROCEDURE: Lead Enrichment
TRIGGER: New leads added OR scheduled batch
RESPONSIBLE: Enrichment Agent

STEPS:
1. QUEUE PREPARATION
   ├── Query Leads_Master for status = "new"
   ├── Prioritize by lead_score (highest first)
   ├── Batch size: 50 leads per run
   └── Skip leads enriched within last 30 days

2. WEBSITE SCRAPING (Crawl4AI)
   ├── For each lead with website_url:
   │   ├── Initialize Crawl4AI session
   │   ├── Scrape target pages:
   │   │   ├── Homepage
   │   │   ├── About page (/about, /about-us, /company)
   │   │   ├── Team page (/team, /leadership, /people)
   │   │   ├── Blog/News (latest 3 posts)
   │   │   └── Products/Services page
   │   │
   │   ├── Error handling:
   │   │   ├── Timeout → retry once, then skip
   │   │   ├── 404 → mark URL invalid
   │   │   └── Blocked → use alternative approach
   │   │
   │   └── Rate limiting: 2-second delay between sites
   │
   └── Store raw scraped content

3. CONTENT ANALYSIS (LLM Processing)
   ├── Feed scraped content to LLM with prompt:
   │   └── "Analyze this company information and extract:
   │        - Company description (2-3 sentences)
   │        - Company size estimate
   │        - Main products/services
   │        - Recent news or achievements
   │        - Potential pain points for [our solution]
   │        - Technology stack if mentioned
   │        - Key differentiators"
   │
   ├── Cost optimization:
   │   ├── Use GPT-4o-mini for extraction
   │   ├── Batch multiple companies per request
   │   └── Cache analysis results
   │
   └── Parse structured output

4. PERSONALIZATION HOOK IDENTIFICATION
   ├── LLM prompt:
   │   └── "Based on this company and person information,
   │        identify 3 personalization hooks:
   │        - Recent achievement to congratulate
   │        - Challenge they might be facing
   │        - Mutual interest or connection point"
   │
   └── Store hooks for email generation

5. DATA STORAGE
   ├── Write to Enrichment_Data sheet
   ├── Update lead_score based on data quality
   ├── Update Leads_Master status = "enriched"
   └── Log enrichment completion

OUTPUT: Enriched lead_ids ready for content generation
```

### 5.3 Content Generation Workflow

```
PROCEDURE: Icebreaker and Email Generation
TRIGGER: Enriched leads queue OR campaign initiation
RESPONSIBLE: Content Agent

STEPS:
1. TEMPLATE SELECTION
   ├── Load templates from Email_Templates sheet
   ├── Select based on:
   │   ├── Lead industry
   │   ├── Lead position level
   │   └── Template performance_score
   │
   └── A/B test: rotate between top 2 templates

2. ICEBREAKER GENERATION
   ├── Retrieve enrichment data for lead
   ├── LLM prompt for icebreaker:
   │   └── "Create a personalized icebreaker for an email to
   │        {first_name}, {job_title} at {company_name}.
   │
   │        Use one of these hooks:
   │        {personalization_hooks}
   │
   │        Requirements:
   │        - Maximum 2 sentences
   │        - Natural, not salesy
   │        - Reference specific details
   │        - Lead into our value proposition"
   │
   ├── Generate 2 variations for testing
   └── Store in Outreach_Tracking

3. SUBJECT LINE GENERATION
   ├── LLM prompt:
   │   └── "Create 2 subject line variations for this cold email.
   │        Context: {company_info}
   │        Goal: {campaign_goal}
   │
   │        Requirements:
   │        - Under 50 characters
   │        - Personalized if possible
   │        - Create curiosity without clickbait
   │        - No spam trigger words"
   │
   └── Select based on historical performance patterns

4. FULL EMAIL COMPOSITION
   ├── Combine elements:
   │   ├── Subject line
   │   ├── Personalized icebreaker
   │   ├── Value proposition (from template)
   │   ├── Call to action
   │   └── Signature
   │
   ├── Token replacement:
   │   ├── {{first_name}} → actual first name
   │   ├── {{company}} → company name
   │   ├── {{icebreaker}} → generated icebreaker
   │   └── {{custom_hook}} → specific personalization
   │
   └── Final review prompt (quality check)

5. STORAGE
   ├── Store composed email in Outreach_Tracking
   ├── Mark as ready_to_send
   └── Add to sending queue

OUTPUT: Ready-to-send personalized emails
```

### 5.4 Outreach Workflow

```
PROCEDURE: Email Sending and Tracking
TRIGGER: Scheduled sending windows OR manual trigger
RESPONSIBLE: Outreach Agent

STEPS:
1. SENDING PREPARATION
   ├── Query Outreach_Tracking for ready_to_send emails
   ├── Check MailRelay daily limit remaining
   ├── Calculate batch size (spread throughout day)
   └── Sending windows: 9AM-11AM, 2PM-4PM local time

2. PRE-SEND CHECKS
   ├── For each email in batch:
   │   ├── Verify lead not unsubscribed
   │   ├── Verify email not previously bounced
   │   ├── Verify not in cooldown period
   │   └── Validate email format
   │
   └── Remove invalid from queue

3. EMAIL SENDING (MailRelay)
   ├── For each validated email:
   │   ├── Prepare MailRelay API request:
   │   │   ├── from: configured sender
   │   │   ├── to: lead email
   │   │   ├── subject: personalized subject
   │   │   ├── html_body: formatted email
   │   │   └── tracking: enabled
   │   │
   │   ├── Send via API
   │   ├── Capture message_id
   │   ├── Update Outreach_Tracking:
   │   │   ├── sent_date = now
   │   │   ├── mailrelay_message_id = response.id
   │   │   └── status = "sent"
   │   │
   │   └── Delay: 5-10 seconds between sends
   │
   └── Handle errors (retry queue for failures)

4. SCHEDULE FOLLOW-UPS
   ├── For each sent email:
   │   ├── Create Follow_Up_Queue entries:
   │   │   ├── follow_up_1: +3 business days
   │   │   ├── follow_up_2: +7 business days
   │   │   └── follow_up_3: +14 business days
   │   │
   │   └── Set status = "pending"
   │
   └── Skip if lead has existing pending follow-ups

5. TRACKING UPDATE (runs hourly)
   ├── Query MailRelay for engagement data
   ├── Update Outreach_Tracking:
   │   ├── opened → true + open_date
   │   ├── clicked → true
   │   └── bounced → mark lead as invalid
   │
   └── Cancel follow-ups for bounced emails

OUTPUT: Sent email count, error count, scheduled follow-ups
```

### 5.5 Follow-Up Workflow

```
PROCEDURE: Automated Follow-Up Management
TRIGGER: Daily at 8AM OR response received
RESPONSIBLE: Outreach Agent + Content Agent

STEPS:
1. FOLLOW-UP QUEUE PROCESSING
   ├── Query Follow_Up_Queue where:
   │   ├── scheduled_date <= today
   │   └── status = "pending"
   │
   └── Sort by priority, then scheduled_date

2. RESPONSE CHECK
   ├── For each pending follow-up:
   │   ├── Check if lead has replied (Responses sheet)
   │   ├── If replied:
   │   │   ├── Cancel this and future follow-ups
   │   │   └── Continue to next lead
   │   │
   │   ├── Check if opened previous emails:
   │   │   ├── If yes → continue with follow-up
   │   │   └── If no → delay by 2 days (maybe spam folder)
   │   │
   │   └── Proceed to generation

3. FOLLOW-UP CONTENT GENERATION
   ├── Retrieve previous outreach context
   ├── Select follow-up template based on:
   │   ├── follow_up_number (1, 2, or 3)
   │   └── Previous email engagement
   │
   ├── Follow-up 1 strategy: "Checking in"
   │   └── Short, add new value point
   │
   ├── Follow-up 2 strategy: "Different angle"
   │   └── New hook, case study reference
   │
   └── Follow-up 3 strategy: "Breakup email"
       └── Last attempt, create urgency

4. FOLLOW-UP SENDING
   ├── Use same Outreach Workflow (5.4)
   ├── Thread with original email if possible
   └── Update Follow_Up_Queue status = "sent"

5. NO-RESPONSE HANDLING
   ├── After follow_up_3 with no response:
   │   ├── Mark lead status = "nurture"
   │   ├── Schedule re-engagement in 90 days
   │   └── Remove from active campaign
   │
   └── Log in Campaign_Analytics

OUTPUT: Follow-ups sent, leads moved to nurture
```

### 5.6 Response Handling Workflow

```
PROCEDURE: Response Detection and Classification
TRIGGER: Webhook from MailRelay OR polling every 15 minutes
RESPONSIBLE: Orchestrator Agent

STEPS:
1. RESPONSE DETECTION
   ├── Check configured inbox for replies
   ├── Match reply to original outreach:
   │   ├── By thread/message-id
   │   └── By email address match
   │
   └── Import response content

2. AI CLASSIFICATION
   ├── LLM prompt:
   │   └── "Classify this email response:
   │
   │        Response: {response_content}
   │
   │        Categories:
   │        - INTERESTED: Wants to learn more or meet
   │        - MEETING_REQUEST: Explicitly asks for meeting
   │        - MORE_INFO: Requests additional information
   │        - NOT_NOW: Interested but timing is wrong
   │        - NOT_INTERESTED: Clear rejection
   │        - OUT_OF_OFFICE: Auto-reply
   │        - UNSUBSCRIBE: Wants to be removed
   │
   │        Also provide:
   │        - Sentiment (positive/neutral/negative)
   │        - Suggested next action
   │        - Key points from their response"
   │
   └── Parse classification

3. AUTOMATIC ACTIONS
   ├── Based on classification:
   │   ├── INTERESTED/MEETING_REQUEST:
   │   │   ├── Cancel all follow-ups
   │   │   ├── Update lead status = "hot"
   │   │   ├── Alert human operator
   │   │   └── Suggest meeting times response
   │   │
   │   ├── MORE_INFO:
   │   │   ├── Cancel automated follow-ups
   │   │   ├── Generate info-sharing response
   │   │   └── Queue for human review
   │   │
   │   ├── NOT_NOW:
   │   │   ├── Cancel current follow-ups
   │   │   ├── Schedule re-engagement (30/60/90 days)
   │   │   └── Mark lead status = "nurture"
   │   │
   │   ├── NOT_INTERESTED:
   │   │   ├── Cancel all follow-ups
   │   │   ├── Mark lead status = "closed_lost"
   │   │   └── Do not contact again
   │   │
   │   ├── OUT_OF_OFFICE:
   │   │   ├── Extract return date if present
   │   │   ├── Reschedule follow-up after return
   │   │   └── Continue sequence
   │   │
   │   └── UNSUBSCRIBE:
   │       ├── Cancel all follow-ups
   │       ├── Add to suppression list
   │       └── Mark lead status = "unsubscribed"

4. STORAGE
   ├── Write to Responses sheet
   ├── Update Leads_Master status
   ├── Log in Campaign_Analytics
   └── Notify relevant parties

OUTPUT: Classified responses, updated lead statuses, notifications
```

---

## 6. Cost Optimization Strategies

### 6.1 API Cost Management

```
STRATEGY: Tiered LLM Usage

HIGH-COST (GPT-4o/Claude Sonnet) - Use sparingly:
├── Final email composition for high-value leads
├── Complex response classification
└── Icebreaker generation for Tier 1 leads

MEDIUM-COST (GPT-4o-mini/Claude Haiku) - Default choice:
├── Data extraction and parsing
├── Standard icebreaker generation
├── Email template filling
└── Basic classification tasks

LOW/NO COST (Local Ollama/Rules):
├── Email validation
├── Deduplication checks
├── Simple data transformations
└── Scheduling logic
```

### 6.2 Serper.dev Optimization

```
Free Tier: 2,500 searches/month

OPTIMIZATION TACTICS:
1. Cache Management
   ├── Cache all search results for 7 days
   ├── Use fuzzy matching for similar queries
   └── Estimated savings: 40% reduction in searches

2. Query Optimization
   ├── Combine related searches into single query
   ├── Use site-specific searches efficiently
   └── Estimated savings: 20% reduction

3. Smart Batching
   ├── Batch related searches together
   ├── Process during off-peak hours
   └── Prioritize high-value searches

MONTHLY BUDGET:
├── Week 1-2: New lead discovery (1,500 searches)
├── Week 3: Verification searches (500 searches)
└── Week 4: Buffer for ad-hoc (500 searches)
```

### 6.3 Crawl4AI Optimization

```
COST: Free (self-hosted), but compute/time costs

OPTIMIZATION TACTICS:
1. Selective Scraping
   ├── Only scrape pages likely to have useful info
   ├── Skip if company info already cached
   └── Limit to 5 pages per website

2. Parallel Processing
   ├── Run 3 concurrent scrapers
   ├── Queue management for efficiency
   └── Respect robots.txt

3. Content Caching
   ├── Cache scraped content for 30 days
   ├── Only re-scrape on significant date events
   └── Store in compressed format
```

### 6.4 MailRelay Optimization

```
Free Tier: 75,000 emails/month

OPTIMIZATION TACTICS:
1. Lead Quality Focus
   ├── Only email leads with score > 50
   ├── Verify emails before sending
   └── Reduces bounces and wasted sends

2. Smart Follow-up Cancellation
   ├── Cancel follow-ups on any engagement
   ├── Combine follow-ups for non-openers
   └── Estimated savings: 30% of follow-up emails

3. Template Performance Tracking
   ├── Drop templates with < 10% open rate
   ├── Optimize subject lines continuously
   └── Higher engagement = fewer sends needed
```

### 6.5 Google Sheets Optimization

```
Free Tier: Standard Google account limits

OPTIMIZATION TACTICS:
1. Batch Operations
   ├── Batch reads/writes (max 100 rows per call)
   ├── Reduce API calls by 90%
   └── Use Sheets API v4 batch endpoints

2. Data Architecture
   ├── Archive old data to separate sheets
   ├── Keep active data < 10,000 rows per sheet
   └── Use data validation to prevent errors

3. Read Optimization
   ├── Cache frequently accessed data locally
   ├── Use named ranges for common queries
   └── Implement change detection
```

---

## 7. Implementation Phases

### Phase 1: Foundation (Week 1-2)

```
DELIVERABLES:
□ Google Sheets structure created
□ All sheet schemas implemented
□ Service accounts configured
□ API keys secured in environment
□ Basic Agno agent skeleton created
□ Development environment setup

TASKS:
1. Create Google Sheets workbook
2. Set up all 8 sheets with headers
3. Create Google Service Account
4. Share sheets with service account
5. Set up Serper.dev account
6. Set up MailRelay account
7. Configure Crawl4AI locally
8. Initialize Agno project structure
9. Create configuration files
10. Test all API connections

VALIDATION:
├── Can read/write to all sheets
├── Serper.dev returns results
├── MailRelay test email succeeds
└── Crawl4AI scrapes test page
```

### Phase 2: Core Agents (Week 3-4)

```
DELIVERABLES:
□ Search Agent functional
□ Data Management Agent functional
□ Basic enrichment working
□ End-to-end data flow tested

TASKS:
1. Implement Search Agent
   ├── Serper.dev tool integration
   ├── Email extraction logic
   └── Deduplication checks

2. Implement Data Management Agent
   ├── Google Sheets read/write tools
   ├── Batch operation support
   └── Error handling

3. Create Orchestrator skeleton
   ├── Agent coordination logic
   └── Workflow state management

4. Test data pipeline
   ├── Search → Extract → Store
   └── Verify data integrity

VALIDATION:
├── Search returns structured leads
├── Leads stored correctly in sheets
├── Duplicates detected and skipped
└── Error handling works
```

### Phase 3: Enrichment & Content (Week 5-6)

```
DELIVERABLES:
□ Enrichment Agent functional
□ Content Generation Agent functional
□ Personalized emails generated
□ Quality meets standards

TASKS:
1. Implement Enrichment Agent
   ├── Crawl4AI integration
   ├── Content extraction prompts
   └── Hook identification

2. Implement Content Agent
   ├── Icebreaker generation
   ├── Subject line creation
   └── Full email composition

3. Create email templates
   ├── Initial outreach (3 variants)
   ├── Follow-up 1 (2 variants)
   ├── Follow-up 2 (2 variants)
   └── Follow-up 3/breakup (1 variant)

4. Quality testing
   ├── Review 50 generated emails
   ├── Tune prompts for quality
   └── A/B test framework setup

VALIDATION:
├── Enrichment extracts useful data
├── Icebreakers are personalized
├── Emails pass spam check
└── Content is professional quality
```

### Phase 4: Outreach & Automation (Week 7-8)

```
DELIVERABLES:
□ Outreach Agent functional
□ Email sending automated
□ Follow-up scheduling works
□ Tracking operational

TASKS:
1. Implement Outreach Agent
   ├── MailRelay API integration
   ├── Sending queue management
   └── Rate limiting

2. Implement follow-up system
   ├── Queue management
   ├── Conditional cancellation
   └── Scheduling logic

3. Implement tracking
   ├── Open/click tracking
   ├── Reply detection
   └── Analytics collection

4. Create scheduling system
   ├── Cron job setup
   ├── Sending window management
   └── Timezone handling

VALIDATION:
├── Emails send successfully
├── Tracking data updates
├── Follow-ups trigger correctly
└── System respects rate limits
```

### Phase 5: Response Handling & Optimization (Week 9-10)

```
DELIVERABLES:
□ Response classification working
□ Automated actions functional
□ Performance dashboard created
□ Full system operational

TASKS:
1. Implement response handling
   ├── Reply detection
   ├── AI classification
   └── Automatic actions

2. Create notification system
   ├── Hot lead alerts
   ├── Daily summary reports
   └── Error notifications

3. Build analytics dashboard
   ├── Campaign performance
   ├── Agent performance
   └── Cost tracking

4. Optimization tuning
   ├── Prompt optimization
   ├── Template performance
   └── Timing optimization

VALIDATION:
├── Responses classified correctly
├── Actions trigger appropriately
├── Dashboard shows accurate data
└── System runs unattended
```

### Phase 6: Testing & Launch (Week 11-12)

```
DELIVERABLES:
□ Full system tested
□ Documentation complete
□ Team trained
□ Production launch

TASKS:
1. End-to-end testing
   ├── 100 lead journey test
   ├── Edge case testing
   └── Load testing

2. Documentation
   ├── User guide
   ├── Troubleshooting guide
   └── API documentation

3. Training
   ├── Team walkthrough
   ├── Override procedures
   └── Escalation paths

4. Production launch
   ├── Gradual rollout (25%→50%→100%)
   ├── Monitoring setup
   └── Rollback plan ready

VALIDATION:
├── All workflows complete successfully
├── Team can operate system
├── Monitoring alerts working
└── Performance meets SLAs
```

---

## 8. Monitoring & Maintenance

### 8.1 Daily Monitoring Checklist

```
AUTOMATED CHECKS (run every 4 hours):
□ API connectivity (Serper, MailRelay, Google Sheets)
□ Agent health status
□ Queue depths (normal ranges defined)
□ Error rate < 5%
□ Email deliverability > 95%

DAILY HUMAN REVIEW:
□ Review hot lead alerts
□ Check response classifications for accuracy
□ Monitor campaign performance trends
□ Verify no unusual patterns
□ Approve any held emails
```

### 8.2 Weekly Maintenance

```
WEEK START:
□ Review previous week's analytics
□ Identify underperforming templates
□ Check API usage vs budget
□ Update A/B test variants

MID-WEEK:
□ Clean up bounced emails
□ Archive completed campaigns
□ Verify follow-up queue health
□ Check enrichment data quality

WEEK END:
□ Generate weekly report
□ Plan next week's campaigns
□ Update lead scoring rules
□ Backup Google Sheets data
```

### 8.3 Monthly Optimization

```
PERFORMANCE REVIEW:
□ Analyze template performance (retire <10% open rate)
□ Review icebreaker effectiveness
□ Assess lead quality by source
□ Calculate true cost per lead

SYSTEM OPTIMIZATION:
□ Tune LLM prompts based on results
□ Update enrichment targets
□ Refine lead scoring algorithm
□ Adjust sending schedules

COST REVIEW:
□ API usage vs budget
□ Identify waste areas
□ Plan optimizations
□ Forecast next month
```

---

## 9. Risk Mitigation

### 9.1 Technical Risks

| Risk                       | Probability | Impact | Mitigation                                                              |
| -------------------------- | ----------- | ------ | ----------------------------------------------------------------------- |
| API rate limit exceeded    | Medium      | High   | Implement circuit breakers, caching, queue management                   |
| Email deliverability drops | Medium      | High   | Monitor sender reputation, warm up gradually, use proper authentication |
| Scraping blocked           | Medium      | Medium | Rotate user agents, respect robots.txt, use delays                      |
| LLM output quality issues  | Low         | Medium | Implement output validation, human review for critical emails           |
| Google Sheets limits hit   | Low         | Medium | Implement archiving, use batch operations, monitor row counts           |

### 9.2 Operational Risks

| Risk                              | Probability | Impact   | Mitigation                                                        |
| --------------------------------- | ----------- | -------- | ----------------------------------------------------------------- |
| Spam complaints                   | Medium      | Critical | Quality over quantity, proper unsubscribe, monitor feedback loops |
| Data privacy issues               | Low         | Critical | Compliance review, data handling procedures, suppression lists    |
| Cost overrun                      | Medium      | Medium   | Usage monitoring, hard limits, alerts at 80% budget               |
| Agent errors causing bad outreach | Low         | High     | Human review for new templates, gradual rollout                   |

### 9.3 Compliance Considerations

```
EMAIL COMPLIANCE:
□ Include physical address in emails
□ Working unsubscribe mechanism
□ Honor unsubscribe within 48 hours
□ Don't use misleading subject lines
□ Identify promotional content appropriately

DATA COMPLIANCE:
□ Only collect publicly available data
□ Respect opt-out requests
□ Secure storage of lead data
□ Regular data cleanup
□ Document data sources
```

---

## 10. Success Metrics

### 10.1 Key Performance Indicators (KPIs)

```
LEAD GENERATION:
├── New leads per day: Target 50+
├── Lead quality score average: Target >60
├── Cost per lead: Target <$0.10
└── Enrichment completion rate: Target >90%

EMAIL PERFORMANCE:
├── Open rate: Target >40%
├── Reply rate: Target >5%
├── Positive reply rate: Target >2%
├── Bounce rate: Target <3%
└── Unsubscribe rate: Target <1%

SYSTEM PERFORMANCE:
├── Uptime: Target >99%
├── Processing time per lead: Target <5 minutes
├── API error rate: Target <2%
└── Cost per month: Target <$100
```

### 10.2 Reporting Dashboard Structure

```
DAILY DASHBOARD:
├── Leads added today
├── Emails sent today
├── Opens/clicks/replies today
├── Hot leads requiring action
└── System health status

WEEKLY DASHBOARD:
├── Week-over-week trends
├── Top performing templates
├── Campaign comparison
├── Cost breakdown
└── Pipeline progression

MONTHLY DASHBOARD:
├── Funnel analysis
├── ROI calculation
├── A/B test results
├── Optimization recommendations
└── Next month planning
```

---

## 11. Appendices

### Appendix A: Environment Variables

```
# LLM Configuration
OPENAI_API_KEY=sk-xxx
ANTHROPIC_API_KEY=sk-ant-xxx

# Search
SERPER_API_KEY=xxx

# Email
MAILRELAY_API_KEY=xxx
MAILRELAY_SENDER_EMAIL=outreach@yourdomain.com
MAILRELAY_SENDER_NAME=Your Name

# Google Sheets
GOOGLE_SERVICE_ACCOUNT_JSON=path/to/service-account.json
GOOGLE_SHEETS_ID=xxx

# System
LOG_LEVEL=INFO
ENVIRONMENT=production
CACHE_DIRECTORY=./cache
```

### Appendix B: Prompt Templates

```
ICEBREAKER_PROMPT:
"""
Create a personalized icebreaker for a cold email.

RECIPIENT:
- Name: {first_name} {last_name}
- Title: {job_title}
- Company: {company_name}

CONTEXT:
{enrichment_summary}

PERSONALIZATION HOOKS:
{hooks}

REQUIREMENTS:
1. Maximum 2 sentences
2. Reference something specific about them or their company
3. Natural, conversational tone
4. No generic compliments
5. Should flow naturally into our value proposition

OUTPUT FORMAT:
Just the icebreaker text, no explanation.
"""

EMAIL_COMPOSITION_PROMPT:
"""
Compose a cold outreach email.

TEMPLATE:
{template}

RECIPIENT:
{lead_info}

ICEBREAKER:
{icebreaker}

REQUIREMENTS:
1. Professional but friendly tone
2. Under 150 words
3. One clear call to action
4. No attachments mentioned
5. No excessive formatting

OUTPUT FORMAT:
Return JSON with: subject, body
"""

RESPONSE_CLASSIFICATION_PROMPT:
"""
Classify this email response.

ORIGINAL EMAIL:
{original_email}

RESPONSE:
{response}

CLASSIFY INTO:
- INTERESTED: Wants to learn more or schedule
- MEETING_REQUEST: Explicitly asks for meeting/call
- MORE_INFO: Requests specific information
- NOT_NOW: Timing is wrong but potentially interested later
- NOT_INTERESTED: Clear rejection
- OUT_OF_OFFICE: Auto-reply/vacation
- UNSUBSCRIBE: Wants to stop receiving emails
- UNCLEAR: Cannot determine intent

ALSO PROVIDE:
- sentiment: positive/neutral/negative
- key_points: main points from their response
- suggested_action: what we should do next
- follow_up_timing: if applicable, when to follow up

OUTPUT: JSON format
"""
```

### Appendix C: Google Sheets Formulas

```
LEAD SCORING FORMULA (in Leads_Master):
=IF(AND(E2<>"",F2<>"",G2<>""),
  (IF(L2="verified",30,10) +
   IF(REGEXMATCH(D2,"CEO|CTO|VP|Director|Head"),25,10) +
   IF(M2<>"",15,0) +
   IF(N2<>"",10,0) +
   20),
  0)

FOLLOW-UP DUE INDICATOR:
=IF(AND(F2<=TODAY(),G2="pending"),"DUE",
  IF(AND(F2<=TODAY()+3,G2="pending"),"UPCOMING",""))

CAMPAIGN PERFORMANCE:
=QUERY(Outreach_Tracking!A:N,
  "SELECT C, COUNT(A), SUM(IF(I='true',1,0)), SUM(IF(K='true',1,0))
   GROUP BY C
   LABEL COUNT(A) 'Sent', SUM(IF(I='true',1,0)) 'Opens',
   SUM(IF(K='true',1,0)) 'Replies'")
```

### Appendix D: Troubleshooting Guide

```
ISSUE: Low open rates (<20%)
SOLUTIONS:
1. Check sender reputation (mail-tester.com)
2. Review subject lines for spam triggers
3. Verify DNS records (SPF, DKIM, DMARC)
4. Check if emails landing in spam
5. A/B test different subject line approaches

ISSUE: Serper searches returning poor results
SOLUTIONS:
1. Refine search query structure
2. Add more specific keywords
3. Use site: operators for LinkedIn
4. Increase search result count
5. Try alternative query phrasings

ISSUE: Crawl4AI failing frequently
SOLUTIONS:
1. Increase timeout values
2. Check for JavaScript requirements
3. Rotate user agents
4. Respect rate limits
5. Handle dynamic content loading

ISSUE: High bounce rate (>5%)
SOLUTIONS:
1. Implement email verification before sending
2. Clean list of known invalid domains
3. Slow down sending speed
4. Check email format validity
5. Remove role-based emails

ISSUE: LLM generating poor quality content
SOLUTIONS:
1. Review and refine prompts
2. Add more context to prompts
3. Include examples in prompts
4. Switch to higher quality model
5. Implement output validation
```

---

## Document Approval

| Role               | Name | Signature | Date |
| ------------------ | ---- | --------- | ---- |
| System Architect   |      |           |      |
| Technical Lead     |      |           |      |
| Operations Manager |      |           |      |
| Compliance Officer |      |           |      |

---

**Document End**

_This SOP is a living document and should be updated as the system evolves and new optimizations are discovered._
