import openai

openai.api_key = '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'

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]


async def chat(user_input: str):
    conversation_history.append({"role": "user", "content": user_input})

    chat_input = "\n".join(f"{msg['role']}: {msg['content']}" for msg in conversation_history)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chat_input,
        max_tokens=150  # You can adjust the response length as needed
    )

    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return response.choices[0].text.strip()
