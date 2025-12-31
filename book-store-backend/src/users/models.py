from sqlalchemy.orm import Mapped, mapped_column

from db.mixins import BaseModelUUID, TimestampableMixin, str_255


class User(BaseModelUUID, TimestampableMixin):
    __tablename__ = "users"

    full_name: Mapped[str_255]
    email: Mapped[str_255] = mapped_column(unique=True)
    hashed_password: Mapped[str_255 | None] = mapped_column(unique=True)
    is_superadmin: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
