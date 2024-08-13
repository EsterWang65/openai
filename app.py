from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/store')
def get_stores():
    return "Hello"
