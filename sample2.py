# https://python.langchain.com/docs/integrations/llms/llamacpp/

from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate

model_path = "tinyllama-1.1b-chat-v0.3.Q5_K_M.gguf"

llm = LlamaCpp(
    model_path=model_path,
    verbose=True,
)

template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

prompt = PromptTemplate.from_template(template)

llm_chain = prompt | llm

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

answer = llm_chain.invoke({"question": question})

print(answer)
