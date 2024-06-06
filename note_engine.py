# docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/?h=functiontool#functiontool
from llama_index.tools import FunctionTool
import os
from datetime import datetime

note_path = os.path.join("data", "notes.txt")

def note_engine(note):
	if not os.path.exists(note_path):
		open(note_path, 'w')

	# Get the current date and time
	current_datetime = datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

	with open(note_path, 'a') as f:
		f.writelines([formatted_datetime + "\n" + note + "\n"])
	return "Saved successfully"


# now that we have the tool we can wrap it with the FunctionTool from llama
tool = FunctionTool.from_defaults(fn = note_engine,
								name ="note saver",
								description = "saves notes to a txt file")
