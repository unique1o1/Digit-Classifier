from flask import Flask, render_template, request
import os
import sys
import re
import base64
import numpy as np
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
