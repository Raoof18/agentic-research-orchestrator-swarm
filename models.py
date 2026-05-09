from pydantic import BaseModel, Field

class ResearchTask(BaseModel):
    task_id: int
    topic: str
    priority: int = Field(gt=0, le=10)
    content: str