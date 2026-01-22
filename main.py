from browser_use import Agent, Browser, BrowserConfig, ChatAnthropic
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def example():
    browser = Browser(
        config=BrowserConfig(use_cloud=True)  # Use stealth browser on Browser Use Cloud
    )

    llm = ChatAnthropic(model="claude-sonnet-4-20250514")

    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())
