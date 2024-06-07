from llama_index.core import PromptTemplate

instruction_str = """\
1. Convert the query to executable Python code using Pandas.
2. The final line of code should be a Python expression that can be called with the `eval()` function.
3. The code should represent a solution to the query.
4. PRINT ONLY THE EXPRESSION.
5. Do not quote the expression.
"""

new_prompt = PromptTemplate(
    """\
You are working with a pandas dataframe in Python.
The name of the dataframe is `df`.
This is the result of `print(df.head())`:
{df_str}

Follow these instructions:
{instruction_str}
Query: {query_str}

Expression: """
)

context = """\
You are an agent and an expert on the population of the world and country.\
    You will answer questions from users by providing accurate and detailed informrtion \
    about the population of the world and country
"""