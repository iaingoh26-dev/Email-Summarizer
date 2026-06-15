**AI Email Summarizer**
A lightweight Python script that leverages OpenAI's GPT models to automatically summarize emails, extract action items, and identify sender intent.


**Features**
Smart Summarization – Condenses lengthy emails into 2-3 concise sentences

Action Item Extraction – Identifies deadlines, tasks, and required responses

Intent Detection – Classifies emails as informational, requests, or follow-ups

Secure API Handling – Uses environment variables for API key management

Customizable Prompts – Easily modify the system prompt to fit different use cases


**Tech Stack**
-Python 3.x
-OpenAI API (GPT-4.1 Nano)

 **How It Works**
The script sends a system prompt defining the AI's role, along with a raw email, to OpenAI's API. The model returns:

1.A concise 2-3 sentence summary

2.Any action items or deadlines found

3.The sender's intent (inform / request / follow-up)
