from langchain_core.prompts import ChatPromptTemplate

system_message = """
Given an input question, create a syntactically correct {dialect} query to
run to help find the answer. Unless the user specifies in his question a
specific number of examples they wish to obtain, always limit your query to
at most {top_k} results. You can order the results by a relevant column to
return the most interesting examples in the database.

Never query for all the columns from a specific table, only ask for a the
few relevant columns given the question.

Pay attention to use only the column names that you can see in the schema
description. Be careful to not query for columns that do not exist. Also,
pay attention to which column is in which table.

Only use the following tables:
{table_info}
"""

USER_PROMPT = "Question: {input}"


class PromptTemplates: 
    def __init__(self, user_prompt: str = USER_PROMPT):
        
        self.query_prompt_template = ChatPromptTemplate(
    [("system", system_message), ("user", user_prompt)]) 
    
    def query_prompt(self): 
        return self.query_prompt_template
