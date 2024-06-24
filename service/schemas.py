from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class SRef(BaseModel):
    id: UUID
    url: str

class SLink(BaseModel):
    id: UUID
    name: str
    refs: list[SRef]
    ref_index: int

class SLinkRef(BaseModel):
    id: UUID
    ref_id: UUID
    link_id: UUID

class SLinkAccess(BaseModel):
    id: UUID
    link_id: UUID
    ip_address: str
    access_time: datetime