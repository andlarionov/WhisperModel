[![Tests](https://github.com/sozykin/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/andlarionov/WhisperModel/actions)
<h2><i>WhisperModel (Приложение для формирования текстов из видео и аудио фвйлов)</i> :camera::arrow_right::page_facing_up:</h2>
<h3><u>Содержание</u></h3>
<p>1. Цель и функциональность программы</p>
<p>2. Инструкция по настройке и запуске модели</p>
<p>3. Пример использования</p>
<p>4. Члены команды</p>

___

<h4><i>1. Цель и функциональность программы</i></h4><p>Составление стенограммы на основе аудио и видео материалов является целью разработки программы. Пользователь в интерфейс программы передает ссылку на видео из Youtube и на выход получает (по выбору):
  
  - текст из субтитров к видео;
  
  - текст, полученный в результате работы модели WhisperModel (аудио- видео-файлы, либо c Youtube). </p>

Есть возможность выполнить суммаризацию текста.

<h4><i>2. Инструкция по настройке и запуске модели</i></h4><p>Для безотказнной работы программы на локальной компьютере, необходимо скачивать файл <a href="https://github.com/andlarionov/WhisperModel/blob/main/requirements.txt" target="_blank">requirements.txt</a> вместе <a href="https://github.com/andlarionov/WhisperModel/blob/main/wm5.py">с основным кодом</a> . Он содержит необходимые библиотеки работы. Ниже приведены модули, которые необходимо использовать в коде для запуска модели :</p>

```python
import gradio as gr
import os
import moviepy.editor as mp 
from faster_whisper import WhisperModel
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import sumy
import nltk
```
Для работы с аудио файлами, отличными от WAV, может понадобиться выполнить следующие команды:
```python
apt-get install software-properties-common
sudo apt-get update
sudo apt-get install ffmpeg
```

Для развертывания программы в облаке используется платформа gradio. При использовании кода на своем компьютере и последующей запуске на платформе, необходимо предварительно установить модуль gradio вводя в командной строке `pip install gradio`.
<h4><i>3. Пример использования</i></h4>

![Пример использования модели](https://github.com/andlarionov/WhisperModel/blob/main/Image_Audio_Video/Image1.png)
![Пример использования модели](https://github.com/andlarionov/WhisperModel/blob/main/Image_Audio_Video/Image2.png)

Ссылка на приложение в gradio : [WhisperModel](https://17057622af014b6ae7.gradio.live/)
<h4><i>4. Члены команды</i></h4>
<table border="1">
  <tr>
    <td>Члены команды</td>
    <td>Основная задача</td>
    <td>Участие в решении иных задач</td>
  </tr>
  <tr>
    <td>Ларионов Андрей</td>
    <td>Менеджер проекта, Full Stack-разработчик</td>
    <td>Инженер по машинному обучению</td>
  </tr>
  <tr>
    <td>Попов Александр</td>
    <td>Инженер по машинному обучению</td>
    <td>Full Stack-разработчик, Тестировщик-QA инженер</td>
  </tr>
  <tr>
    <td>Режист Моиз</td>
    <td>Документалист</td>
    <td>Тестировщик-QA инженер</td>
  </tr>
</table>
