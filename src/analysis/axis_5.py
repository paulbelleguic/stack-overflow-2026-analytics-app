"""Member 5: learning and adoption requirements."""
from src.analysis.common import frequency_table


def summarise(frame, column="LearnAI"):
    return frequency_table(frame, column, multiple=(column != "LearnAI"))
