import asyncio
from agents import BaseAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

async def main():
    Alice = BaseAgent("Alice", "Researcher", api_key)
    Bob =  BaseAgent("Bob", "Researcher", api_key)
    James = BaseAgent("James", "Manager", api_key)

    results = await asyncio.gather(Alice.execute_research("Quantum Computing"), Bob.execute_research("Artigicial Intelligence"))
    
    final_output =  await James.compile_report(results)


    print(final_output)


asyncio.run(main()) 