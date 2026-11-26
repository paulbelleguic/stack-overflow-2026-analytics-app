"""Member 4: trust and verification practices, not objective tool accuracy."""
from src.analysis.common import frequency_table


def summarise(frame, column="AITrust"):
    return frequency_table(frame, column, multiple=(column == "AIWorkNext"))
