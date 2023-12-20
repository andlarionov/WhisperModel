import gradio as gr
import os
import moviepy.editor as mp
from faster_whisper import WhisperModel
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Загружаем модель Whisper
model = WhisperModel("large-v2")

def process_video(subtitles_whisper, sURL, subtitles_lang):
    # Извлекаем видео ID из URL
    video_id = sURL.split("v=")[1]

    # Получаем информацию о видео
    yt = YouTube(sURL)

    if subtitles_whisper == 'Субтитры':
        # Извлекаем субтитры
        return GetSubtitles(subtitles_lang, yt)
    elif subtitles_whisper == 'Распознать аудио':
        # Извлекаем субтитры
        text_from_video = GetTextFromVideoYt(yt)
        # Суммаризируем текст
        summarizer = LsaSummarizer()
        parser = PlaintextParser.from_string(text_from_video, Tokenizer("english"))
        summarized_text = summarizer(parser.document, sentences_count=10)  # Меняйте sentences_count по вашему усмотрению
        return "\n".join(str(sentence) for sentence in summarized_text)

    return "Укажите параметры работы с видео материалом."

def GetSubtitles(first_language_code, yt):
    sLang = 'Базовые языки:' + '\n'
    bFind = False
    transcript_list = YouTubeTranscriptApi.list_transcripts(yt.video_id)

    for transcript in transcript_list:
        sLang += '   - ' + transcript.language_code + ' - ' + transcript.language + '\n'
        if transcript.language_code == first_language_code:
            Text_sub = transcript.fetch()
            bFind = True
            break
    sLang += '\n' + 'Переводы:' + '\n'
    if not bFind:
        for transcript in transcript_list:
            if transcript.is_translatable:
                sLang += '   - Базовый язык ' + transcript.language_code + ' - ' + transcript.language + '. Переводы:\n'
                for tr_l in transcript.translation_languages:
                    sLang += '      - ' + tr_l['language_code'] + ' - ' + tr_l['language'] + '\n'
                    if tr_l['language_code'] == first_language_code:
                        Text_sub = transcript.translate(first_language_code).fetch()
                        bFind = True
                        break

    sText = ''
    if bFind:
        for s1 in Text_sub:
            sText += s1['text'] + '\n'
        return sText
    else:
        return "Указанный код языка не найден. Возможно выбрать указанные ниже языки:" + '\n' + sLang

def GetTextFromVideoYt(yt):
    fileName = yt.streams.filter(type="audio").first().download()

    audio_file = mp.AudioFileClip(fileName)
    audio_file.write_audiofile("vrem.wav")

    segments, info = model.transcribe("vrem.wav")
    sText = ''

    for segment in segments:
        sText += segment.text
    os.remove(fileName)
    os.remove("vrem.wav")

    return sText

iface = gr.Interface(
    fn=process_video,
    inputs=[
        gr.Radio(["Субтитры", "Распознать аудио"], label="Вариант исполнения на YouTube:"),
        gr.Text("https://www.youtube.com/watch?v=6EsCI3CbmTk", label="YouTube - ссылка на страницу с видео"),
        gr.Text("ru", label="Язык субтитров (основной либо перевод (указывается код): ru, en ...)")
    ],
    outputs=['text']
)
iface.launch(share=True)
