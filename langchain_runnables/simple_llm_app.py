from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv



load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model2 =ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    input_variables = ['topic'],
    template = 'Suggest a catchy blog about {topic}'
)

chain = prompt | model1

topic = input('Enter a topic')
output = chain.invoke({"topic": topic})

print("Generated Blog Title", output.content)