from protocol import get_all
from protocol import get_info
from protocol import get_head_position
from protocol import get_temp
from protocol import get_progress
from protocol import get_status
from protocol import set_temperature
from protocol import set_led

from flask import Flask
from flask import jsonify

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

PORT = 8899  # default port


@app.route("/")
def index():
    return ''

@app.route("/<string:ip_address>/all")
def all(ip_address):
    printer_info = get_all({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/info")
def info(ip_address):
    printer_info = get_info({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/head-location")
def head_location(ip_address):
    printer_info = get_head_position({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/temp")
def temp(ip_address):
    printer_info = get_temp({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)

@app.route("/<string:ip_address>/set-temp/<string:temp>")
def set_temp(ip_address, temp):
    printer_info = set_temperature({'ip': ip_address, 'port': PORT}, temp)
    return jsonify(printer_info)

@app.route("/<string:ip_address>/set-light/<string:red>/<string:green>/<string:blue>")
def set_light(ip_address, red, green, blue):
    printer_info = set_led({'ip': ip_address, 'port': PORT}, red, green, blue)
    return jsonify(printer_info)

@app.route("/<string:ip_address>/progress")
def progress(ip_address):
    printer_info = get_progress({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)


@app.route("/<string:ip_address>/status")
def status(ip_address):
    printer_info = get_status({'ip': ip_address, 'port': PORT})
    return jsonify(printer_info)
