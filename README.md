<h2><i>WhisperModel (Получение текста из видео на Youtube)</i> :camera::arrow_right::page_facing_up:</h2>
<h3><u>Содержание</u></h3>
<p>1. Цель и функциональность программы</p>
<p>2. Инструкция по настройке и запуске модели</p>
<p>3. Пример использования</p>
<p>4. Члены команды</p>

___

<p><i>1. Цель и функциональность программы</i>: Упрощение работы по составлению стенограммы и конспекта на основе аудио и видео материалов является целью разработки программы. Пользователь в интерфейс программы передает ссылку на видео из Youtube и на выход получает текст из субтитра видео если имеется или от аудио из видеоролика.</p>

<p><i>2. Инструкция по настройке и запуске модели</i>: Для безотказнной работы программы на локальной компьютере, необходимо скачивать файл <a href="https://github.com/andlarionov/WhisperModel/blob/main/requirements.txt" target="_blank">requirements.txt</a> вместе <a href="https://github.com/andlarionov/WhisperModel/blob/main/wm5.py">с основным кодом</a> . Он содержит необходимые библиотеки для нормальной работы. Ниже приведены модули, которые необходимо использовать в коде для запуска модели :</p>

```python
import gradio as gr
import os
import moviepy.editor as mp 
from faster_whisper import WhisperModel
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
```

<p><i>3. Пример использования</i></p>

[Logo](https://disk.yandex.ru/i/_U7gkO5FQAgkGA)

<p><i>4. Члены команды</i></p>
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
