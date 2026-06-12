from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

os.environ['HF_HOME']='E:/hf_cache'

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    temperature = 0,
    max_new_tokens=102
)

model = ChatHuggingFace(llm=llm)

respone = model.invoke("What is the orchestration in langchain?")

print(respone.content)