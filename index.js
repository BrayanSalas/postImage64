let db = firebase.database().ref('imagenes')
    
    db.on('value', function(data) {
        document.getElementById("img").src = 'data:image/jpg;base64,' + data.val().goku;
    })