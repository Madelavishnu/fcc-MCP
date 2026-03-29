from fastmcp import FastMCP

mcp = FastMCP(name ="calculatormcp")

@mcp.tool()
def multiply(a:float,b:float) -> float:
    """Multiply two numbers.
    
    args: a (float): The first number.
          b (float): The second number.
          
    returns: float: The product of the two numbers.
    """
    return a*b


@mcp.tool()
def add(a:float,b:float) -> float:
    """Add two numbers.
    
    args: a (float): The first number.
          b (float): The second number.
          
    returns: float: The sum of the two numbers.
    """
    return a+b

if __name__ == "__main__":
    mcp.run(transport="http")
