# built-in libraries
from datetime import datetime, time

# third-party libraries
from typing import Optional, List
from pydantic import BaseModel



class Agent(BaseModel):

    agent_id: Optional[str]
    agent_name: Optional[str]
    agent_team: Optional[str]

    class Config:
        orm_mode = True