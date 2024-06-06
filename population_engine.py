
import pandas as pd
from prompts import new_prompt, instruction_str
from llama_index.experimental.query_engine import PandasQueryEngine

#https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/
def population_engine(file_path, query):
	df = pd.read_csv(file_path)
	# The agent uses the PandasQueryEngine as a tool to query structured csv data and get use the human readble answers
	query_engine = PandasQueryEngine(df=df, instruction_str= instruction_str, verbose=True)
	query_engine.update_prompts({"pandas_prompt": new_prompt})
	response = query_engine.query(query)
	print(response)
	return query_engine

