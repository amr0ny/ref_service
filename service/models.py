from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()

class Ref(Base):
    __tablename__ = 'ref'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String)
    links = relationship('Link', secondary='link_ref', back_populates='refs')

class LinkRef(Base):
    __tablename__ = 'link_ref'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ref_id = Column(UUID(as_uuid=True), ForeignKey('ref.id'))
    link_id = Column(UUID(as_uuid=True), ForeignKey('link.id'))

class Link(Base):
    __tablename__ = 'link'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    ref_index = Column(Integer, default=0)
    refs = relationship('Ref', secondary='link_ref', back_populates='links')


class LinkAccess(Base):
    __tablename__ = 'link_access'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    link_id = Column(UUID, ForeignKey('link.id'))
    ip_address = Column(String, index=True)
    ref_index = Column(Integer)
    access_time = Column(DateTime, default=datetime.utcnow)