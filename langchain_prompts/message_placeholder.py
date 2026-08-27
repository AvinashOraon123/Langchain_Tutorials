from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate.from_messages([
    ('system',"You are a helpful {customer_support} expert"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt', 'r') as f:
    chat_history = f.readlines()

print(chat_history)

# create prompt
prompt = chat_template.format_prompt(customer_support="Customer Service", query="Where is my refund?", chat_history=chat_history)

print(prompt)