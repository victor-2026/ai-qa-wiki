# Prompts from "Software Testing with Generative AI"

**Author:** Mark Winteringham
**Source:** [GitHub](https://github.com/mwinteringham/generative-ai-and-testing)
**Book:** Software Testing with Generative AI (Manning, 2025)

---

## Chapter 2: Prompt Engineering Principles

### Principle 1: Write Clear and Specific Instructions

#### Use Delimiters
```
Analyze the following code:
---
[code here]
---
Return a JSON object with:
- complexity score
- potential bugs
- suggestions
```

#### Ask for Structured Output
```
Generate test cases for:
User login functionality

Return in Markdown table with columns:
| Test ID | Input | Expected Output | Priority |
```

#### Check for Assumptions
```
Review this API response handling:
[code]

Identify any assumptions being made that could fail.
```

#### Few-Shot Prompting
```
Example 1:
Input: "Login with wrong password"
Output: "Should show error message"

Example 2:
Input: "Login with empty field"
Output: "Should show validation error"

Now analyze:
[user's input]
```

### Principle 2: Give the Model Time to "Think"

#### Specify Steps
```
To analyze this feature request:

Step 1: Identify key user stories
Step 2: List acceptance criteria
Step 3: Suggest edge cases
Step 4: Recommend test approaches

Feature: [description]
```

#### Instruct to Work Out Solution First
```
Don't jump to conclusions. First work through the logic:

1. What is the expected behavior?
2. What edge cases exist?
3. What could go wrong?

Then provide your analysis of:
[test scenario]
```

---

## Chapter 4: AI-Assisted Testing for Developers

### Code Analysis Prompt
```
As a senior tester, analyze this code for testability:

[paste code]

Consider:
- What dependencies need mocking?
- What side effects exist?
- What would you need to test this?
```

### TDD Loop Prompt
```
Help me practice TDD with this feature:

Feature: [description]

Step 1: Write a failing test
Step 2: Write minimal code to pass
Step 3: Refactor

Guide me through each step.
```

### Documentation Generation
```
Generate documentation for:

Code: [paste code]

Include:
- Purpose
- Parameters
- Return values
- Side effects
- Example usage
```

---

## Chapter 5: Test Planning with AI

### Test Planning Model
```
Based on this user story:

[story]

Create a test planning model that includes:
1. Prompts for identifying risks
2. Prompts for generating test conditions
3. Prompts for creating test cases
```

### Risk Identification
```
Analyze these requirements for testing risks:

[requirements]

Identify:
- Functional risks
- Non-functional risks
- Integration risks
- Edge cases

For each risk, suggest a testing approach.
```

---

## Chapter 6: Rapid Data Creation

### Data Generation Prompt
```
Generate test data for:

Table: Users
Fields: name, email, age, registration_date

Requirements:
- 10 records
- Mix of valid and invalid email formats
- Age range 18-80
- Dates in 2024

Return as SQL INSERT statements.
```

### Data Transformation
```
Transform this test data from JSON to CSV:

[JSON data]

Maintain referential integrity.
```

### SQL Export as Prompt Guide
```
Given this SQL schema:

[schema]

Generate realistic test data that:
- Covers normal cases
- Includes boundary values
- Has some invalid data for error testing
```

---

## Chapter 7: UI Automation with AI

### Page Object Pattern Prompt
```
Analyze this web page and suggest a Page Object model:

URL: [description]

Identify:
- Key page elements
- Common actions
- Page-specific methods
```

### Test Script Generation
```
Generate Playwright test for:

Action: Login with valid credentials
Page: [description]

Include:
- Element locators (prioritize data-testid)
- Assertions
- Error handling
```

---

## Chapter 8: Exploratory Testing

### Charter Augmentation
```
Augment this exploratory charter:

Current: [charter]

Add:
- Risks to explore
- Questions to investigate
- Data requirements
- Success criteria
```

### Session Note Summarization
```
Summarize these testing notes into:
1. Key findings
2. Bugs discovered
3. Risks identified
4. Recommendations

Notes:
[paste notes]
```

---

## Chapter 9: AI Agents

### Agent Setup
```
Design an AI agent for:

Task: [description]

Include:
- Core functions/tools
- Decision logic
- Error handling
- Human oversight points
```

### Tool Chaining
```
Design a tool chain for:

Workflow: [description]

Each step should:
- Have clear input/output
- Include validation
- Handle failures gracefully
```

---

## Chapter 11: RAG for Testing

### RAG System Design
```
Design a RAG system for:

Context: [testing domain]

Components:
- Embedding strategy
- Vector store structure
- Retrieval approach
- Response generation
```

---

## Chapter 12: Fine-Tuning

### Fine-Tuning Approach
```
For testing domain: [description]

Recommend:
- Base model
- Training data approach
- Evaluation metrics
- When to use fine-tuning vs RAG
```

---

## General Prompt Library Structure

Based on Winteringham's approach:

```
prompts/
├── planning/
│   ├── risk-identification.md
│   ├── test-case-generation.md
│   └── test-data-creation.md
├── execution/
│   ├── code-analysis.md
│   ├── test-automation.md
│   └── exploratory-notes.md
├── evaluation/
│   ├── result-analysis.md
│   └── regression-checks.md
└── reporting/
    ├── test-summary.md
    └── bug-report.md
```

---

## Related

- [[raw/software-testing-with-generative-ai]] — Book reference
- [[wiki/qa-prompt-engineering-guide]] — More prompt patterns
- [[wiki/agentic-patterns]] — AI agents
