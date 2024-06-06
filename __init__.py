from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index import ReActAgent
from llama_index.llms import OpenAI
from note_engine import note_engine
from population_engine import population_engine
from prompts import context

# So just like we did for the note_engine we by creating a function tool with name and description we do same for the population_engine. The only different is the for the functiontool we used that because it was a custom function.
# for the population query we already use a query_engine (PandasQueryEngine) so when defining the tools, we use QueryEngineTool

tools = [
	note_engine,
	QueryEngineTool.from_defaults(query_engine = population_engine, metadata = ToolMetadata(name = "Population Query Engine", description = "Query Engine for World Population", type = "query_engine")),
]

# now we instantiat our llm
# And also or agent. The ReActAgent takes the tools list and is able to choose from the list which tool is best suited for the job based on the query. Verbose is true so as to see how the agent is thinking and which tool it is using.
# the context as defined in the prompts file give the agent a role and tells it what its function is and what it should be doing
llm = OpenAI(model= 'gpt-3.5-turbo')
agent = ReActAgent.from_tools(
	llm=llm, tools=tools, verbose=True, context = context
)
