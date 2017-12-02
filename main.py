from flask import Flask
from flask_split import split, ab_test, finished

app = Flask(__name__)
app.config.update(dict(
    REDIS_URL='redis://localhost:6379',
    KAFKA_SERVERS='localhost:9092',
    KAFKA_TOPIC='ab_test',
    SESSION_TYPE='filesystem'
))

app.secret_key = 'super secret key'

app.register_blueprint(split)
@app.route("/")
def hello():
    ab_test('signup_btn_text', 'Register', 'SignUp')
    finished('signup_btn_text')
    return "Hello World!"

if __name__ == "__main__":
    app.run()
