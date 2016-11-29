from flask import Flask, request
from datetime import datetime
import requests
from subprocess import check_output
import tempfile

app = Flask(__name__)


@app.route("/api/num_colors")
def colors():
    url = request.args.get('src')
    r = requests.get(url)
    temp = tempfile.NamedTemporaryFile()
    with open(temp.name, 'wb') as fd:
        fd.write(r.content)
    result = check_output(["identify", "-format", "%k", temp.name])
    return result

if __name__ == "__main__":
    app.run()
