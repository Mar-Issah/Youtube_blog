# in order to make the handles_note fucn a tool we need to wrap it with the FunctionTool from llama
# docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/?h=functiontool#functiontool
from llama_index.tools import FunctionTool
import os

note_path = os.path.join("data", "notes.txt")

def handle_note(note):
	if not os.path.exists(note_path):
		open(note_path, 'w')

	with open(note_path, 'a') as f:
		f.writelines([note + "\n"])
	# return belwo so the the llm an use as reference to know that the tool executed its work successfully
	return "Saved successfully"

# it is important to give it a name and description so that llama knows the purpose of the tool and when to call and use it
tool = FunctionTool.from_defaults(fn = handle_note,
								name ="note saver",
								description = "saves notes to a txt file")