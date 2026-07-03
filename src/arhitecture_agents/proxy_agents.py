from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 

template = """
You are a proxy agent responsible for translating natural language into structured queries. 

User input: "{query}"

Return a JSON object with the following fields:
- intent: The action to perform.
- location: Inferred or stated location,
- time_filter: Indicate if the query includes time-based constraints. 
- format: Response format (e.g. 'list')

Respond ONLY with JSON
"""

prompt = PromptTemplate(input_variables= ["query"], template = template)

chain = LLMChain(prompt = prompt, llm=openai_chat)

response = chain.run({"query": "Find restaurants near me that are open now"})

