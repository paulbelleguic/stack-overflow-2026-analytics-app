"""Member 2: starting calculations for tools; use and wishes stay separate."""
from src.analysis.common import frequency_table


def summarise(frame, column="AICodeAgentHaveWorkedWith"):
    return frequency_table(frame, column, multiple=True)
