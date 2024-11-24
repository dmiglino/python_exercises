from flask import Flask, request
import random

app1 = Flask(__name__)
max_value = 1000

@app1.route('/set_max/<max>', methods=['POST'])
def set_max(max):
    global max_value
    max_value = int(max)
    return "Ok!"

@app1.route('/get_value', methods=['GET'])
def get_value():
    num = random.randint(1, max_value)    
    return str(num)

app1.run(port=5000)

