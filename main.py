import pandas as pd
from prompts import new_prompt, instruction_str
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from note_engine import note_engine
from prompts import context

#https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/
file_path = './data/population2023.csv'
df = pd.read_csv(file_path)
# The agent uses the PandasQueryEngine as a tool to query structured csv data and get use the human readble answers
population_query_engine = PandasQueryEngine(df=df, instruction_str= instruction_str, verbose=True)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})


# Create instances of the tools
population_query_engine_tool = QueryEngineTool(
	query_engine=population_query_engine,
	metadata=ToolMetadata(
		name="population_query",
		description="This gives information of the world population and demographics"
	)
)

# Define all the tools
tools = [
	note_engine,
	population_query_engine_tool
]

# Use an llm for reasoning and evaluation
llm = OpenAI(model= 'gpt-3.5-turbo')
agent = ReActAgent.from_tools(
	tools=tools, llm=llm, context = context, verbose=True,
)

while (prompt := input("Ask me anything (type exit to quit): ")) != "exit":
	respnse = agent.query(prompt)
	print(respnse)
