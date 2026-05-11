# Skill: `career-positioning-builder`

## Purpose

Build ATS-friendly career positioning from any combination of:

- a tech stack
- a resume or CV
- a target job description
- a target market: US, UK, EU, or global

Use this skill when the user wants to understand which roles fit their background, map skills to job titles, rewrite bullets, adapt a resume for a market, or prepare LinkedIn and recruiter outreach materials.

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

If critical context is missing, ask only for what is needed next:

- target market: US, UK, EU, global, or specific country
- seniority: junior, mid, senior, lead, staff
- goal: positioning, rewrite, gap analysis, or application package

## Workflow

### 1. Identify the input type

Classify the user's material into one or more of:

- stack notes
- resume/CV text
- job description
- target market
- constraints or preferences

### 2. Diagnose positioning

Produce:

- primary role
- 2 to 4 alternative titles
- role family
- likely seniority
- strongest signals
- weak signals
- missing proof points

Use `references/role-taxonomy.md` and `references/skill-to-role-mapping.md` as the main mapping sources.

### 3. Build the keyword map

Split keywords into:

- must-have keywords
- strong keywords
- optional keywords
- risky or unsupported keywords

Use `references/tech-keyword-clusters.md` and the target job description.

### 4. Rewrite or assemble the deliverable

Depending on the user's goal, produce one or more of:

- career map
- resume/CV rewrite
- bullet rewrites
- LinkedIn headline and summary
- recruiter outreach message
- gap analysis
- application strategy

### 5. Run an honesty check

Flag anything that is:

- unproven
- too vague
- inflated
- missing a metric
- missing business context

Do not invent experience, tools, company scale, or impact.

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
