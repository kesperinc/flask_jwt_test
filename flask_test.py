import bcrypt


from flask import Flask
app = Flask(__name__)

password = "password"
encrypted_password = bcrypt.hashpw(password.encode(
    "utf-8"), bcrypt.gensalt())  # str 객체, bytes로 인코드, salt를 이용하여 암호화
print(encrypted_password)  # bytes-string
print(encrypted_password.decode("utf-8"))  # str 객체

print("updated")

"""
https://justkode.kr/python/flask-restapi-3 : Flask로 REST API 구현하기 참고 
    pip install bcrypt
    pip install PyJWT
    pip install Flask-JWT-Extended

https://edudeveloper.tistory.com/135 : Flask 사용 방법 참고
"""


@app.route('/')
def hello_world():
    return 'Hello World! '+encrypted_password.decode("utf-8")


if __name__ == '__main__':
    app.run()
