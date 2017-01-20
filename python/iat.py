#!/usr/bin/python
import ctypes,subprocess

iat_params = "sub = iat, domain = iat, language = zh_ch, accent = mandarin, sample_rate = 16000, result_type = plain, result_encoding = utf8"
tts_params = "voice_name = xiaoyan, text_encoding = UTF8, sample_rate = 16000, speed = 50, volume = 50, pitch = 50, rdn = 2"
login_params = "appid = 58723fb7, work_dir = ."


iatso = ctypes.CDLL("../libs/RaspberryPi/libiat.so")
ttsso = ctypes.CDLL("../libs/RaspberryPi/libtts.so")

if  iatso.iatLogin(login_params) == 0 :
	while 1:
		subprocess.call('arecord -D "plughw:1,0" -d 5 -r 16000 -f S16_LE ./test.wav', shell=True)
		text = iatso.iatRun("./test.wav", iat_params)
		ttsso.text_to_speech(text, "./out.wav", tts_params)
		subprocess.call('omxplayer out.wav', shell=True)
so.iatLogOut()
