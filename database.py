from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Basisklasse für unsere SQLAlchemy-Modelle
Base = declarative_base()


class Breeder(Base):
  __tablename__ = "breeders"

  id = Column(Integer, primary_key=True, autoincrement=True)
  zwingername = Column(String, nullable=False)
  zuechtername = Column(String, nullable=True)
  adresse = Column(String, nullable=True)
  url = Column(String, nullable=True)
  content_hash = Column(String, nullable=True)
  last_checked = Column(DateTime, default=datetime.utcnow)
  status = Column(String, default="neu")


# SQLite-Datenbankdatei im Projektverzeichnis anlegen
DATABASE_URL = "sqlite:///sam.db"
engine = create_engine(DATABASE_URL, echo=False)

# Session-Fabrik für Transaktionen bereitstellen
SessionLocal = sessionmaker(bind=engine)


def init_db():
  """Erstellt die Datenbank und alle Tabellen, falls sie noch nicht existieren."""
  Base.metadata.create_all(engine)
  print("Datenbank `sam.db` erfolgreich initialisiert!")


if __name__ == "__main__":
  init_db()