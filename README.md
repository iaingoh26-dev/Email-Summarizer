# AI Email Summarizer using OpenAI API

## Overview

This project is a simple AI-powered email summarization tool built using Python and the OpenAI API. It processes email content and generates concise summaries while extracting action items, deadlines, and the sender's intent.

The goal of this project is to demonstrate prompt engineering, API integration, and practical applications of Large Language Models (LLMs) in automating everyday business tasks.

---

## Features

- Generates concise 2–3 sentence email summaries
- Extracts action items and important deadlines
- Identifies sender intent:
  - Inform
  - Request
  - Follow-up
- Uses structured prompts for consistent outputs
- Integrates directly with the OpenAI API

---

## Technologies Used

- Python
- OpenAI API
- Prompt Engineering
- Environment Variables for API Key Management

---

## How It Works

1. Configure the OpenAI API key using environment variables.
2. Define a system prompt that instructs the AI on how to process emails.
3. Pass email content as a user prompt.
4. Send the prompts to the OpenAI model.
5. Receive and display a structured summary.

---

## Sample Input

```text
Hi iaingoh1,

We are pleased to inform you that #260505JWQW8CYR has been delivered.

Please confirm and accept the order in the Shopee App. Once you confirm, payment will be made to bamnatural.

ORDER DETAILS

Order ID: #260505JWQW8CYR
Order Date: 05/05/2026 11:20:15
Seller: bamnatural
```

## Sample Output

```text
Summary:
The seller has informed the customer that the order has been successfully delivered. The customer is requested to confirm receipt through the platform so payment can be released to the seller.

Action Items:
- Confirm receipt of the order in the application.
- Record an unboxing video or take photos of the package for potential return or refund requests.

Sender Intent:
Inform / Request
```

---

## Skills Demonstrated

- API Integration
- Prompt Engineering
- Large Language Model (LLM) Applications
- Text Processing
- Python Programming
- Environment Variable Management
- AI-Assisted Workflow Automation

---

## Key Learning Outcomes

Through this project, I gained hands-on experience with:

- Designing effective system prompts
- Structuring conversations for chat-based AI models
- Integrating external AI services into Python applications
- Building practical productivity tools using generative AI

---
---

## Challenges Encountered

### 1. Prompt Consistency

One of the initial challenges was ensuring that the AI generated responses in a consistent format. Early prompts sometimes produced summaries that varied in structure, making it difficult to reliably extract information such as action items and sender intent.

**Solution:**  
A structured system prompt was implemented to clearly define the expected output format, improving response consistency across different email types.

### 2. Handling Different Email Formats

Emails can vary significantly in structure, ranging from formal business messages to automated notifications and promotional content. Some emails contained excessive metadata or formatting that could affect summary quality.

**Solution:**  
The prompts were refined to focus on the most relevant content while ignoring unnecessary details, allowing the model to generate more concise and useful summaries.

### 3. API Configuration and Authentication

During development, managing API credentials securely was a challenge. Hardcoding API keys poses security risks and is not considered best practice.

**Solution:**  
Environment variables were used to store API credentials securely, preventing sensitive information from being exposed in the source code.

### 4. Selecting an Appropriate AI Model

Different OpenAI models offer varying trade-offs between response quality, speed, and cost. Choosing the right model required experimentation and evaluation.

**Solution:**  
Several models were tested before selecting a lightweight model that provided an acceptable balance between performance and efficiency for email summarization tasks.

### 5. Managing Token Limits

Long emails may exceed context limits or increase API usage costs. This became apparent when testing with larger email bodies and threads.

**Solution:**  
The project was designed around concise email inputs, and future improvements include implementing text chunking and preprocessing techniques to handle larger documents efficiently.

---

## Future Improvements

- Process multiple emails in batches
- Export summaries to PDF or Excel
- Add a graphical user interface (GUI)
- Support email ingestion directly from Gmail or Outlook
- Implement sentiment analysis and priority scoring

---

## Author

Developed as a learning project to explore practical applications of Generative AI and OpenAI APIs in business communication workflows.




