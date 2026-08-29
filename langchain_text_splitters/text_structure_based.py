from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
My name is Nitish
I am 35 years old
I live in Gurgaon
How are you
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)