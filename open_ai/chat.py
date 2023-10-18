import openai

openai.api_key = 'YOUR_API_KEY'
messages = [{"role": "system", "content":
             "You are a intelligent assistant."}]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        response = openai.Completion.create(
            engine="text-davinci-003",
            messages=messages
        )
        reply = response.choices[0].message['content']['content']
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

