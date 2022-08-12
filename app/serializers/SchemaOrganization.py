# built-in libraries
from datetime import datetime, time

# third-party libraries
from typing import Optional, List
from pydantic import BaseModel



class Organization(BaseModel):
    organization_id: Optional[str]
    organization_name: Optional[str]

    class Config:
        orm_mode = True