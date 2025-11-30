# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# # Load API Key from environment variable
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=OPENAI_API_KEY)


# def generate_text(prompt: str) -> str:
#     """
#     Sends a prompt to OpenAI and returns the model response.
#     """
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return response.choices[0].message["content"]

# ----------------
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found in environment variables!")

# client = OpenAI(api_key=OPENAI_API_KEY)

# def generate_text(prompt: str) -> str:
#     try:
#         response = client.chat.completions.create(
#             model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         return response.choices[0].message["content"]
#     except Exception as e:
#         print("OpenAI API Error:", e)
#         raise e
# ----------------


import os

MOCK_MODE = os.getenv("MOCK_MODE", "true").lower() == "true"

def generate_text(prompt: str) -> dict:
    """
    Generate AI text using OpenAI or mock response.
    Always returns a dict so FastAPI can serialize without errors.
    """
    if MOCK_MODE:
        # Safe mock response
        return {"text": f"[MOCK RESPONSE] You asked: '{prompt}' and AI replies with a reversed string: '{prompt[::-1]}'"}

    # Real OpenAI call
    try:
        import openai
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not set in environment variables!")

        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return {"text": response.choices[0].message.content}

    except Exception as e:
        # Catch all exceptions to avoid FastAPI 500
        print("Error in generate_text:", e)
        return {"text": f"[ERROR] {str(e)}"}
