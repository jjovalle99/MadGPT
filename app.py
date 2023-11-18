import chainlit as cl
import openai
from chainlit.playground.providers import ChatOpenAI
from chainlit.prompt import Prompt, PromptMessage

client = openai.AsyncOpenAI()
settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 200,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "seed": 1399,
}
sys_template = "You are a helpful assistant who always speaks in a rude tone!"
user_template = """{input}
Think through your response step by step."""  # Add Chain of Thought


@cl.on_chat_start
async def start_chat():
    cl.user_session.set("settings", settings)


@cl.on_message
async def main(message: cl.Message):
    settings = cl.user_session.get("settings")

    prompt = Prompt(
        provider=ChatOpenAI.id,
        messages=[
            PromptMessage(
                role="system",
                template=sys_template,
                formatted=sys_template,
            ),
            PromptMessage(
                role="user",
                template=user_template,
                formatted=user_template.format(input=message.content),
            ),
        ],
        inputs={"input": message.content},
        settings=settings,
    )

    print([message.to_openai() for message in prompt.messages])
    message = cl.Message(content="")

    stream = await client.chat.completions.create(
        messages=[message.to_openai() for message in prompt.messages],
        stream=True,  # Stream mode
        **settings
    )

    async for part in stream:
        token = part.choices[0].delta.content or ""  # Stream mode
        await message.stream_token(token)

    prompt.completion = message.content
    message.prompt = prompt

    await message.send()
