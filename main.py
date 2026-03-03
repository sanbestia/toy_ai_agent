import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import available_functions


def main():
    # Load environmental variables, api_key includad
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("environment variable api_key not found")
    
    # Initialize Gemini client
    client = genai.Client(api_key=api_key)
    
    # Parse Python arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    # First argument is user prompt
    parser.add_argument("user_prompt", type=str, help="User prompt")
    # Second argument is --verbose option
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # Add current user prompt to message history
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]    
    
    # Call the client with user prompt and history
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],
                                           system_instruction=system_prompt),
    )
        
    # Result: if --verbose, print user prompt and token usage data
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    # Always print functions used OR otherwise normal response
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f'Response: {response.text}')


if __name__ == "__main__":
    main()
