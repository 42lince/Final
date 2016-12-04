from flask import Flask, request
from datetime import datetime
import requests
from subprocess import check_output
import tempfile


app = Flask(__name__)
app.debug = True

@app.route("/api/num_colors")
def colors():
    url = request.args.get('src')
    r = requests.get(url)
    temp = tempfile.NamedTemporaryFile()
    with open(temp.name, 'wb') as fd:
        fd.write(r.content)
    try:
        result = check_output(["/usr/bin/identify", "-format", "%k", temp.name])
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    return result

@app.route("/")
def index():
    return "Hello!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
