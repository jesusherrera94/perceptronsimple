import pyrebase

class connection:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyChsrzrviFkP6dPs4gg9fon__PTLLZZ9D4",
            "authDomain": "rappido-tests.firebaseapp.com",
            "databaseURL": "https://rappido-tests.firebaseio.com",
            "projectId": "rappido-tests",
            "storageBucket": "rappido-tests.appspot.com",
            "messagingSenderId": "961198614601",
            "appId": "1:961198614601:web:d5bc60b56c83c13b417798"

        }   
        self.firebase = pyrebase.initialize_app(config)
        

    def pushDB(self,data):
        db = self.firebase.database()
        result = db.child("pythonTest").push(data)
        print(result)

    def getDB(self,id):
        db = self.firebase.database()
        result = db.child("pythonTest").get()
        for ids in result.each():
            if(ids.key() == id):
                return ids.val()



