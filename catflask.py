# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from flask import *
from flask import url_for
import argparse
import requests
import os

app = Flask(__name__)


@app.route("/")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', type=int)
    args = parser.parse_args()
    directory = "static"

    parent_dir = '/Users/lenguyen/Desktop/flaskproject'
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.mkdir(path)

    for i in range(args.integers):
        location = os.path.join(path, 'cat' + str(i))

        r = requests.get('https://cataas.com/cat')
        with open(location, 'wb') as f:
            f.write(r.content)
        return url_for('static', filename='cat'+str(i))


if __name__ == "__main__":
    main()
