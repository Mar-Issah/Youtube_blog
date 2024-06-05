
import pandas as pd
from prompts import new_prompt, instruction_str
from llama_index.experimental.query_engine import PandasQueryEngine

#https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/
def handle_csv(file_path, query):
	df = pd.read_csv(file_path)
	# query specifically for csv file takes the df as param
	# now that we have the query_engine we can nor run our query
	# pass in the variables to be injected by the prompt template
	query_engine = PandasQueryEngine(df=df, instruction_str= instruction_str, verbose=True)
	query_engine.update_prompts({"pandas_prompt": new_prompt})
	response = query_engine.query(query)
	return response
