#Exercise 2

# The OpenAI SDK was updated on Nov 8, 2023 with new guidance for migration
# See: https://github.com/openai/openai-python/discussions/742

## Updated
import os
import openai
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

## Updated
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens=1024
    )
    return response.choices[0].message.content

## ---------- Call the helper method

### 1. Set primary content or prompt text
text = f"""
oh say can you see
"""

### 2. Use that in the prompt template below
prompt = f"""
```{text}```
"""

## 3. Run the prompt
response = get_completion(prompt)
print(response)