"""Member 3: each workflow column has its own answering population."""
from src.analysis.common import frequency_table


def summarise(frame, column="AIWorkCurrentlyUse"):
    return frequency_table(frame, column, multiple=True)
