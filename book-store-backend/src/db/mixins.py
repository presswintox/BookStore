from datetime import datetime
from typing import Annotated
from uuid import UUID

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from db import Base

str_255 = Annotated[
    str,
    mapped_column(String(255), default=""),
]


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, sort_order=-10)


class BaseModelUUID(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(primary_key=True, sort_order=-10)


class TimestampableMixin(object):
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now())
