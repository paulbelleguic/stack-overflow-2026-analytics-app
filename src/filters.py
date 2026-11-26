"""Filtres partagés et filtre local d'axe, sans Streamlit."""


def filter_population(frame, roles=None, experiences=None, employment=None):
    result = frame
    if roles:
        result = result.loc[result["Role"].isin(roles)]
    if experiences:
        result = result.loc[result["experience_group"].isin(experiences)]
    if employment:
        result = result.loc[result["Employment"].isin(employment)]
    return result.copy()
