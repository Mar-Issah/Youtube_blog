
import pandas as pd
#from llama_index.core.query_engine import PandasQueryEngine
from llama_index.experimental.query_engine import PandasQueryEngine

#https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/
def handle_csv(file_path):
	df = pd.read_csv(file_path)
	# query specifically for csv file takes the df as param
	# now that we have the query_engine we can nor run our query
	query_engine = PandasQueryEngine(df=df, verbose=True)
	response = query_engine.query("What is the population of India in 2023?")
	return response
