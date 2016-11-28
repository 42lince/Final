from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def time():
	begin = datetime(1970, 1, 1, 0, 0, 0, 0)
	delta = (datetime.utcnow() - begin).total_seconds()
	return "UTC Time Now: " + str(round(delta))

if __name__ == "__main__":
    app.run()
