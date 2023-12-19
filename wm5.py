import gradio as gr
from faster_whisper import WhisperModel
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Загружаем модель Whisper
model = WhisperModel("large-v2")

def process_video(video_url):
    # Извлекаем видео ID из URL
    video_id = video_url.split("v=")[1]

    # Получаем информацию о видео
    yt = YouTube(video_url)

    # Извлекаем субтитры
    first_language_code = 'ru'
    bFind = False
    transcript_list = YouTubeTranscriptApi.list_transcripts(yt.video_id)

    for transcript in transcript_list:
        if transcript.language_code == first_language_code:
            Text_sub = transcript.fetch()
            bFind = True
            break

    if not bFind:
        for transcript in transcript_list:
            if transcript.is_translatable == True:
                for tr_l in transcript.translation_languages:
                    if tr_l['language_code'] == first_language_code:
                        Text_sub = transcript.translate(first_language_code).fetch()
                        bFind = True
                        break

    sText = ''
    for s1 in Text_sub:
        sText += s1['text'] + '\n'

    return sText

    # Работаем с аудио
    if not sText:
        fileName = yt.streams.filter(type="audio").first().download()
        segments, _ = model.transcribe(fileName)
        os.remove(fileName)

        result_text = "\n".join([segment.text for segment in segments])
        return result_text

    return "No text extracted from video."

iface = gr.Interface(fn=process_video, inputs="textbox", outputs="text")
iface.launch(share=True)

    #print(sText)
