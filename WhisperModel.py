import io
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
from youtube_transcript_api import YouTubeTranscriptApi
from faster_whisper import WhisperModel

app = FastAPI()
model = WhisperModel("large-v2")

class VideoInfo(BaseModel):
    video_url: str

@app.post("/process_video/")
async def process_video(video_info: VideoInfo, file: UploadFile = File(...)):
    # Сохраняем загруженный видеофайл
    video_path = f"uploaded_videos/{file.filename}"
    with open(video_path, "wb") as video_file:
        video_file.write(file.file.read())

    # Получаем информацию о видео
    video_info = VideoFileClip(video_path)
    
    # Работаем с субтитрами
    first_language_code = 'ru'
    transcript_list = YouTubeTranscriptApi.list_transcripts(YouTube(video_info).video_id)
    
    bFind = False
    for transcript in transcript_list:
        if transcript.language_code == first_language_code:
            text_sub = transcript.fetch()
            bFind = True
            break
    
    if not bFind:
        for transcript in transcript_list:
            if transcript.is_translatable:
                for tr_l in transcript.translation_languages:
                    if tr_l['language_code'] == first_language_code:
                        text_sub = transcript.translate(first_language_code).fetch()
                        bFind = True
                        break
    
    if bFind:
        sText = ''
        for s1 in text_sub:
            sText += s1['text'] + '\n'

        print("Субтитры:")
        print(sText)

    # Работаем с аудио
    audio_file_path = "audio.wav"
    video_info.audio.write_audiofile(audio_file_path)

    segments, info = model.transcribe(audio_file_path)

    print("Результаты распознавания:")
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

    os.remove(audio_file_path)
    os.remove(video_path)

    return {"segments": segments, "info": info}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
