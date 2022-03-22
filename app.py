import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to the mission demo for AQ"

@app.route('/mission-statement')
def hello():
    return 'Migrate on-prem Openstack to Azure Openshift (ARO)'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
