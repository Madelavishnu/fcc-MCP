from fastmcp import FastMCP

from langchain.utilities.dalle_image_generator import DallEAPIWrapper

mcp1 = FastMCP("image-mcp")

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


@mcp1.tool()
def generate_image(prompt: str) -> str:
    """Generate an image from text prompt and return image URL."""
    dalle = DallEAPIWrapper()
    img_url = dalle.run(prompt)
    return img_url

@mcp1.prompt()
def image_assistant():
    return "You can generate images using the generate_image tool when user asks."
if __name__ == "__main__":
    mcp.run(transport="http", host = "127.0.0.1", port = "8005")
