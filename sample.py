# https://python.langchain.com/docs/integrations/llms/llamacpp/

from langchain_community.llms import LlamaCpp

model_path = "tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf"

llm = LlamaCpp(
    model_path=model_path,
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    verbose=True,
)

question = """
Question: A rap battle between Stephen Colbert and John Oliver
"""

answer = llm.invoke(question)

print(answer)
