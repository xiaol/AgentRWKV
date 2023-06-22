from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field, validator

from reworkd_platform.web.api.agent.analysis import Analysis

LLM_Model = Literal[
    "RWKV-world-7B",
    "gpt-3.5-turbo-16k",
    "gpt-4",
]

Loop_Step = Literal[
    "start",
    "analyze",
    "execute",
    "create",
]

LLM_MODEL_MAX_TOKENS: Dict[LLM_Model, int] = {
    "RWKV-world-7B": 4000,
    "gpt-3.5-turbo-16k": 16000,
    "gpt-4": 8000,
}


class ModelSettings(BaseModel):
    model: LLM_Model = Field(default="RWKV-world-7B")
    custom_api_key: str = Field(default="")
    temperature: float = Field(default=1.5, ge=0.0, le=2.0)
    max_tokens: int = Field(default=500, ge=0)
    language: str = Field(default="English")

    @validator("max_tokens")
    def validate_max_tokens(cls, v: float, values: dict) -> float:
        if v > (model := LLM_MODEL_MAX_TOKENS[values["model"]]):
            raise ValueError(
                f"Model {values['model']} only supports {LLM_MODEL_MAX_TOKENS[model]} tokens"
            )

        return v


class AgentRunCreate(BaseModel):
    goal: str
    model_settings: ModelSettings = Field(default=ModelSettings())


class AgentRun(AgentRunCreate):
    run_id: str


class AgentTaskAnalyze(AgentRun):
    task: str
    tool_names: List[str] = Field(default=[])
    model_settings: ModelSettings = Field(default=ModelSettings())


class AgentTaskExecute(AgentRun):
    task: str
    analysis: Optional[Analysis] = None  # TODO Why is this optional?


class AgentTaskCreate(AgentRun):
    tasks: List[str] = Field(default=[])
    last_task: Optional[str] = Field(default=None)
    result: Optional[str] = Field(default=None)
    completed_tasks: List[str] = Field(default=[])


class NewTasksResponse(BaseModel):
    run_id: str
    new_tasks: List[str] = Field(alias="newTasks")


class RunCount(BaseModel):
    count: int
    first_run: Optional[datetime]
    last_run: Optional[datetime]


class UserBase(BaseModel):
    id: str
    name: Optional[str]
    email: Optional[str]
