"""Member 1: starting calculations for adoption and profiles."""
from src.analysis.common import adoption_by


def summarise(frame, group_column="experience_group", minimum=20):
    return adoption_by(frame, group_column, minimum)
