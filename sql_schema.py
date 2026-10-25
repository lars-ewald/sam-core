from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Breeder(Base):
  __tablename__ = "breeders"

  # Technischer Anker, da Zwingername doppelt sein kann
  id = Column(Integer, primary_key=True, autoincrement=True)

  # Fachliche Stammdaten
  zwingername = Column(String, nullable=False)
  zuechtername = Column(String, nullable=True)
  adresse = Column(String, nullable=True)
  url = Column(
      String, nullable=True
  )  # Optional, falls keine eigene Website vorhanden

  # Status- und Überwachungswerte für den Scraper & die UI
  content_hash = Column(
      String, nullable=True
  )  # Für den präzisen Diff-Vergleich der Seite
  last_checked = Column(DateTime, default=datetime.utcnow)
  status = Column(
      String, default="neu"
  )  # Später steuerbar via UI (z.B. 'aktiv', 'kontaktiert', 'abgesagt')