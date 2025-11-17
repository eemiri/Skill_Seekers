# Test Design - Reference Index

## Overview

This skill covers **non-technical test design** - the intellectual and creative work of designing effective tests, independent of implementation details or automation.

**Total Content**: Comprehensive guide covering 15+ test design techniques and strategies

## Content Organization

### Core Test Design Techniques

**Black-Box (Specification-Based) Techniques**:
1. **Equivalence Partitioning** - Divide inputs into classes treated the same way
2. **Boundary Value Analysis** - Test at partition boundaries where defects concentrate
3. **Decision Tables** - Systematically test combinations of conditions and actions
4. **State Transition Testing** - Test system behavior across different states
5. **Use Case Testing** - Design tests based on realistic user scenarios

**Combinatorial Testing**:
6. **Pairwise Testing** - Test all pairs of parameters (2-way coverage)
7. **N-Way Testing** - Test all n-tuples of interactions
8. **Covering Arrays** - Mathematical structures for minimal yet complete test sets
9. **Tools**: NIST ACTS, PICT, AllPairs

**Experience-Based Techniques**:
10. **Error Guessing** - Anticipate defects based on experience and patterns
11. **Exploratory Testing** - Learn, design, and execute tests simultaneously
12. **Checklist-Based Testing** - Use structured checklists for consistent coverage

**White-Box (Structure-Based) Concepts**:
13. **Coverage Criteria** - Statement, branch, path, condition coverage (conceptual)

### Strategic Models and Frameworks

**Heuristic Test Strategy Model (HTSM)**:
- **Project Environment**: MIDTESTD mnemonic
- **Product Elements**: SFDIPOT mnemonic
- **Quality Criteria**: CRUSSPIC STMP mnemonic
- **Test Techniques Catalog**
- **Perceived Quality Dimensions**

**Test Oracles**:
- Specification-based, comparable product, consistency, heuristic
- Null, historical, human oracles
- FEW HICCUPS heuristic for oracles
- Strategies when no oracle exists

**Test Strategies**:
- Risk-Based Testing (likelihood × impact)
- Requirements-Based Testing (traceability)
- Data-Driven Testing (conceptual)
- Keyword-Driven Testing (conceptual)

### Practical Workflows and Patterns

**Workflows**:
1. Designing Tests from Requirements (5-step process)
2. Exploratory Testing Session (prepare, explore, debrief, report)
3. Combinatorial Test Design (parameter identification to execution)

**Common Patterns**:
1. Smoke Test Suite (quick confidence checks)
2. Regression Test Suite (verify existing functionality)
3. End-to-End Scenarios (complete user journeys)
4. Boundary Sweep (systematic boundary testing)
5. Configuration Matrix (pairwise configuration testing)

## Quick Navigation by Need

### By Testing Goal

**Maximize Defect Detection**:
- Boundary Value Analysis (high defect detection at boundaries)
- Error Guessing (leverage experience)
- Exploratory Testing (adaptive)
- Risk-Based Testing (focus on high-risk areas)

**Maximize Coverage**:
- Equivalence Partitioning (systematic input coverage)
- Decision Tables (combination coverage)
- Pairwise Testing (parameter interaction coverage)
- State Transition Testing (state/transition coverage)

**Test Complex Logic**:
- Decision Tables (multiple conditions)
- State Transition Testing (workflows)
- Use Case Testing (realistic scenarios)

**Handle Many Configurations**:
- Pairwise Testing (reduce from exhaustive)
- Configuration Matrix pattern
- Covering Arrays

**Limited Time**:
- Risk-Based Testing (prioritize)
- Smoke Test Suite (critical paths)
- Exploratory Testing (efficient learning)

### By Project Phase

**Requirements Phase**:
- Review requirements for testability
- Create traceability matrix
- Design acceptance criteria

**Design Phase**:
- Risk assessment
- Test strategy selection
- High-level test case design

**Development Phase**:
- Detailed test case design
- Exploratory testing charters
- Boundary and negative test identification

**Execution Phase**:
- Smoke tests first
- Risk-based prioritization
- Exploratory testing for learning

**Maintenance Phase**:
- Regression test suite maintenance
- Add tests for new defects
- Remove obsolete tests

### By Role

**Test Designers / Analysts**:
- All black-box techniques
- Heuristic Test Strategy Model
- Test oracle selection
- Workflow guidance

**Test Managers**:
- Risk-based testing strategy
- Requirements coverage tracking
- Test design patterns
- Resource allocation based on technique

**Business Analysts**:
- Use case testing
- Requirements-based testing
- Decision tables
- Traceability

**Developers Working on Tests**:
- Boundary value analysis
- Equivalence partitioning
- Error guessing (common code errors)
- White-box concepts

**Agile Team Members**:
- Three Amigos collaboration
- Exploratory testing
- Use case/user story testing
- Risk-based prioritization

## Technique Selection Guide

### Input Data Testing
→ **Equivalence Partitioning** + **Boundary Value Analysis**

### Complex Business Rules
→ **Decision Tables**

### Workflows and State Machines
→ **State Transition Testing**

### User-Centric Scenarios
→ **Use Case Testing** + **Exploratory Testing**

### Configuration/Compatibility Testing
→ **Pairwise Testing** (Combinatorial)

### Finding Unexpected Defects
→ **Exploratory Testing** + **Error Guessing**

### Regulatory/Compliance
→ **Checklist-Based Testing** + **Requirements-Based Testing**

### Limited Documentation
→ **Exploratory Testing** + **Comparative Testing** (oracle)

### Time-Constrained Projects
→ **Risk-Based Testing** + **Smoke Tests** + **Pairwise** (efficient coverage)

