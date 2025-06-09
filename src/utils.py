"""
Utility functions for the project
"""

def greet(name: str) -> str:
    """
    Greet someone by name
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting message
    """
    message = f"Hello, {name}! 🚀"
    print(message)
    return message

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b
