from functions.call_function import available_functions, call_function
from google.genai import types



def get_function_call_by_model(client, messages, system_prompt="", verbose=False):
    # Call the client with user prompt and history
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],
                                           system_instruction=system_prompt),
    )
    
    # Result: if --verbose, print user prompt and token usage data
    if verbose:
        print(f'User prompt: {messages[-1]}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
        
    
    # List of function calls
    function_call_results = []
        
    # Run functions used OR otherwise print response
    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=verbose)
            if not function_call_result.parts:
                raise Exception(f"Error: called function {function_call.name} but got no result")
            response = function_call_result.parts[0].function_response
            if not response:
                raise Exception(f"Error: called function {function_call.name} but got empty response")
            
            function_call_results.append(function_call_result.parts[0])
            
            if verbose:
                print(f"-> {response}")
                
    else:
        print(f'Response: {response.text}')
        
        
    return function_call_results
