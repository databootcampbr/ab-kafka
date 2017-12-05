from flask import Flask, render_template
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
def product():
    alternative = ab_test('buy_text', 'Buy', 'Free')
    return render_template('product.html',
        alternative=alternative
    )
@app.route("/buy")
def buy():
    finished('buy_text')
    return render_template('buy.html')
if __name__ == "__main__":
    app.run()
