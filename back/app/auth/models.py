from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str | None] = mapped_column(
        String,
        unique=True,
        index=True,
        nullable=True
    )

    username: Mapped[str | None] = mapped_column(
        String,
        unique=True,
        index=True,
        nullable=True
    )

    password_hash: Mapped[str]

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
