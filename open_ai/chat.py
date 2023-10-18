import openai

openai.api_key = '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'

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        break

    conversation_history.append({"role": "user", "content": user_input})

    # Format conversation history as a single string
    messages = [{"role": role, "content": content} for role, content in conversation_history]
    chat_input = "\n".join(f"{msg['role']}: {msg['content']}" for msg in messages)

    # Generate a response from the AI model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chat_input,
        max_tokens=150  # You can adjust the response length as needed
    )

    print(response)

    # Extract and print the assistant's reply
    assistant_reply = response.choices[0].text.strip()
    print(f"ChatGPT: {assistant_reply}")

    # Store the assistant's reply in the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_reply})
