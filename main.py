import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from config import MAX_LOOPS
from functions.call_function import available_functions, call_function
from functions.get_function_call_by_model import get_function_call_by_model


def main():
    # Load environmental variables, api_key includad
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("environment variable api_key not found")
    
    # Initialize Gemini client
    client = genai.Client(api_key=api_key)
    
    # FIRST CALL: MADE BY USER
    # Parse Python arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    # First argument is user prompt
    parser.add_argument("user_prompt", type=str, help="User prompt")
    # Second argument is --verbose option
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    # Add current user prompt to message history
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]    
    
    function_call_result = None
    
    # call the model, handle responses, etc.
    for _ in range(MAX_LOOPS):
        function_call_result = get_function_call_by_model(client, messages, system_prompt, args.verbose)
        
        if not function_call_result["function_called"]:
            break
        
        messages = function_call_result["messages"]
        
    
    if function_call_result and function_call_result["function_called"]:
        print("Model couldn't reach a final response in the determined max calls amount")
        sys.exit(1)
    
        
        
    
        
        
    

if __name__ == "__main__":
    main()
