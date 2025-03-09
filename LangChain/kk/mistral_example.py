"""
Example of using ChatMistralAI with LangChain

This example demonstrates how to use the ChatMistralAI class from langchain_mistralai
instead of trying to import MistralLLM which doesn't exist.
"""

import os
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage

# Set your Mistral API key
# You can get one from https://console.mistral.ai/
# os.environ["MISTRAL_API_KEY"] = "your-api-key-here"


def main():
    # Initialize the ChatMistralAI model
    # Note: We're using ChatMistralAI, not MistralLLM
    chat = ChatMistralAI(
        model="mistral-small-latest",  # You can also use other models like "mistral-medium-latest" or "mistral-large-latest"
        temperature=0.7,
    )

    # Create messages
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="What is the capital of France?"),
    ]

    # Get a response
    response = chat.invoke(messages)

    print("Response:")
    print(response.content)

    # You can also use it in a more conversational way
    print("\nConversational example:")

    # Start a conversation
    messages = [
        SystemMessage(
            content="You are a helpful AI assistant specialized in Python programming."
        )
    ]

    # First user message
    messages.append(HumanMessage(content="How do I read a file in Python?"))
    response = chat.invoke(messages)
    print("User: How do I read a file in Python?")
    print(f"AI: {response.content}")

    # Add the response to the conversation history
    messages.append(response)

    # Second user message
    messages.append(
        HumanMessage(content="How would I modify that to read only the first 10 lines?")
    )
    response = chat.invoke(messages)
    print("\nUser: How would I modify that to read only the first 10 lines?")
    print(f"AI: {response.content}")


if __name__ == "__main__":
    main()
