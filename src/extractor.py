from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Extractor")

@mcp.tool()
async def test()-> None:
    pass