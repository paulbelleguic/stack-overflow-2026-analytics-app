"""Pure calculations for axis 2; no Streamlit or data loading."""
import pandas as pd
from src.analysis.common import frequency_table, valid_answers

USED = 'AICodeAgentHaveWorkedWith'
WANTED = 'AICodeAgentWantToUseNext6Months'
VENDORS = 'LLMHaveWorkedWith'


def choices(value):
    """Distinct non-empty selections; a missing list remains unknown."""
    if pd.isna(value) or not str(value).strip():
        return None
    return {part.strip() for part in str(value).split(';') if part.strip()}


def tool_ranking(frame, column):
    table, n = frequency_table(frame, column, multiple=True)
    return table.sort_values(['respondents', 'answer'], ascending=[False, True]).reset_index(drop=True), n


def paired_comparison(frame):
    """Two explicit lists, same people and denominator; not a growth measure."""
    paired = frame.loc[valid_answers(frame, USED) & valid_answers(frame, WANTED)]
    used, n = tool_ranking(paired, USED)
    wanted, _ = tool_ranking(paired, WANTED)
    result = used.rename(columns={'respondents': 'used_n', 'share_pct': 'used_pct'}).merge(
        wanted.rename(columns={'respondents': 'wanted_n', 'share_pct': 'wanted_pct'}),
        on='answer', how='outer').fillna(0)
    result[['used_n', 'wanted_n']] = result[['used_n', 'wanted_n']].astype(int)
    result['difference_points'] = result['wanted_pct'] - result['used_pct']
    result['maximum_n'] = result[['used_n', 'wanted_n']].max(axis=1)
    result = result.sort_values(['maximum_n', 'answer'], ascending=[False, True]).drop(columns='maximum_n')
    return result.reset_index(drop=True), n


def tool_count_distribution(frame):
    """Names selected over the past year, not concurrent use; exclude unknowns."""
    values = frame.loc[valid_answers(frame, USED), USED].map(choices).map(len)
    categories = values.map(lambda n: '1 outil' if n == 1 else '2 outils' if n == 2 else '3 outils' if n == 3 else '4 outils ou plus')
    counts = categories.value_counts().reindex(['1 outil', '2 outils', '3 outils', '4 outils ou plus'], fill_value=0)
    table = counts.rename_axis('answer').rename('respondents').reset_index()
    table['share_pct'] = table.respondents / len(values) * 100 if len(values) else 0.0
    return table, len(values)


def selected_tool_details(frame, tool):
    """Paired selections for one tool, not a retention or conversion metric."""
    paired = frame.loc[valid_answers(frame, USED) & valid_answers(frame, WANTED)]
    used = paired[USED].map(choices).map(lambda v: tool in v)
    wanted = paired[WANTED].map(choices).map(lambda v: tool in v)
    return {'paired_n': len(paired), 'used_n': int(used.sum()),
            'wanted_n': int(wanted.sum()), 'both_n': int((used & wanted).sum())}
