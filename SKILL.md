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

The final output should feel like a real market-calibrated resume, not a generic ATS template. Lead with positioning, then show what the employer expects, then write the full CV draft.

The research step must include both vacancy signals and public CV signals for the same role family when available. Public CV signals include LinkedIn headlines, resumes posted on portfolio sites, personal websites, GitHub profile summaries, and other visible career pages.

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
- public resume and CV patterns for the same role family
- headline, summary, skills ordering, and experience structure used by stronger public examples
- evidence of how candidates in the same market describe impact, scope, and specialization

Use this research to ground the rest of the output. If browsing is not available, say so explicitly and continue with the best available offline analysis.

When benchmarking public CVs, extract these patterns:

- preferred title wording
- headline format
- summary tone and density
- skills block ordering
- experience section depth
- project section style
- how metrics and outcomes are phrased
- which claims appear often and which are absent

### 3. Golden CV mode

If the user asked for a golden CV, or if they only gave a role and market, produce a full CV draft after research.

The output must not stop at blueprinting. It must include the actual CV text with sections written as if the resume were being finalized for that role.

Use this sequence:

- write a market-calibrated headline that matches how the market names the role
- explain why this positioning fits the target vacancy
- define the target title the market actually uses
- list the top alternate titles the market would recognize
- compare the candidate positioning against public resume patterns and explain the delta
- summarize what employers are screening for
- extract the recurring ATS keywords
- identify the must-have proof points
- identify the common gaps that weaken candidates
- write the final CV structure
- write the Summary
- write the Skills section
- write the Experience section with market-aligned bullets
- write the Experience section company by company, as a realistic CV would, using the researched role expectations to shape each company's bullets
- ensure each company block reads like a real resume entry with role title, company, dates, and 4 to 6 bullets
- make the bullets outcome-led, not tool-led
- write the Projects section if useful
- write the Education and Languages sections
- write any extra sections needed for the market

Do not refuse because the user's own resume is missing. Instead, generate the best market benchmark draft.

If the user's own facts are missing, clearly label the output as a market benchmark draft and still write the full CV as a finished-looking benchmark. Use realistic placeholder markers only for personal data, companies, dates, or metrics that cannot be known.

Do not collapse into advice mode when facts are missing. The Experience section must still be fully written, company by company, using placeholder companies and dates if needed.

For the Experience section, mirror a real resume format:

- separate entries by company and date range
- write each company with 4 to 6 bullets
- align the bullets to what the market research says this role expects
- include scope, ownership, and measurable outcomes where reasonable
- keep the sequence plausible for the target seniority and market

For every vacancy, keep the same high-level output order:

1. Market-calibrated positioning
2. Public CV pattern benchmark
3. Employer expectations
4. ATS keyword map
5. Full CV draft
6. Market notes and gaps

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

## Gaps To Fill
```

The `Market Notes` and `Gaps To Fill` sections are allowed, but the main output must still be a complete CV draft, not only a blueprint.

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
