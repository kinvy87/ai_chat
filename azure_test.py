import openai
openai.api_type = "azure"
openai.api_base = "https://bjzkjuk.openai.azure.com/"
openai.api_version = "2023-08-01-preview"
openai.api_key = "c2dd7174b09044f0b693f9b8a893af3d"

## gpt35_16k

response = openai.ChatCompletion.create(
    # engine="gpt35_16k", # engine = "deployment_name".
    engine="gpt4_turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
#         {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
#         {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
#     ]
# )

    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "树上七只鸟，开枪打死了一只，还有几只"},
    ]
)

print(response)
print(response['choices'][0]['message']['content'])