import openai

openai.api_key = "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"


while True:
    prompt = input("you : ")
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)

    generated_text = response.choices[0].text
    print(generated_text)