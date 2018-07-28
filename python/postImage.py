from firebase import firebase
firebase = firebase.FirebaseApplication('https://proyecto-ejemplo-86c11.firebaseio.com/', None)

if __name__ == '__main__':
    
    with open("../assets/goku.jpg", "rb") as f:
        data = f.read()
        imagenCodificada = data.encode("base64")

    firebase.patch('/imagenes/', {'goku': imagenCodificada})