from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.database.base import BaseEntity
from shared.enums import DocumentStatus
from shared.mixins import TimestampMixin


class DocumentModel(BaseEntity, TimestampMixin):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[DocumentStatus] = mapped_column(
        String(50),
        default=DocumentStatus.PENDING
    )