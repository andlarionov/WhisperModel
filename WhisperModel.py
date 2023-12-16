from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from faster_whisper import WhisperModel
import moviepy.editor as mp
import os

app = FastAPI()

# Загружаем модель Whisper
model = WhisperModel("large-v2")

@app.post("/process_audio/")
async def process_audio(file: UploadFile = File(...)):
    # Сохраняем загруженный аудиофайл
    file_path = f"uploaded_audio/{file.filename}"
    with open(file_path, "wb") as audio_file:
        audio_file.write(file.file.read())

    # Если субтитры найдены, используем их
    if sText:
        segments, info = model.transcribe(audio_path=file_path)
        results = {"segments": segments, "info": info}
    else:
        # Если субтитры не найдены, просто выводим текст из распознавания аудио
        video = mp.AudioFileClip(file_path)
        audio_file_path = "vrem.wav"
        video.audio.write_audiofile(audio_file_path)
        segments, info = model.transcribe(audio_path=audio_file_path)
        results = {"segments": segments, "info": info}
        os.remove(audio_file_path)

    return JSONResponse(content=results)

# Ваш код для загрузки видео и получения субтитров

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
