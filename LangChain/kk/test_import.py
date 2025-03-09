# Test script to verify langchain_experimental.utilities import
try:
    from langchain_experimental.utilities import TavilySearchAPIWrapper

    print("Import successful!")
    print(f"TavilySearchAPIWrapper: {TavilySearchAPIWrapper}")
except ImportError as e:
    print(f"Import failed: {e}")

    # Try alternative import
    try:
        from langchain_community.utilities import TavilySearchAPIWrapper

        print("Alternative import successful!")
        print(f"TavilySearchAPIWrapper from community: {TavilySearchAPIWrapper}")
    except ImportError as e:
        print(f"Alternative import failed: {e}")
