def final_value_after_operations(operations):
    
    # Initialize the variable
    final_answer = 0
    # Iterate through each operation
    for operation in operations:
        if operation == "++X" or operation == "X++":
            final_answer += 1
        elif operation == "--X" or operation == "X--":
            final_answer -= 1
            
    return final_answer

# Example usage
operations = ["++X", "X++", "--X", "X--", "X++", "X++", "--X","++X", "X++", "X--"]
result = final_value_after_operations(operations)
print("Final value of our asnwer is :", result)
