import openai
import os

# Step 1: Configure API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 2: Define prompts
system_prompt = """You are an expert email summarizer. For every email you receive:
1. Write a 2-3 sentence summary
2. Extract any action items or deadlines
3. Identify the sender's intent (inform / request / follow-up)
Be concise and professional."""
user_prompt = """Summarize this email: 

[
Hi iaingoh1,
 
We are pleased to inform you that #260505JWQW8CYR has been delivered.

Please confirm and accept the order in the Shopee App. Once you confirm, payment will be made to bamnatural. If we don’t hear from you, the payment will be automatically transferred.

In order to capture any defects on the parcel or products, please perform an unboxing video and/or take pictures or videos of the packaging and condition of the received product to ease the review process if any return refund request was raised.
 
 
 
 
ORDER DETAILS
 
 
Order ID:	#260505JWQW8CYR
Order Date:	05/05/2026 11:20:15
Seller:	bamnatural
 ]
"""

# Step 3: Make the messages list
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Step 4: Call OpenAI
response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

# Step 5: Print the result
print(response.choices[0].message.content)