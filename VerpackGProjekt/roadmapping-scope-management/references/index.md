# Roadmapping & Scope Management - Reference Index

This skill combines documentation from multiple authoritative sources on product roadmapping and scope management.

## Sub-Skills Available

### 1. Basecamp Shape Up (100 pages)
**Location**: `../basecamp-shapeup/`
**Coverage**: Complete Shape Up methodology book

**Categories**:
- `shaping.md` (38 pages) - Principles of shaping, appetites, boundaries, breadboarding, fat marker sketches
- `betting.md` (35 pages) - Betting tables, six-week cycles, circuit breakers, no backlogs
- `building.md` (1 page) - Execution and delivery practices
- `other.md` (26 pages) - Additional concepts and practices

**Key Topics**:
- Setting appetite (fixed time, variable scope)
- Shaping work before building
- Six-week cycles and two-week cool-downs
- Betting tables and circuit breakers
- Hill Charts for tracking progress
- Rabbit holes and no-gos
- Vertical slices and scope hammering

### 2. Aha! Roadmapping Guide (150 pages)
**Location**: `../aha-roadmapping/`
**Coverage**: Comprehensive roadmapping and product planning guide

**Categories**:
- `fundamentals.md` (40 pages) - What is roadmapping, who owns it, core concepts
- `strategy.md` (29 pages) - Vision, goals, initiatives, value-based development
- `building.md` (56 pages) - Creating roadmaps, frameworks, Aha! methodology
- `prioritization.md` (3 pages) - Scoring, prioritization frameworks
- `communication.md` (1 page) - Stakeholder communication, reporting
- `other.md` (21 pages) - Additional topics and resources

**Key Topics**:
- Product vision and strategy
- Goals and initiatives
- Roadmap types (business, portfolio, features, technology, go-to-market)
- Prioritization frameworks and scoring
- Stakeholder communication
- The Aha! Framework for product development
- Release planning and capacity management
- Value-based product development

### 3. MoSCoW Prioritisation (1 page)
**Location**: `../moscow-prioritisation/`
**Coverage**: Core MoSCoW framework documentation

**Key Topics**:
- Must have (critical requirements)
- Should have (important but not vital)
- Could have (desirable but not necessary)
- Won't have (explicitly out of scope)
- Applying the framework to requirements prioritization

### 4. ProductPlan Guide (1 page)
**Location**: `../productplan-guide/`
**Coverage**: Product management resources and best practices

**Key Topics**:
- Product management glossary
- Roadmapping techniques
- Planning frameworks and templates

## How to Use These References

### For Specific Methodologies
- **Shape Up implementation** → Load `basecamp-shapeup` skill, focus on shaping.md and betting.md
- **Strategic roadmapping** → Load `aha-roadmapping` skill, focus on strategy.md and building.md
- **Requirements prioritization** → Load `moscow-prioritisation` skill

### For Common Tasks
- **Setting project scope** → Shape Up shaping.md (appetite, boundaries)
- **Planning quarterly roadmap** → Aha! strategy.md + building.md
- **Prioritizing backlog** → MoSCoW + Aha! prioritization.md
- **Tracking project progress** → Shape Up (Hill Charts in building.md)
- **Stakeholder communication** → Aha! communication.md + roadmap views

### For Different Roles
- **Product Managers** → All sources, focus on strategy and communication
- **Team Leads** → Shape Up for execution, Aha! for planning
- **Designers** → Shape Up shaping.md for breadboarding and fat marker sketches
- **Engineers** → Shape Up building.md for vertical slices and scope hammering
- **Stakeholders** → Aha! fundamentals.md and communication.md

## Integration Patterns

### Combining Shape Up + Strategic Roadmapping
1. Use Aha! framework for vision, goals, initiatives (quarterly/annual)
2. Use Shape Up cycles for execution (six-week builds)
3. Feed shaped work from roadmap into betting table
4. Track strategic progress through shipped cycles

### Combining MoSCoW + Shape Up
1. Use MoSCoW to identify Must-haves for shaping
2. Set appetite based on Should/Could classification
3. Mark Won't-haves as explicit no-gos in pitch
4. Scope hammer to Must-haves when time boxing

### Combining All Three
1. **Strategy layer** (Aha!): Vision → Goals → Initiatives
2. **Prioritization layer** (MoSCoW): Must/Should/Could/Won't
3. **Execution layer** (Shape Up): Shape → Bet → Build

## File Navigation

All sub-skills are located in the parent `output/` directory:

```
output/
├── roadmapping-scope-management/    (This router skill)
│   ├── SKILL.md
│   └── references/
│       └── index.md (this file)
├── basecamp-shapeup/
│   ├── SKILL.md
│   └── references/
│       ├── shaping.md
│       ├── betting.md
│       ├── building.md
│       └── other.md
├── aha-roadmapping/
│   ├── SKILL.md
│   └── references/
│       ├── fundamentals.md
│       ├── strategy.md
│       ├── building.md
│       ├── prioritization.md
│       ├── communication.md
│       └── other.md
├── moscow-prioritisation/
│   ├── SKILL.md
│   └── references/
│       └── other.md
└── productplan-guide/
    ├── SKILL.md
    └── references/
        └── other.md
```

## Quick Reference: When to Use Which Source

| Your Need | Primary Source | Supporting Sources |
|-----------|---------------|-------------------|
| Six-week cycles | Shape Up | Aha! (planning) |
| Strategic roadmap | Aha! | Shape Up (execution) |
| Requirements prioritization | MoSCoW | Aha! (scoring) |
| Appetite setting | Shape Up | MoSCoW (scope) |
| Stakeholder communication | Aha! | Shape Up (Hill Charts) |
| Progress tracking | Shape Up (Hill Charts) | Aha! (reporting) |
| Feature scoring | Aha! | MoSCoW |
| Risk management | Shape Up (rabbit holes) | All sources |
| Scope management | Shape Up | MoSCoW |
| Vision/Strategy | Aha! | Shape Up (principles) |

---

**Total Documentation**: 252+ pages across 4 authoritative sources
**Last Updated**: 2025-10-21
