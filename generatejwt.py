import jwt
import time

def generate_jitsi_token(room_name, user):
    app_id = 'jitsi_class_app_12d93f6e'
    app_secret = 'b4a5f784d7b8f9e12c6a58a3b9d12345a9e8f7a6c5b4d3a2f1e8d7c9b6a5e4f3'

    payload = {
        "aud": app_id,
        "iss": app_id,
        "sub": "api.codecraftmeet.online",  
        "room": room_name,
        "exp": int(time.time()) + 3600, 
        
        "context": {
            "user": {
                "name": user['name'],      
                "email": user['email'],
                "avatar": "https:/gravatar.com/avatar/abc123",    
                "affiliation": affiliation, 
            }
        }
    }

    token = jwt.encode(payload, app_secret, algorithm='HS256')
    return token

user = {
    "name": "Reniel dasdas",
    "email": "dsadsad@gmail.com",
}

room_name = "kahitano" #same name as created room name
affiliation = "owner" # owner for moderator or member for students/guests

token = generate_jitsi_token(room_name, user)
print(token)
