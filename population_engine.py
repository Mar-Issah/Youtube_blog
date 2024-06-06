import pandas as pd
from prompts import new_prompt, instruction_str
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms import OpenAI
from note_engine import note_engine
from prompts import context

#https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/
def population_engine(file_path):
	df = pd.read_csv(file_path)
	# The agent uses the PandasQueryEngine as a tool to query structured csv data and get use the human readble answers
	query_engine = PandasQueryEngine(df=df, instruction_str= instruction_str, verbose=True)
	query_engine.update_prompts({"pandas_prompt": new_prompt})
	#response = query_engine.query("What is the pouplation of Canada?")
	return query_engine


# define all the tools
tools = [
	note_engine,
	QueryEngineTool.from_defaults(query_engine = population_engine('./data/population2023.csv'), metadata = ToolMetadata(name = "Population Query Engine", description = "Query Engine for World Population", type = "query_engine")),
]

# Use an llm for reasoning and evaluation
llm = OpenAI(model= 'gpt-3.5-turbo')
agent = ReActAgent.from_tools(
	llm=llm, tools=tools,  context = context, sources=[], verbose=True,
)
