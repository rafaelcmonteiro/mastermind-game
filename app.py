from flask import Flask
import mastermind_logic as l_master
app = Flask(__name__)


@app.route("/generate-number", methods=['GET'])
def random_number():
    str_number = l_master.generate_number()
    return str_number


@app.route("/initialize", methods=['GET'])
def to_txt():
    resolution = l_master.to_txt()
    return resolution


@app.route("/mastermind/<string:number_typed>", methods=['GET'])
def mastermind(number_typed):
    to_send = l_master.master_mind(number_typed)
    return to_send


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
