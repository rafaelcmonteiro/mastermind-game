from flask import Flask, render_template
import mastermind_logic as l_master

app = Flask("mastermind")


# Test


@app.route("/", methods=['GET'])
def index():
    dict_user = {"name": "Rafael", "best_time": 5}
    return render_template('perfil.html', titulo='login', usuario=dict_user)


# Test
@app.route("/game/", methods=['GET'])
def mastermind_game():
    dict_score = {"": "Rafael", "best_time": 5}
    return render_template('mastermind.html', titulo='game', usuario=dict_score)


@app.route("/generate-number/", methods=['GET'])
def random_number():
    str_number = l_master.generate_number()
    return str_number, 200


# This function insert the random number on user dict.
@app.route("/initialize/<string:user_name>/", methods=['GET'])
def to_db(user_name):
    resolution = l_master.inserting_random(user_name)
    return resolution, 200


# This function trigger the game.
@app.route("/mastermind/<string:number_typed>/<string:user>/", methods=['GET'])
def mastermind(number_typed, user):
    to_send = l_master.master_mind(number_typed, user)
    return to_send, 200


@app.errorhandler(404)
def page_not_found(error):
    return 'A página não existe.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
