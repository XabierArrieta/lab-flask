import sys
sys.path.append("../")

from starter.code.app.app import app
from flask import requests


### Endpoints
"""
### /celebrity

- parameters = name, occupation, catch_phrase
- create a celebrity database
"""

@app.route("/celebrity")
def celebrity():
    celeb = request.arg