from pydantic import BaseModel, Field
from typing import List, Dict

class Task(BaseModel):
    id: int
    description: str
    dependencies: List[int] = Field(default_factory=list)
    tool_required: str
    status: str = "Pending"
    timeline: str = ""

class ExecutionPlan(BaseModel):
    goal: str
    tasks: List[Task]
    reasoning: str
    resource_checks: List[str] = Field(default_factory=list)

class MarketingPlanner:
    def __init__(self, goal: str):
        self.goal = goal
        self.plan = None

    def format_plan_output(self, plan: ExecutionPlan):
        output = f"\n{'='*50}\n"
        output += f"STRUCTURED EXECUTION PLAN: {plan.goal}\n"
        output += f"{'='*50}\n\n"
        output += f"REASONING:\n{plan.reasoning}\n\n"
        output += "RESOURCE CHECKS:\n"
        for check in plan.resource_checks:
            output += f"- {check}\n"
        output += "\nTASK LIST:\n"
        for task in plan.tasks:
            deps = f" (Depends on: {task.dependencies})" if task.dependencies else ""
            output += f"[{task.id}] {task.description} - Tool: {task.tool_required}{deps}\n"
        
        # Timeline will be populated by the SchedulerTool usually, 
        # but the agent will integrate it into the plan objects.
        return output
