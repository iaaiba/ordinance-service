from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class AdministrativeDecision(PublicationDetails):
    """Decisão Administrativa"""
