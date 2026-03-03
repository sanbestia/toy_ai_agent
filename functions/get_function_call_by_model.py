from functions.call_function import available_functions, call_function
from config import MODEL
from google.genai import types


def get_function_call_by_model(client, messages, system_prompt="", verbose=False):
    """
    Run functions that the model proposes and save them to the previous history of messages.
    Returns a dict with two key/value pairs: the new history and whether a function has been run during the call
    """
    
    # Call the client with user prompt and history
    response = client.models.generate_content(
        model=MODEL,
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],
                                           system_instruction=system_prompt),
    )
    
    # Result: if --verbose, print user prompt and token usage data
    if verbose:
        print(f'User prompt: {messages[-1]}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
        
    
    # 1st part: We'll return the response of the model as part of the message history
    new_messages = messages.copy()
    for candidate in response.candidates:
        new_messages.append(candidate.content)
    
    # List of function calls
    function_call_results = []
        
    # Run functions used OR otherwise print response
    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=verbose)
            if not function_call_result.parts:
                raise Exception(f"Error: called function {function_call.name} but got no result")
            function_response = function_call_result.parts[0].function_response
            if not function_response:
                raise Exception(f"Error: called function {function_call.name} but got empty response")
            
            function_call_results.append(function_call_result.parts[0])
            
            if verbose:
                print(f"-> {function_response}")
                
    else:
        # If there has been no function call
        print(f'Response: {response.text}')
        
        
    # 2nd part: We'll return the response of the model as part of the message history
    new_messages.append(types.Content(role="user", parts=function_call_results))
    
    
    ret_value = {"messages": new_messages, "function_called": response.function_calls != None}
    return ret_value
