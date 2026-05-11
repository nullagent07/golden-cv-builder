---
name: golden-cv-builder
description: researches current job markets and builds golden ATS-friendly CVs, resumes, LinkedIn positioning, keyword maps, and job-application materials from a user's role target, resume, tech stack, or career goal. Use when the user wants a market-first CV for US, UK, or EU roles, a job-aligned resume rewrite, role-to-keyword mapping, salary guidance, or a golden CV benchmark for technical, data, AI, product, analytics, or engineering positions.
---

# Golden CV Builder

## Purpose

Build ATS-friendly career positioning from any combination of:

- a tech stack
- a resume or CV
- a target job description
- a target market: US, UK, EU, or global

Use this skill when the user wants to understand which roles fit their background, map skills to job titles, rewrite bullets, adapt a resume for a market, or prepare LinkedIn and recruiter outreach materials.

When the user provides a role, resume, or target market, do not stop at abstract advice. First, research current public job postings for that market/role and, when useful, benchmark publicly visible resume patterns for the same role family. Use that market evidence to shape the final CV, keywords, title, and salary guidance.

## Core Principle

Do not optimize for one stack. Optimize for the candidate's strongest marketable positioning.

Prefer honest positioning over inflated claims. Every output must stay grounded in the source material the user provided.

## Intake Modes

Detect which inputs are available and proceed accordingly:

1. Stack only
2. Resume or CV only
3. Job description only
4. Resume + job description
5. Resume + stack + target market
6. Resume + stack + job description + target market
7. Role only
8. Role + target market

If critical context is missing, ask only for what is needed next:

- target market: US, UK, EU, global, or specific country
- seniority: junior, mid, senior, lead, staff
- goal: positioning, rewrite, gap analysis, or application package
- if the user asked for a golden CV, proceed without asking for a resume first

## Workflow

### 1. Identify the input type

Classify the user's material into one or more of:

- stack notes
- resume/CV text
- job description
- target market
- constraints or preferences

### 2. Research the market

If the user gave enough context to search, collect live evidence before drafting the final output:

- current job postings for the target role or role family
- repeated keywords, tools, and responsibilities
- seniority signals in the market
- common salary bands if available from public sources
- resume patterns that match the same role family

Use this research to ground the rest of the output. If browsing is not available, say so explicitly and continue with the best available offline analysis.

### 3. Golden CV mode

If the user asked for a golden CV, or if they only gave a role and market, produce a full CV draft after research.

The output must not stop at blueprinting. It must include the actual CV text with sections written as if the resume were being finalized for that role.

Use this sequence:

- define the target title the market actually uses
- summarize what employers are screening for
- extract the recurring ATS keywords
- identify the must-have proof points
- identify the common gaps that weaken candidates
- write the final CV structure
- write the Summary
- write the Skills section
- write the Experience section with market-aligned bullets
- for Senior or Lead roles, write the Experience section as a market-standard 5-year senior experience arc, showing progression across 2 to 3 roles or phases
- write the Projects section if useful
- write the Education and Languages sections
- write any extra sections needed for the market

Do not refuse because the user's own resume is missing. Instead, generate the best market benchmark draft.

If the user's own facts are missing, clearly label the output as a market benchmark draft and use realistic placeholder markers only for personal data, companies, dates, or metrics that cannot be known.

### 4. Diagnose positioning

Produce:

- primary role
- 2 to 4 alternative titles
- role family
- likely seniority
- strongest signals
- weak signals
- missing proof points

Use `references/role-taxonomy.md` and `references/skill-to-role-mapping.md` as the main mapping sources.

### 5. Build the keyword map

Split keywords into:

- must-have keywords
- strong keywords
- optional keywords
- risky or unsupported keywords

Use `references/tech-keyword-clusters.md` and the target job description.

### 6. Rewrite or assemble the deliverable

Depending on the user's goal, produce one or more of:

- career map
- resume/CV rewrite
- bullet rewrites
- LinkedIn headline and summary
- recruiter outreach message
- gap analysis
- application strategy

### 7. Run an honesty check

Flag anything that is:

- unproven
- too vague
- inflated
- missing a metric
- missing business context

Do not invent experience, tools, company scale, or impact.

When the user asked for a golden CV and has not provided personal experience, use placeholders like `[YOUR EXPERIENCE HERE]` instead of asking to stop.

## Default Output Format

When the user asks for positioning, use this structure:

```markdown
## Candidate Career Map

Primary positioning:
Alternative titles:
Role family:
Market fit:
Strongest signals:
Weak signals:
Keyword map:
Gap notes:
Recommended next step:
```

When the user asks for a resume rewrite, use:

```markdown
## Target Title

## Summary

## Skills

## Experience

## Projects

## Education

## Extra Sections
```

When the user asks for a golden CV, use the full CV draft format below:

```markdown
## [Target Title]

## Summary

## Core Skills

## Professional Experience

## Selected Projects

## Education

## Languages

## Additional Information

## Market Notes

## Senior Experience Arc

## Gaps To Fill
```

The `Market Notes`, `Senior Experience Arc`, and `Gaps To Fill` sections are allowed, but the main output must still be a complete CV draft, not only a blueprint.

For Senior roles, the `Professional Experience` section should read like a realistic senior benchmark resume:

- phase 1: solid iOS foundation with delivery ownership
- phase 2: deeper product feature ownership and architecture
- phase 3: performance, testing, release quality, mentoring, and cross-functional leadership

Use the market research to decide the bullets, but keep the draft concrete and readable as if it were a real CV.

## Market Rules

Use `references/ats-rules-us-eu.md` and `references/market-positioning-templates.md` to adapt the output for the target market.

### US

- no photo
- no age or date of birth
- impact-first bullets
- strong keyword coverage
- typically 1 to 2 pages

### UK / EU

- keep personal data minimal
- include work authorization when relevant
- include languages when relevant
- tailor formatting to local expectations

## Bullet Writing Rules

Use the formula from `references/resume-bullet-formulas.md`:

- action + technology + scope + result
- action + ownership + business outcome
- action + scale + measurable impact

Prefer specific evidence over generic claims.

## Reference Files

- `references/role-taxonomy.md`
- `references/skill-to-role-mapping.md`
- `references/tech-keyword-clusters.md`
- `references/ats-rules-us-eu.md`
- `references/resume-bullet-formulas.md`
- `references/market-positioning-templates.md`
- `references/intake-questionnaire.md`

## Asset Files

- `assets/us-resume-template.md`
- `assets/eu-cv-template.md`
- `assets/linkedin-profile-template.md`
- `assets/recruiter-message-template.md`

## Tooling

Use `scripts/keyword_gap_checker.py` when the user provides a resume and a target role or job description and wants a keyword gap summary.

## Response Style

- be direct
- be market-aware
- be honest about gaps
- avoid generic career advice unless it supports the specific positioning
- prioritize practical output the user can use immediately
