from flask import Flask, render_template, request, jsonify
from Manager.Control.controler import Controler
import json

app = Flask(__name__)
controler = Controler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_spider_list', methods=['GET'])
def get_spider_list():
    data = controler._get_spider_list()
    return jsonify(data)

@app.route('/spider', methods=['POST'])
def get_spider():
    pass

@app.route('/create_spider', methods=['GET', 'POST'])
def create_spider():
    kwargs = {}
    kwargs['name'] = request.form['name']
    kwargs['domain'] = request.form['domain']
    kwargs['urls'] = request.form['urls']
    kwargs['rules'] = request.form['rules']
    kwargs['title'] = request.form['title']
    if (kwargs['domain'] != '') & (kwargs['urls'] != '') & (kwargs['rules'] != '') & (kwargs['title'] != '') & (kwargs['name'] != ''):
        try:
            controler._create_spider(**kwargs)
        except Exception as e:
            print(str(e))
            return '0'
        return '1'
    else:
        return '0'

@app.route('/start_spider', methods=['GET', 'POST'])
def start_spider():
    name = request.form['name']
    try:
        controler._start_spider(name)
    except Exception as e:
        print(str(e))
        return '0'
    return '1'

@app.route('/stop_spider', methods=['GET', 'POST'])
def stop_spider():
    name = request.form['name']
    try:
        controler._stop_spider(name)
    except Exception as e:
        print(str(e))
        return '0'
    return '1'

@app.route('/delete_spider', methods=['GET', 'POST'])
def delete_spider():
    name = request.form['name']
    try:
        controler._delete_spider(name)
    except Exception as e:
        print(str(e))
        return '0'
    return '1'

if __name__ == '__main__':
    app.run()