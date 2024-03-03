import pytest
from wm5.py import process_video

@pytest.mark.parametrize("subtitres_whisper, sURL, subtitres_lang, t_video, t_audio, expected_output", [
    ("Субтитры", "https://www.youtube.com/watch?v=6EsCI3CbmTk", "ru", "", "", " Ну что, дружище, ты же на Мехмате учился? На Мехмате. Так ты тоже на Мехмате. А, слушай, а ты на какой кафедре учился? Так я матан. Матан? Матан. Ммм. А ты? Я алгебру учил. Прекрасно. Да, у меня к тебе вопрос такой. Давай. Как друг другу, да, скажи честно вот, доверительно, тебе когда-то этот матан пригодился в жизни? Я тебе скажу по секрету, один раз таки точно да. Как? Уронил я ключи в унитаз, взял проволоку, сделал интегратик и достал. О, интеграл взял."),
    
])
def test_process_video_with_valid_url(subtitres_whisper, sURL, subtitres_lang, t_video, t_audio, expected_output):
    result = process_video(subtitres_whisper, sURL, subtitres_lang, t_video, t_audio)
    assert result.strip() == expected_output.strip()
