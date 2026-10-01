import streamlit as st
from openai import OpenAI


def get_api_key():

    return st.secrets["GROQ_API_KEY"]


def get_client():

    return OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=get_api_key()
    )


def generate_response(system_prompt, user_prompt):

    client = get_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content