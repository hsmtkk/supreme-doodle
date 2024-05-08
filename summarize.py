# https://python.langchain.com/docs/integrations/llms/llamacpp/

from langchain_community.llms import LlamaCpp

with open("transcription.txt") as f:
    transcription = f.read()

prompt = f"""### Instruction ###
Summarize the following sentences in 100 characters or less.

### Sentences ###
{transcription}

### Summary ###
"""

print(prompt)

model_path = "tinyllama-1.1b-chat-v0.3.Q5_K_M.gguf"

llm = LlamaCpp(
    model_path=model_path,
    verbose=True,
)

answer = llm.invoke(prompt)

print(answer)
