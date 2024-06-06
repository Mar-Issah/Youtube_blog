# docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/?h=functiontool#functiontool
from llama_index.tools import FunctionTool
import os

note_path = os.path.join("data", "notes.txt")

def note_engine(note):
	if not os.path.exists(note_path):
		open(note_path, 'w')

	with open(note_path, 'a') as f:
		f.writelines([note + "\n"])
	return "Saved successfully"


# now that we have the tool we can wrap it with the FunctionTool from llama
tool = FunctionTool.from_defaults(fn = note_engine,
								name ="note saver",
								description = "saves notes to a txt file")
