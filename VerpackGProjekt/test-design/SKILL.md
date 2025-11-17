# Test Design Skill (Non-Technical)

## When to Use This Skill

Use this skill when you need guidance on:

- **Test design techniques**: Black-box, white-box, and experience-based testing methods
- **Test case creation**: Designing effective test cases without technical implementation details
- **Test strategy**: Planning test approaches using heuristics and models
- **Combinatorial testing**: Pairwise testing, covering arrays, and interaction testing
- **Exploratory testing**: Session-based testing, test charters, and rapid test design
- **Test oracles**: Determining expected results and verification strategies
- **Risk-based testing**: Prioritizing tests based on risk assessment
- **Requirements-based testing**: Tracing tests to requirements and specifications
- **Domain testing**: Boundary value analysis, equivalence partitioning
- **Decision testing**: Decision tables, state transition testing
- **Heuristic testing**: Using rules of thumb and testing mnemonics

This skill focuses on the **intellectual and creative aspects of test design** - the "what" and "why" of testing - rather than technical implementation ("how" to automate or code tests).

## Core Test Design Knowledge

### Test Design Fundamentals

**What is Test Design?**
Test design is the process of creating test cases and test conditions that:
- Effectively reveal defects
- Provide adequate coverage of the system
- Are efficient and maintainable
- Support risk management objectives
- Can be executed within constraints (time, budget, resources)

**Key Principles**:
1. **Coverage**: Tests should cover requirements, risks, and system behavior
2. **Effectiveness**: Tests should find important defects
3. **Efficiency**: Achieve maximum coverage with minimum tests
4. **Maintainability**: Tests should be easy to understand and update
5. **Traceability**: Tests should link to requirements and risks

