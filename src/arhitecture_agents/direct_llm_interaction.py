from openai import OpenAI
 
client = OpenAI()

response = client.chat.completions.create()
    model="gpt-4",
    messages=[
        {"role": "user", "content": "What is the capital of Canada?"}
    ]
)

print(response.choices[0].message.content)