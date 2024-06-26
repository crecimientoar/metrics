# example dune api query
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase

# define dune query
query_id = 2721037
today = today()

# pull latest executed result
dune = DuneClient.from_env()
dsr_state = dune.get_latest_result_dataframe(query_id)

# check if execution is more than 1 day old
dsr_state["dt"] = pd.to_datetime(dsr_state["dt"])
max_dsr_date = dsr_state["dt"].max()
max_dsr_date = max_dsr_date.date()
diff = abs(max_dsr_date - today)
if diff.days > 1:
    query_result = dune.run_query_dataframe(QueryBase((query_id)))
    query_result.to_csv("dsr_state.csv", index=False)
else:
    dsr_state.to_csv("dsr_state.csv", index=False)