# docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/?h=functiontool#functiontool
from llama_index.core.tools import FunctionTool
import os
from datetime import datetime

note_path = os.path.join("data", "notes.txt")

def handle_note(note):
	if not os.path.exists(note_path):
		open(note_path, 'w')

	# Get the current date and time
	current_datetime = datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

	with open(note_path, 'a') as f:
		f.writelines(["NEW NOTE ON:" + formatted_datetime + "\n" + note + "\n\n"])
	return "Saved successfully"


# now that we have the tool we can wrap it with the FunctionTool from llama and export it
note_engine = FunctionTool.from_defaults(fn = handle_note,
								name ="note_saver",
								description = "saves notes to a txt file")
