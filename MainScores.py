from flask import Flask, render_template
import Utils

app = Flask(__name__)

@app.route("/")
def score_server():
    points = 0
    try:
        scores_file = open(Utils.SCORES_FILE_NAME, 'r')
        for line in scores_file.readlines():
            points = int(line)
        scores_file.close()
        return render_template('index.html', score=points)
    except:
        return render_template('error_index.html')

app.run(host='127.0.0.1', debug=True, port=3000)