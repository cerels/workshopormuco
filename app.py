import pickle
import json
import subprocess
from jinja2 import Environment, PackageLoader, select_autoescape

from flask import Flask, jsonify

app = Flask(__name__)

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def get_info(file_name, script_name):
    # Run the other Python file using the subprocess.run() method and pass additional arguments
    subprocess.run(["python", script_name])

    # Import the names from the file using the pickle module
    with open(file_name, "rb") as f:
        names = pickle.load(f)
        names = json.loads(names)
    return names


@app.route('/images', methods=['GET'])
def get_images():
    return get_info("images.pkl", "list.py")

@app.route('/networks', methods=['GET'])
def get_networks():
    return get_info("networks.pkl", "net.py")

@app.route('/flavors', methods=['GET'])
def get_flavors():
    return get_info("flavors.pkl", "flav.py")

@app.route('/keys', methods=['GET'])
def get_keys():
    return get_info("key.pkl", "key.py")

@app.route('/groups', methods=['GET'])
def get_groups():
    return get_info("group.pkl", "group.py")

@app.route('/')
def index():
    images = get_images()
    networks = get_networks()
    flavors = get_flavors()
    keys = get_keys()
    groups = get_groups()
    return env.get_template('index.html').render(
        images=images,
        networks=networks,
        flavors=flavors,
        keys=keys,
        groups=groups
    )

if __name__ == '__main__':
    app.run()
