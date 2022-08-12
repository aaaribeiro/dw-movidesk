# built-in libraries
from datetime import datetime, time
from typing import Optional, List
# third-party libraries
from pydantic import BaseModel
from . import SchemaAgent


class TicketAppointment(BaseModel):
    time_appointment_id: Optional[int]
    time_appointment: Optional[time]
    created_date: Optional[datetime]
    agent : Optional[SchemaAgent.Agent] = None

    class Config:
        orm_mode = True


class TimeAppointment(BaseModel):
    time_appointment_id: Optional[int]
    ticket_id: Optional[int]
    agent_id: Optional[str]
    time_appointment: Optional[time]
    created_date: Optional[datetime]

    class Config:
        orm_mode = True