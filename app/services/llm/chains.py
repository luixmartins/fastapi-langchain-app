from typing_extensions import TypedDict, Annotated 
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool

from .template import PromptTemplates 
from .factory import ChatModelFactory 

from ..database import DatabaseService 


class State(TypedDict): 
    """
    State object for chains.
    """
    question: str
    query: str 
    result: str 
    answer: str 
    
class QueryOutput(TypedDict): 

    query: Annotated[str, ..., "Syntactically valid SQL query"] 
    
class ChainFactory(State): 
    def __init_subclass__(cls):
        return super().__init_subclass__()    
        
    def write_query(self, state: State): 
        """Generate SQL query to fetch information."""
        
        
        
        query_prompt_template = PromptTemplates().query_prompt()
        
        prompt = query_prompt_template.invoke(
            {
                "dialect": self.db['dialect'],
                "top_k": 10,
                "table_info": self.db['table_names'],
                "input": state["question"],
            }
        )
        structured_llm = self.llm.with_structured_output(QueryOutput)
        result = structured_llm.invoke(prompt)
        
        return {"query": result["query"]}
    
    def execute_query(self, state: State):
        """Execute SQL query."""
        execute_query_tool = QuerySQLDatabaseTool(db=self.db)
        
        return {"result": execute_query_tool.invoke(state["query"])}
    
    def generate_answer(self, state: State): 
        """Answer question using retrieved information as context."""
        prompt = (
            "Given the following user question, corresponding SQL query, "
            "and SQL result, answer the user question.\n\n"
            f"Question: {state['question']}\n"
            f"SQL Query: {state['query']}\n"
            f"SQL Result: {state['result']}"
        )
        response = self.llm.invoke(prompt)
        
        return {"answer": response.content}

class ChainFactory:
    """
    A factory class for creating and managing the execution of a chain of operations 
    involving a language model (LLM) and a database. This class is designed to handle 
    the process of generating SQL queries from natural language questions, executing 
    those queries on a database, and generating human-readable answers based on the 
    query results.
    Attributes:
        llm: An instance of a language model initialized via the ChatModelFactory.
        db: A database connection object retrieved via the DatabaseService.
    Methods:
        write_query(question: str) -> str:
            Generates an SQL query from a natural language question using a prompt 
            template and the language model. The query is tailored to the database's 
            dialect and schema.
        execute_query(query: str) -> str:
            Executes the given SQL query on the connected database and returns the 
            query result.
        generate_answer(question: str, query: str, result: str) -> str:
            Generates a human-readable answer to the user's question based on the 
            original question, the SQL query, and the query result.
        run_chain(question: str) -> State:
            Executes the full chain of operations: generates an SQL query from the 
            question, executes the query, and generates a final answer. Returns a 
            State object containing the question, query, result, and answer.
    """
    def __init__(self):
        self.llm = ChatModelFactory().init_model()
        self.db = DatabaseService().get_db()

    def write_query(self, question: str) -> str:
        query_prompt_template = PromptTemplates().query_prompt()
        
        prompt = query_prompt_template.invoke({
            "dialect": self.db['dialect'],
            "top_k": 10,
            "table_info": self.db['table_names'],
            "input": question,
        })
        
        structured_llm = self.llm.with_structured_output(QueryOutput)
        result = structured_llm.invoke(prompt)
        
        return result["query"]

    def execute_query(self, query: str) -> str:
        execute_query_tool = QuerySQLDatabaseTool(db=self.db)
        
        return execute_query_tool.invoke(query)

    def generate_answer(self, question: str, query: str, result: str) -> str:
        prompt = (
            "Given the following user question, corresponding SQL query, "
            "and SQL result, answer the user question.\n\n"
            f"Question: {question}\n"
            f"SQL Query: {query}\n"
            f"SQL Result: {result}"
        )
        response = self.llm.invoke(prompt)
        
        return response.content

    def run_chain(self, question: str) -> State:
        query = self.write_query(question)
        result = self.execute_query(query)
        answer = self.generate_answer(question, query, result)
        
        return State(question=question, query=query, result=result, answer=answer)