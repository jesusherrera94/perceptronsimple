import pyrebase

class connection:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyCseJUkeU2hI3PUTkXA9UxjJosIOPrZvEI",
            "authDomain": "talleria-c580a.firebaseapp.com",
            "databaseURL": "https://talleria-c580a.firebaseio.com",
            "projectId": "talleria-c580a",
            "storageBucket": "talleria-c580a.appspot.com",
            "messagingSenderId": "364732825669",
            "appId": "1:364732825669:web:86bc77b58fd59155aa232c",
            "measurementId": "G-QCXW45MC9X"


        }   
        self.firebase = pyrebase.initialize_app(config)
        

    def pushDB(self,data):
        db = self.firebase.database()
        result = db.child("training").push(data)
        print(result)

    def getDB(self,id):
        db = self.firebase.database()
        result = db.child("training").get()
        for ids in result.each():
            if(ids.key() == id):
                return ids.val()



