from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  

chat_template = ChatPromptTemplate.from_messages([
    ('system',"You are a helpful {domain} expert"),
    ('human', "Explain in simple terms what is {Topic}?")])

prompt = chat_template.format_prompt(domain="Cricket", Topic="Dusra")

print(prompt)