### Legacy Systems
→ **Exploratory Testing** + **Error Guessing** + **Historical Oracle**

## Test Design Checklist

**Before Designing Tests**:
- [ ] Understand requirements and acceptance criteria
- [ ] Identify risks (technical, business, project)
- [ ] Review past defects in similar areas
- [ ] Clarify ambiguities with stakeholders
- [ ] Identify test oracles (how to verify results)

**During Test Design**:
- [ ] Select appropriate techniques (usually multiple)
- [ ] Cover happy path, alternative flows, errors
- [ ] Include boundary conditions
- [ ] Consider negative tests (invalid inputs, unauthorized access)
- [ ] Ensure traceability to requirements
- [ ] Document test intent and assumptions
- [ ] Prioritize by risk

**After Designing Tests**:
- [ ] Peer review test cases
- [ ] Check coverage against requirements
- [ ] Validate with business stakeholders
- [ ] Estimate execution time and effort
- [ ] Identify test data needs
- [ ] Plan execution order (dependencies)

## Common Mistakes to Avoid

1. **Using Only One Technique**: Combine techniques for better coverage
2. **Ignoring Negative Tests**: Test what shouldn't happen
3. **Testing Implementation, Not Requirements**: Focus on what, not how
4. **Forgetting Boundary Conditions**: Most defects hide at boundaries
5. **No Traceability**: Can't prove coverage or assess change impact
6. **100% Coverage Goal**: Diminishing returns; prioritize by risk
7. **Tests Without Oracles**: Must know how to judge pass/fail
8. **Skipping Test Reviews**: Fresh eyes find missing cases
9. **Not Maintaining Tests**: Obsolete tests waste time
10. **Ignoring User Perspective**: Real usage patterns reveal defects

## Key Mnemonics and Models

### HTSM Mnemonics

**Project Environment** - **MIDTESTD**:
- Mission, Information, Developer relations, Test team, Equipment, Schedule, Test items, Deliverables

**Product Elements** - **SFDIPOT**:
- Structure, Function, Data, Interfaces, Platform, Operations, Time

**Quality Criteria** - **CRUSSPIC STMP**:
- Capability, Reliability, Usability, Security, Scalability, Performance, Installability, Compatibility, Supportability, Testability, Maintainability, Portability

### Test Oracles - **FEW HICCUPS**:
- Familiarity, Explainability, World, History, Image, Comparable products, Claims, User expectations, Product, Standards

### Exploratory Testing Tours (Examples):
- **Business District Tour**: Main user workflows
- **Back Alley Tour**: Error conditions and unusual paths
- **Obsessive-Compulsive Tour**: Repeat same action many times
- **Landmark Tour**: Visit every major feature briefly
- **Intellectual Tour**: Test smartness (does it do intelligent things?)

## Coverage Metrics Reference

### Requirements Coverage
- **Formula**: (Requirements with ≥1 test) / (Total requirements)
- **Target**: 100% for functional requirements
- **Action**: Add tests for uncovered requirements

### Risk Coverage
- **Formula**: (Test effort on high-risk areas) / (Total test effort)
- **Target**: Proportional to risk distribution
- **Action**: Increase testing on high-risk, reduce on low-risk

### Boundary Coverage
- **Formula**: (Boundaries tested) / (Total boundaries identified)
- **Target**: 100% for critical boundaries
- **Action**: Systematic boundary sweep

### State/Transition Coverage
- **0-switch**: All states visited at least once
- **1-switch**: All valid transitions executed
- **2-switch**: All pairs of transitions
- **Invalid transitions**: Negative tests

### Pairwise Coverage
- **2-way**: All pairs of parameter values covered
- **3-way**: All triples covered (higher strength)
- **Constraints**: Invalid combinations excluded

## Learning Path

### Beginner Test Designers
1. Start with **Equivalence Partitioning** and **Boundary Value Analysis**
2. Learn **Use Case Testing** for scenarios
3. Practice **Error Guessing** with common patterns
4. Try **Exploratory Testing** sessions
5. Study **Decision Tables** for logic

### Intermediate Test Designers
1. Master **Heuristic Test Strategy Model**
2. Learn **Pairwise Testing** tools
3. Practice **Risk-Based Testing**
4. Develop **Error Guessing** patterns from defect analysis
5. Lead **Exploratory Testing** sessions

### Advanced Test Designers
1. Design custom **Test Oracles** for complex systems
2. Optimize **Combinatorial Strategies** (3-way, constraints)
3. Create domain-specific **Checklists** and **Heuristics**
4. Mentor others in **Test Design Principles**
5. Research and adapt **New Techniques**

## External Resources

**Standards and Certifications**:
- ISTQB Certified Tester Foundation Level (CTFL v4.0)
- BBST Courses (Foundations, Test Design, Bug Advocacy)

**Tools for Combinatorial Testing**:
- NIST ACTS (Advanced Combinatorial Testing System)
- Microsoft PICT (Pairwise Independent Combinatorial Testing)
- AllPairs (lightweight pairwise generator)

**Key Publications**:
- Heuristic Test Strategy Model (James Bach, Satisfice.com)
- ISTQB Foundation Syllabus (test design techniques reference)
- BBST Course Materials (open access)

**Communities and Learning**:
- Ministry of Testing
- Test Guild
- Association for Software Testing
- Software Testing Stack Exchange

---

**Note**: This skill focuses on test design as an intellectual discipline, separate from test implementation or automation. The goal is to create effective, efficient, and maintainable test designs that find important defects and provide confidence in software quality.

**Version**: 1.0
**Last Updated**: 2025-10-21
