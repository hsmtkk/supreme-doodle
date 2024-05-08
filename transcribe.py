import whisper

model = whisper.load_model("base")
result = model.transcribe("240506-sleep.mp3")
print(result["text"])
