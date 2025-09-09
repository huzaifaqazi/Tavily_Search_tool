from agents import  AsyncOpenAI , OpenAIChatCompletionsModel , OpenAIResponsesModel
from decouple import config

api  = config('openai')
base = config("base_url")
model = config("openai_model")

client = AsyncOpenAI(
    api_key=api,
    # base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    base_url=base
)

model = OpenAIResponsesModel(
    # model="gemini-2.5-flash",
    model=model,
    openai_client=client
)

