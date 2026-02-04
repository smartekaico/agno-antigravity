# Plan: Multi-Strategy Lead Search

ID: 002-lead-search
Directive: lead-search
Cost: ~$2.50 (Serper + Apify) | Tokens: ~25k

## Objective

Implement a modular lead generation system that supports two distinct strategies:

1.  **Local Business**: Discovery (Serper Maps) -> Instagram Enrichment (Apify).
2.  **B2B/Professional**: Discovery (Serper X-Ray) -> LinkedIn Enrichment (Apify).

## Context Applied

- `lead-search.md` (Updated)
- `GEMINI.md` v5.0

## Steps

- [ ] Create branch `feature/002-lead-search`
- [ ] **Configuration**:
  - [ ] Verify `APIFY_TOKEN` and `SERPER_API_KEY`.
  - [ ] Update `rules/tech-stack.md` to include Apify actors.
- [ ] **Skill Integration**:
  - [ ] Create `apify` skill wrapper (`.agent/skills/apify/SKILL.md`).
  - [ ] Verify `crawl4ai` skill.
- [ ] **Workflow Implementation**:
  - [ ] Create `lead-search-workflow` that accepts `strategy` ("LOCAL" or "B2B").
  - [ ] Implement Strategy A (Local): `Serper -> Crawl4AI -> Apify (IG)`.
  - [ ] Implement Strategy B (B2B): `Serper (X-Ray) -> Apify (LinkedIn)`.
- [ ] **Verification**:
  - [ ] Test Strategy A: "Gyms in Austin".
  - [ ] Test Strategy B: "CTO SaaS London".

## Files

- `.agent/skills/apify/SKILL.md` (New)
- `.agent/workflows/lead-generation.md` (New)

## Rollback

- Delete branch `feature/002-lead-search`
