FROM python:3.11

RUN apt-get -y update && apt-get -y install ffmpeg

RUN pip install langchain-community llama-cpp-python openai-whisper

ENTRYPOINT ["tail", "-f", "/dev/null"]
