from openai import OpenAI

client = OpenAI()

# for gpt-3.5-turbo
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a coding and programming assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Write a python program to print all the prime numbers between 0-100"}
    ]
)

# Extract and print the message from the completion
response_message = completion.choices[0].message.content
print(response_message)
