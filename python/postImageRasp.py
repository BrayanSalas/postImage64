from firebase import firebase
import time
import picamera
firebase = firebase.FirebaseApplication('https://proyecto-ejemplo-86c11.firebaseio.com/', None)

with picamera.PiCamera() as picam:
	ruta = "../assets/foto.jpg"
	picam.start_preview()
	time.sleep(5)
	picam.capture(ruta)
	picam.stop_preview()
	picam.close()
	time.sleep(5)

with open(ruta, "rb") as f:
    data = f.read()
    imagenCodificada = data.encode("base64")
    firebase.patch('/imagenes/', {'foto': imagenCodificada})