import asyncio
from models import ResearchTask
from groq import AsyncGroq
from utils import performance_logger


class BaseAgent:
    def __init__(self, name, role, api_key):
        self.name = name
        self.role = role
        self.client = AsyncGroq(api_key=api_key)

    TASK_MAPPING = {
        "Researcher": "Research",
        "Manager": "Compilation"
    }    


    @performance_logger
    async def execute_research(self, topic):
        
        completion = await self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a professional researcher. Give a concise 1-sentence summary."},
                {"role": "user", "content": f"Research this topic: {topic}"}
            ]
        )
        
        live_content = completion.choices[0].message.content
        
        
        return ResearchTask(
            task_id=1,
            topic=topic,
            priority=5,
            content=live_content
        )
    

    @performance_logger
    async def compile_report(self, entire_data):
        
        raw_context = "\n\n".join([f"TOPIC: {i.topic}\nCONTENT: {i.content}" for i in entire_data])

        
        completion = await self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system", 
                    "content": "You are an Executive Manager. Summarize the research findings into a polished, professional Markdown report. Use clear headings, bold text, and a concluding synthesis."
                },
                {
                    "role": "user", 
                    "content": f"Please summarize these research findings:\n\n{raw_context}"
                }
            ]
        )
        
       
        return completion.choices[0].message.content
     