**Test Design vs. Test Execution**:
- **Test Design**: Creating test conditions, test cases, test data (this skill's focus)
- **Test Execution**: Running tests, comparing actual vs expected, logging results
- **Test Automation**: Implementing tests in code (out of scope for this skill)

### Test Design Techniques Overview

**Three Main Categories**:

1. **Black-Box (Specification-Based)**
   - Based on requirements, specifications, or user stories
   - No knowledge of internal code structure needed
   - Techniques: Equivalence partitioning, boundary value analysis, decision tables, state transition, use case testing

2. **White-Box (Structure-Based)**
   - Based on internal code structure and design
   - Requires code knowledge (but we focus on concepts, not implementation)
   - Techniques: Statement coverage, branch coverage, path coverage, condition coverage

3. **Experience-Based**
   - Based on tester's knowledge, intuition, and experience
   - Techniques: Error guessing, exploratory testing, checklist-based testing, attack-based testing

## Black-Box Test Design Techniques

### 1. Equivalence Partitioning (EP)

**Concept**:
Divide input data into partitions (classes) where all values are expected to be treated the same way by the system.

**Why Use It**:
- Reduces number of test cases needed
- Provides systematic coverage
- Works for both valid and invalid data

**How to Apply**:
1. Identify input conditions or output requirements
2. Divide into valid and invalid equivalence classes
3. Create one test case per equivalence class
4. Aim for each test to cover multiple valid classes simultaneously
5. Ensure each invalid class is tested separately

**Example - Age Field (18-65 allowed)**:
- **Valid partitions**: 18-65 (one test: age = 30)
- **Invalid partitions**:
  - Below minimum: < 18 (one test: age = 10)
  - Above maximum: > 65 (one test: age = 70)
  - Non-numeric: letters (one test: age = "abc")

**Tips**:
- Consider both input and output partitions
- Include boundary conditions in partitions
- Think about data types, ranges, sets of values

### 2. Boundary Value Analysis (BVA)

**Concept**:
Test at the boundaries between partitions, where defects are most likely to occur.

**Why Use It**:
- Defects often occur at boundaries (off-by-one errors)
- Complements equivalence partitioning
- High defect detection rate

**How to Apply**:
1. Identify boundaries of equivalence classes
2. Test values at, just below, and just above each boundary
3. For ranges, test: min, min-1, min+1, max, max-1, max+1

**Example - Age Field (18-65 allowed)**:
- Lower boundary: 17, 18, 19
- Upper boundary: 64, 65, 66

**Two-Point vs. Three-Point BVA**:
- **Two-point**: Test boundary value and just outside (18, 17 / 65, 66)
- **Three-point**: Add value just inside boundary (17, 18, 19 / 64, 65, 66)

**Tips**:
- Combine with equivalence partitioning for efficiency
- Consider boundaries in time, dates, file sizes, quantities
- Don't forget minimum and maximum together (e.g., empty list, single item, max capacity)

### 3. Decision Tables

**Concept**:
Systematically test combinations of conditions and their resulting actions.

**Why Use It**:
- Handles complex business logic with multiple conditions
- Ensures all combinations are considered
- Makes implicit requirements explicit
- Great for "if-then-else" rules

**How to Apply**:
1. Identify conditions (inputs) and actions (outputs)
2. Create columns for all possible combinations of conditions
3. Mark which actions occur for each combination
4. Eliminate impossible or redundant combinations
5. Create one test case per column

**Example - Loan Approval**:
```
Conditions:
- Credit score >= 700? (Y/N)
- Income >= $50k? (Y/N)
- Debt ratio < 40%? (Y/N)

Actions:
- Approve loan
- Deny loan
- Request manager review

Full table would have 2^3 = 8 combinations
After analysis, might reduce to 5-6 meaningful combinations
```

**Tips**:
- Start with full truth table, then simplify
- Use "don't care" (DC) for irrelevant conditions
- Consider both valid and invalid combinations
- Great for regulatory/compliance requirements

### 4. State Transition Testing

**Concept**:
Test how a system transitions between different states based on events.

**Why Use It**:
- Systems with distinct states and transitions
- Ensures valid transitions work
- Reveals invalid transitions
- Good for workflows, protocols, UI flows

**How to Apply**:
1. Identify system states
2. Identify events that trigger transitions
3. Create state transition diagram or table
4. Design tests to cover:
   - All states (0-switch coverage)
   - All valid transitions (1-switch coverage)
   - All sequences of transitions (n-switch coverage)
   - Invalid transitions (negative tests)

**Example - Login System**:
```
States: Logged Out, Logged In, Locked
Events: Login (valid), Login (invalid), Logout, 3rd Failed Login

Transitions:
- Logged Out + Login(valid) → Logged In
- Logged Out + Login(invalid) → Logged Out (fail count++)
- Logged Out + 3rd Failed Login → Locked
- Logged In + Logout → Logged Out
- Locked + (any login attempt) → Locked
```

**Coverage Levels**:
- **All states**: Visit every state at least once
- **Valid transitions**: Execute every valid transition once (1-switch)
- **All transitions**: Include invalid transitions
- **Transition pairs**: Sequences of two transitions (2-switch)

**Tips**:
- Draw diagrams first (state machines)
- Consider "impossible" transitions (negative tests)
- Watch for missing transitions
- Good for session management, document workflows

### 5. Use Case Testing

**Concept**:
Design tests based on how users actually use the system (use cases or user stories).

**Why Use It**:
- Tests realistic user scenarios
- Ensures main user flows work
- Good for functional and acceptance testing
- Aligns with Agile user stories

**How to Apply**:
1. Identify use cases or user stories
2. For each use case, design tests for:
   - Main success scenario (happy path)
   - Alternative flows
   - Exception/error flows
3. Consider pre-conditions and post-conditions
4. Add boundary and negative cases

**Example - Online Shopping**:
```
Use Case: Purchase Item

Main Flow:
1. User searches for product
2. User adds item to cart
3. User proceeds to checkout
4. User enters shipping info
5. User enters payment
6. Order confirmed

Alternative Flows:
- User applies discount code
- User selects express shipping
- User checks out as guest

Exception Flows:
- Payment declined
- Item out of stock
- Session timeout
```

**Tips**:
- Focus on end-to-end scenarios
- Include pre-conditions (e.g., logged in, cart not empty)
- Test both typical and atypical user behaviors
- Combine with boundary value analysis for inputs

## Combinatorial Testing

### Pairwise Testing (2-Way Coverage)

**Concept**:
Instead of testing all possible combinations (exhaustive), test all possible pairs of parameter values.

**Why Use It**:
- Drastically reduces test cases while maintaining high defect detection
- Studies show 70-90% of defects are triggered by single parameters or pairs
- Practical for systems with many parameters

**Example**:
```
System with 3 parameters:
- Browser: Chrome, Firefox, Safari (3 values)
- OS: Windows, Mac, Linux (3 values)
- Resolution: 1024x768, 1920x1080 (2 values)

Exhaustive: 3 × 3 × 2 = 18 combinations
Pairwise: 9-12 combinations (covering all pairs)
```

**How to Apply**:
1. Identify parameters and their values
2. Use pairwise generation tool or algorithm (ACTS, PICT, AllPairs)
3. Generate minimal set covering all pairs
4. Review and add specific combinations if needed (risk-based)

**When to Use**:
- Configuration testing (OS, browser, device combinations)
- Multiple independent parameters
- When exhaustive testing is impractical
- Early testing phases for broad coverage

**N-Way Testing**:
- **1-way**: Each value tested at least once (minimal)
- **2-way**: All pairs covered (pairwise) - **most common**
- **3-way**: All triples covered (higher coverage, more tests)
- **N-way**: All n-tuples covered (approaches exhaustive)

### Orthogonal Arrays and Covering Arrays

**Concept**:
Mathematical structures that guarantee all n-way interactions are covered with minimal tests.

**Covering Array Notation**: CA(N; t, k, v)
- N = number of tests
- t = strength (2 for pairwise)
- k = number of parameters
- v = values per parameter

**Example**: CA(9; 2, 4, 3) = 9 tests covering all pairs of 4 parameters with 3 values each

**Tools**:
- **NIST ACTS**: Free tool from NIST for generating covering arrays
- **PICT**: Microsoft's pairwise independent combinatorial testing tool
- **AllPairs**: Lightweight pairwise test case generator

**Tips**:
- Start with 2-way for most situations
- Use 3-way for higher-risk areas
- Consider constraints (invalid combinations)
- Combine with risk analysis to add specific tests

## Experience-Based Techniques

### 1. Error Guessing

**Concept**:
Anticipate where defects might occur based on experience, intuition, and knowledge of typical errors.

**Why Use It**:
- Finds defects that systematic techniques might miss
- Leverages tester expertise
- Quick and adaptable
- Good complement to specification-based techniques

**How to Apply**:
1. Review similar applications/systems
2. Consider common failure patterns
3. Think about technology-specific issues
4. Review past defect data
5. Brainstorm "what could go wrong?"

**Common Error Patterns**:
- **Off-by-one errors**: Loops, boundaries, counts
- **Null/empty handling**: Null values, empty strings, empty lists
- **Special characters**: Quotes, apostrophes, unicode, SQL injection characters
- **Number handling**: Zero, negative, very large, decimal vs integer
- **Date/time**: Leap years, time zones, DST, Y2K-style issues
- **Concurrency**: Race conditions, deadlocks
- **Resource limits**: Memory, disk space, connection limits
- **Integration points**: APIs, databases, third-party services

**Tips**:
- Maintain defect taxonomies from past projects
- Share knowledge across team
- Document your error guessing patterns
- Combine with checklists

### 2. Exploratory Testing

**Concept**:
Simultaneously learn the system, design tests, and execute tests in an iterative, adaptive way.

**Why Use It**:
- Adapts to what you learn during testing
- Good for complex systems
- Finds unexpected defects
- Complements scripted testing

**Session-Based Testing**:
Structure exploratory testing with:
- **Charter**: Mission for the session (what to explore)
- **Time-box**: Fixed duration (60-90 minutes typical)
- **Debrief**: Review findings and plan next session

**Charter Template**:
```
Explore [area]
With [resources/tools]
To discover [information/defects related to risk/requirement]
```

**Example Charters**:
- "Explore shopping cart with various product types to discover calculation errors"
- "Explore user profile with boundary data to discover validation issues"
- "Explore search functionality with special characters to discover parsing defects"

**Techniques During Exploration**:
- **Tours**: Structured exploration paths (business district tour, back alley tour, etc.)
- **Heuristics**: SFDIPOT (Structure, Function, Data, Interfaces, Platform, Operations, Time)
- **Mnemonics**: FCC CUTS VIDS (File, Clipboard, Compatibility, etc.)

**Tips**:
- Keep notes during sessions
- Track time spent on different activities
- Report findings immediately
- Pair with another tester for idea sharing

### 3. Checklist-Based Testing

**Concept**:
Use pre-defined checklists to ensure consistent coverage of known areas.

**Why Use It**:
- Ensures nothing is forgotten
- Captures team knowledge
- Quick to create and execute
- Good for reviews and inspections

**Types of Checklists**:
- **Generic**: Applies to any application (security, usability, performance)
- **Domain-specific**: E-commerce, healthcare, finance
- **Technology-specific**: Web, mobile, API
- **Regulatory**: GDPR, HIPAA, accessibility (WCAG)

**Example - Web Application Security Checklist**:
```
☐ Input validation on all fields
☐ SQL injection prevention
☐ XSS (Cross-Site Scripting) prevention
☐ CSRF token implementation
☐ Secure password storage (hashing)
☐ HTTPS for sensitive data
☐ Session timeout implemented
☐ Error messages don't reveal sensitive info
☐ File upload restrictions
☐ Access control enforced
```

**Creating Checklists**:
1. Review standards and guidelines
2. Analyze past defects
3. Consult subject matter experts
4. Keep checklists focused and actionable
5. Update based on new findings

**Tips**:
- Don't treat checklist as exhaustive
- Combine with exploratory testing
- Review and update regularly
- Make them easy to use (simple, scannable)

## Heuristic Test Strategy Model (HTSM)

### Overview

**What is HTSM?**
A structured approach to test strategy using heuristics (rules of thumb) across multiple dimensions.

**Created by**: James Bach (Satisfice.com)

**Key Components**:
1. **Project Environment**: What affects your test project
2. **Product Elements**: What you're testing
3. **Quality Criteria**: What makes the product good
4. **Test Techniques**: How you test
5. **Perceived Quality**: Stakeholder concerns

### Project Environment Factors

**MIDTESTD Mnemonic**:
- **Mission**: What problems are you solving? What are your testing goals?
- **Information**: What do you need to know? Sources: specs, code, users, competition
- **Developer Relations**: Who creates the product? How do you work together?
- **Test Team**: Who tests? Skills, tools, diversity
- **Equipment & Tools**: What hardware/software do you need?
- **Schedule**: When must we be done? Key milestones?
- **Test Items**: What ships to customers? Scope of testing
- **Deliverables**: What testng outputs are needed? Reports, metrics, test cases?

### Product Elements (What to Test)

**SFDIPOT Mnemonic**:
- **Structure**: Physical components (files, modules, integrations)
- **Function**: What the product does (features, capabilities)
- **Data**: Information processed or produced
- **Interfaces**: How components connect (UI, API, hardware)
- **Platform**: External systems it depends on (OS, browser, database)
- **Operations**: How it's used (scenarios, workflows, configurations)
- **Time**: Time-related behavior (performance, timeouts, date handling)

**How to Use**:
- Go through each element systematically
- Ask "What could go wrong here?"
- Design tests targeting each area
- Use as checklist for completeness

### Quality Criteria (What Makes It Good?)

**CRUSSPIC STMP Mnemonic**:
- **Capability**: Can it perform required functions?
- **Reliability**: Is it available and accurate?
- **Usability**: Can users operate it easily?
- **Security**: Is it protected from threats?
- **Scalability**: Can it handle growth?
- **Performance**: Is it fast enough?
- **Installability**: Can it be deployed smoothly?
- **Compatibility**: Does it work with other systems?
- **Supportability**: Can it be maintained?
- **Testability**: Can we test it effectively?
- **Maintainability**: Can it be modified easily?
- **Portability**: Can it work in different environments?

**Risk-Based Testing**:
- Prioritize quality criteria by importance to stakeholders
- Focus testing on high-priority criteria
- Allocate effort based on risk

### Test Techniques Catalog

**Category-Based**:
- Function testing
- Domain testing
- Specification testing
- Risk-based testing
- Automatic checking
- Exploratory testing
- User testing
- Scenario testing
- Claims testing
- Regression testing
- Stress testing

**Activity-Based**:
- Manual testing
- Automated testing
- Formal review
- Pair testing
- Mob testing

**Evaluation-Based**:
- Pass/fail testing
- Comparative testing (against previous version, competitor)
- Mutation testing
- Metamorphic testing

## Test Oracles

### What is a Test Oracle?

**Definition**:
A mechanism for determining whether a test has passed or failed - how we know expected results.

**The Oracle Problem**:
For many systems, knowing the correct output is as hard as building the system itself. We need practical oracles.

### Types of Oracles

**1. Specification-Based Oracle**
- Expected results come from requirements/specs
- **Strengths**: Objective, traceable
- **Weaknesses**: Specs may be incomplete, ambiguous, or wrong

**2. Comparable Product Oracle**
- Compare to competitor or previous version
- **Strengths**: Practical, finds differences
- **Weaknesses**: Other product might also be wrong

**3. Consistency Oracle**
- System should behave consistently in similar situations
- **Example**: Same search term should give same results
- **Strengths**: Finds unexpected variations
- **Weaknesses**: Doesn't catch errors consistent across board

**4. Heuristic Oracle**
- Rules of thumb about how software should behave
- **Examples**:
  - "The system should not crash"
  - "Error messages should be helpful"
  - "Output should match input format"
  - "Performance should be reasonable"

**5. Null Oracle**
- System should do nothing in certain cases
- **Example**: Invalid input should not change state

**6. Historical Oracle**
- Compare current behavior to previous baseline
- **Use**: Regression testing
- **Tool**: Golden master testing

**7. Human Oracle**
- Expert judges correctness
- **Use**: Complex calculations, UI/UX
- **Weakness**: Subjective, not scalable

### Oracle Heuristics

**FEW HICCUPS** (Heuristic Oracles):
- **Familiarity**: Similar to something you know
- **Explainability**: Can you explain behavior?
- **World**: Consistent with real world
- **History**: Consistent with past versions
- **Image**: Consistent with branding/marketing
- **Comparable Products**: Similar to competition
- **Claims**: Matches advertising/documentation
- **User Expectations**: Meets user assumptions
- **Product**: Internal consistency
- **Standards**: Meets industry standards, regulations

### When No Oracle Exists

**Strategies**:
1. **Partial Oracle**: Check some properties (e.g., output format valid)
2. **Metamorphic Relations**: If input changes in X way, output should change in Y way
3. **N-Version Testing**: Compare multiple independent implementations
4. **Statistical Oracle**: Output distribution should match expected pattern
5. **Crowd Oracle**: Aggregate opinions of multiple users

## Test Strategy Patterns

### Risk-Based Testing

**Concept**:
Prioritize and allocate testing effort based on risk (likelihood × impact of failure).

**Process**:
1. **Identify Risks**:
   - Technical risks (complexity, new technology)
   - Business risks (financial impact, reputation)
   - Project risks (tight deadlines, inexperienced team)

2. **Assess Risks**:
   - **Likelihood**: How probable is failure? (Low/Med/High or 1-5 scale)
   - **Impact**: How severe if it fails? (Low/Med/High or 1-5 scale)
   - **Risk Level**: Likelihood × Impact

3. **Prioritize Testing**:
   - High risk → Deep testing, early testing, multiple techniques
   - Medium risk → Standard testing
   - Low risk → Light testing or skip if time-constrained

4. **Monitor and Adjust**:
   - Track defects by risk area
   - Adjust strategy based on findings

**Example Risk Matrix**:
```
           Impact
         Low  Med  High
High      M    H    H
Likelihood Med   L    M    H
Low       L    L    M

H = High Priority Testing
M = Medium Priority
L = Low Priority
```

### Requirements-Based Testing

**Concept**:
Ensure every requirement has corresponding tests (bidirectional traceability).

**Process**:
1. **Requirements Coverage**:
   - Each requirement should have ≥1 test
   - Critical requirements should have multiple tests
   - Test both functional and non-functional requirements

2. **Traceability Matrix**:
   ```
   Requirement ID | Test Case IDs | Status
   REQ-001        | TC-001, TC-002, TC-015 | Covered
   REQ-002        | TC-003 | Covered
   REQ-003        | (none) | NOT COVERED ⚠
   ```

3. **Coverage Metrics**:
   - % requirements with tests
   - % requirements passed
   - % requirements not tested

**Benefits**:
- Ensures no requirement is forgotten
- Supports impact analysis (if requirement changes, which tests affected?)
- Demonstrates completeness to stakeholders

### Data-Driven Testing Strategy

**Concept**:
Separate test logic from test data to enable testing multiple scenarios with same test structure.

**Approach** (Conceptual, not implementation):
1. **Identify Test Flow**: Steps that repeat with different data
2. **Extract Test Data**: Values that change between iterations
3. **Create Data Sets**: Tables or files with input/expected output pairs
4. **Execute**: Run same test logic with each data set

**Example - Login Test**:
```
Test Logic: Enter username, enter password, click login, verify result

Test Data:
| Username | Password | Expected Result |
|----------|----------|----------------|
| valid    | valid    | Success        |
| valid    | invalid  | Error message  |
| invalid  | valid    | Error message  |
| empty    | valid    | Error message  |
| valid    | empty    | Error message  |
```

**Benefits**:
- Easy to add new test scenarios
- Non-technical users can contribute test data
- Clear separation of concerns

### Keyword-Driven Testing Strategy

**Concept**:
Define tests using high-level keywords representing actions (non-technical abstraction).

**Example**:
```
Keyword: OpenApplication
Keyword: Login [username] [password]
Keyword: NavigateToPage [pageName]
Keyword: VerifyElementPresent [elementName]

Test Case:
1. OpenApplication
2. Login "testuser" "password123"
3. NavigateToPage "Dashboard"
4. VerifyElementPresent "Welcome Message"
```

**Benefits**:
- Business-readable tests
- Reusable actions
- Changes to UI only affect keyword implementation, not test cases

## Test Design Workflows

### Workflow 1: Designing Tests from Requirements

```
1. Review Requirement:
   - Understand functional and non-functional aspects
   - Identify inputs, outputs, behaviors
   - Note ambiguities or questions

2. Identify Test Conditions:
   - Valid scenarios (happy path)
   - Invalid scenarios (negative tests)
   - Boundary conditions
   - Error handling

3. Select Techniques:
   - Equivalence partitioning for inputs
   - Boundary value analysis for ranges
   - Decision tables for complex logic
   - State transition for workflows
   - Use case testing for user scenarios

4. Create Test Cases:
   - Specify: preconditions, inputs, steps, expected results
   - Ensure traceability to requirement
   - Prioritize by risk

5. Review Test Cases:
   - Peer review for completeness
   - Check against acceptance criteria
   - Validate with stakeholders
```

### Workflow 2: Exploratory Testing Session

```
1. Prepare:
   - Define charter (what to explore, why)
   - Time-box session (60-90 min)
   - Gather tools and test data

2. Explore:
   - Execute charter
   - Take notes on observations
   - Record defects immediately
   - Follow interesting threads
   - Track time allocation

3. Debrief:
   - Summarize findings
   - Identify areas for deeper testing
   - Update risk assessment
   - Plan next charter

4. Report:
   - Document coverage achieved
   - Report defects with context
   - Share learning with team
```

### Workflow 3: Combinatorial Test Design

```
1. Identify Parameters:
   - System inputs, configurations, environments
   - List values for each parameter

2. Choose Coverage Strength:
   - 2-way (pairwise) for most cases
   - 3-way for critical areas
   - 1-way for smoke tests

3. Generate Covering Array:
   - Use tool (ACTS, PICT, AllPairs)
   - Apply constraints for invalid combinations
   - Review generated test set

4. Enhance with Risk-Based Tests:
   - Add specific high-risk combinations
   - Add edge cases not covered by pairwise

5. Execute and Analyze:
   - Track defects by parameter interaction
   - If defects found, consider higher strength (3-way)
```

## Common Test Design Patterns

### Pattern 1: Smoke Test Suite

**Purpose**: Quick confidence check that major functionality works.

**Design**:
- Select critical paths through system
- One happy-path test per major feature
- Fast execution (<10 minutes ideal)
- High-value, low-maintenance tests

**When to Use**: After build, before deeper testing

**Example** - E-commerce:
- User can log in
- User can search for product
- User can add item to cart
- User can complete checkout

### Pattern 2: Regression Test Suite

**Purpose**: Verify that existing functionality still works after changes.

**Design**:
- Cover previously stable features
- Include tests for past defects (prevent re-occurrence)
- Prioritize by risk and change frequency
- Balance coverage vs execution time

**Maintenance**:
- Remove obsolete tests
- Update for requirement changes
- Keep execution time reasonable

### Pattern 3: End-to-End Scenarios

**Purpose**: Validate complete user workflows.

**Design**:
- Reflect realistic user journeys
- Include multiple features/components
- Test integration points
- Cover common use cases

**Example** - Banking:
1. User logs in
2. User transfers money between accounts
3. User views transaction history
4. User logs out

**Tips**:
- Keep scenarios independent (don't chain)
- Test both success and failure paths
- Consider different user roles/personas

### Pattern 4: Boundary Sweep

**Purpose**: Systematically test all boundaries in the system.

**Design**:
1. List all inputs with ranges
2. For each range, test: min-1, min, min+1, max-1, max, max+1
3. For collections, test: empty, one item, max capacity, over capacity
4. For dates, test: start of range, end of range, leap year, timezone changes

**Example** - Shopping Cart:
- 0 items (empty cart)
- 1 item
- Max items - 1
- Max items
- Max items + 1

### Pattern 5: Configuration Matrix

**Purpose**: Test product across different configurations.

**Design**:
1. Identify configuration dimensions (OS, browser, language, device)
2. Use pairwise testing to reduce combinations
3. Add specific high-risk or high-usage configurations
4. Document compatibility matrix

**Example** - Web Application:
```
Pairwise coverage of:
- Browser: Chrome, Firefox, Safari, Edge
- OS: Windows, Mac, Linux
- Language: English, Spanish, Chinese
- Screen Size: Mobile, Tablet, Desktop

Results in ~15-20 configurations instead of 4×3×3×3 = 108
```

## Tips for Effective Test Design

### General Principles

1. **Start with Risk**: Focus on what matters most
2. **Think Like a User**: How will they actually use it?
3. **Think Like an Attacker**: How could they break it?
4. **Diversify Techniques**: Combine multiple approaches
5. **Keep It Simple**: Maintainability matters
6. **Document Intent**: Future you will thank you
7. **Iterate**: Test design improves over time

### Coverage Goals

**Aim for Balance**:
- **Breadth**: Cover all features lightly
- **Depth**: Test critical features thoroughly
- **Edge Cases**: Boundaries and error conditions
- **Integration**: How pieces work together

**Don't Aim for 100%**:
- 100% coverage is expensive and often impossible
- Diminishing returns
- Focus on valuable coverage
- Use risk to prioritize

### Collaboration

**Involve Others**:
- **Developers**: Review test design, share code insights
- **Business Analysts**: Validate scenarios, clarify requirements
- **Users**: Provide real-world context
- **Other Testers**: Peer review, pair testing

**Three Amigos** (Agile Pattern):
- Developer + Tester + Business Representative
- Review user stories together before development
- Design acceptance tests collaboratively
- Clarify requirements and edge cases

### Continuous Improvement

**Retrospect on Testing**:
- Which techniques found the most defects?
- Which tests were most valuable?
- Which tests were wasted effort?
- What did we miss?

**Maintain Test Assets**:
- Remove obsolete tests
- Refactor confusing tests
- Update for new patterns learned
- Share knowledge across team

## Quick Reference: When to Use Which Technique

| Situation | Recommended Techniques |
|-----------|----------------------|
| Multiple input fields with ranges | Equivalence Partitioning + Boundary Value Analysis |
| Complex business rules | Decision Tables |
| Workflow with states | State Transition Testing |
| User scenarios | Use Case Testing |
| Many configuration options | Pairwise (Combinatorial) Testing |
| New feature, learning as you go | Exploratory Testing |
| Known error-prone areas | Error Guessing + Checklist |
| Regression after bug fix | Re-test defect + nearby areas |
| Critical business transaction | End-to-End Scenarios + Risk-Based Testing |
| Integration between systems | Interface testing + Error Guessing |
| Time-sensitive functionality | State Transition + Boundary Value (time) |
| Accessibility requirements | Checklist-Based + Heuristic Evaluation |

## Resources and Further Learning

**Key Frameworks**:
- ISTQB Foundation Level Syllabus (test design techniques)
- BBST Courses (test design, bug advocacy, foundations)
- Heuristic Test Strategy Model (James Bach, Satisfice)
- NIST Combinatorial Testing (pairwise and covering arrays)

**Recommended Reading**:
- "Lessons Learned in Software Testing" - Kaner, Bach, Pettichord
- "Explore It!" - Elisabeth Hendrickson
- "Perfect Software and Other Illusions About Testing" - Gerald Weinberg
- "Agile Testing" - Lisa Crispin, Janet Gregory

**Online Resources**:
- Satisfice.com (James Bach's heuristics and models)
- BBST.courses (free course materials)
- ISTQB.org (certification and syllabi)
- NIST ACTS tool (combinatorial testing)

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Focus**: Non-technical test design - the intellectual work of creating effective tests
