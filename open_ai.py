from openai import OpenAI
client = OpenAI(api_key="sk-4NwYzHRgVbEY1ptK6dE21fF47dDc47C2Bf8324D32c36F5A6")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"四大文明古国分别有哪些",}
    ]
)