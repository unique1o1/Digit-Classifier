from flask import Flask, render_template, request
import os
import sys
import re
import base64
import numpy as np
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template("index.html")


extra_dirs = ['./templates']
extra_files = []
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

print(extra_files)
if __name__ == '__main__':
    app.run(port=5000, extra_files=extra_files)
