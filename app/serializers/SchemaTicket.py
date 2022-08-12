# built-in libraries
from datetime import datetime
from typing import Optional, List
# third-party libraries
from pydantic import BaseModel
from . import SchemaOrganization
from . import SchemaTimeAppointment
from . import SchemaAgent



class Ticket(BaseModel):
    ticket_id: Optional[int]
    organization_id: Optional[str]
    agent_id: Optional[str]
    created_date: Optional[datetime]
    status: Optional[str]
    category: Optional[str]
    urgency: Optional[str]
    subject: Optional[str]
    sla_solution_date: Optional[datetime]
    sla_first_response: Optional[datetime]

    class Config:
        orm_mode = True


class TicketNestedCompany(BaseModel):
    ticket_id: Optional[int]
    organization: Optional[SchemaOrganization.Organization] = None
    agent: Optional[SchemaAgent.Agent] = None
    created_date: Optional[datetime]
    status: Optional[str]
    category: Optional[str]
    urgency: Optional[str]
    subject: Optional[str]
    sla_solution_date: Optional[datetime]
    sla_first_response: Optional[datetime]
    time_appointments: List[SchemaTimeAppointment.TicketAppointment] = None

    class Config:
        orm_mode = True
