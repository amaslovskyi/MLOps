"""
Test script for Tavily API key functionality
"""

import os
import getpass
from dotenv import load_dotenv

# Try to load from .env file
load_dotenv()


def get_tavily_api_key():
    """Get Tavily API key from environment or prompt user"""
    key = os.getenv("TAVILY_API_KEY")
    print(f"Key from environment: {'Found' if key else 'Not found'}")

    if not key:
        print("Please enter your Tavily API key when prompted:")
        key = getpass.getpass("Enter your TAVILY API key: ")
        os.environ["TAVILY_API_KEY"] = key

    return key


if __name__ == "__main__":
    # Clear the key from environment for testing
    if "TAVILY_API_KEY" in os.environ:
        print("Removing existing TAVILY_API_KEY from environment for testing")
        del os.environ["TAVILY_API_KEY"]

    # Get the key (should prompt)
    tavily_api_key = get_tavily_api_key()
    print(f"Tavily API key status: {'Set' if tavily_api_key else 'Not set'}")

    # Try to use the key with Tavily
    try:
        from langchain_community.tools.tavily_search import TavilySearchResults

        print("\nCreating Tavily search tool...")
        search_tool = TavilySearchResults()

        print("Testing Tavily search...")
        search_results = search_tool.invoke({"query": "Latest developments in AI"})
        print("Search successful!")
        print(search_results[:2])  # Print first 2 results
    except ImportError:
        print(
            "Could not import TavilySearchResults. Make sure langchain_community is installed."
        )
    except Exception as e:
        print(f"Error using Tavily search: {e}")
