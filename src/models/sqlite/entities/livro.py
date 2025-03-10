from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class TabelaLivros(Base):
    __tablename__ = "livros"

    id = Column(BIGINT, primary_key=True)
    titulo = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    foto = Column(String, nullable=False)
    autor = Column(String, nullable=False)

    def __repr__(self):
        return f"Livros [titulo={self._titulo}, editora={self.editora}, foto={self.foto}, autor={self.autor}]"
    