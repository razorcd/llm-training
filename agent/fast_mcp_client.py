from fastmcp import Client

import asyncio

async def main():
    async with Client("fast_mcp_demo.py") as client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        
        # Execute operations
        await client.call_tool("set_weather", {"city": "Bremen", "temp": 55})
        result = await client.call_tool("get_weather", {"city": "Bremen"})
        print(result)

if __name__ == "__main__":
    test = asyncio.run(main())
