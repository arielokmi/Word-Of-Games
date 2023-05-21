from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def score_server():
    try :
        f = open('score.txt', 'r')
        return render_template('score_server.html',SCORE = f.read())
        f.close()
    except:
        return  render_template("score_server_eror.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")

