from . import Base
from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column


class Candidate(Base):
    __tablename__ = 'candidate'

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
