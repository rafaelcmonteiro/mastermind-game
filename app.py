from flask import Flask, render_template
import mastermind_logic as l_master

app = Flask("mastermind")


@app.route("/", methods=['GET'])
def index():
    lista = [
        {'name': 'Rafael', 'user': 'rafael10'},
        {'name': 'Anny', 'user': 'rafael1011'}
    ]
    return render_template('index.html', titulo='login', usuarios=lista)


@app.route("/generate-number/", methods=['GET'])
def random_number():
    str_number = l_master.generate_number()
    return str_number, 200


@app.route("/initialize/", methods=['GET'])
def to_txt():
    resolution = l_master.to_txt()
    return resolution, 200


@app.route("/mastermind/<string:number_typed>/", methods=['GET'])
def mastermind(number_typed):
    to_send = l_master.master_mind(number_typed)
    return to_send, 200


@app.errorhandler(404)
def page_not_found(error):
    return 'A página não existe.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)