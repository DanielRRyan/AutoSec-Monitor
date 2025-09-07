# backend/models.py

from sqlalchemy import Column, String, DateTime, Integer, Text
from db import Base
from datetime import datetime

class CVEAlert(Base):
    __tablename__ = "cve_alerts"

    id = Column(Integer, primary_key=True, index=True)
    package = Column(String, index=True)
    cve_id = Column(String, index=True)
    description = Column(Text)
    published = Column(DateTime)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
