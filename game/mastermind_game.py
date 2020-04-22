from flask import render_template, request, session
from flask import Blueprint
import user_dao as dao
import mastermind_logic as l_master
from entity.mastermindEntity import DictClass


objectMastermind = DictClass([{}])
mastermind_game_bp = Blueprint('game', 'mastermind')


@mastermind_game_bp.route("/game/", methods=['GET'])
def mastermind_game():
    objectMastermind.list_dict.clear()
    session['random_number'] = l_master.generate_number()
    return render_template('mastermind.html', title='Game', nav_bar=True)


# This function trigger the game.
@mastermind_game_bp.route("/mastermind/", methods=['GET', 'POST'])
def mastermind():
    number_typed = request.form['typed-number']
    to_send = l_master.master_mind(number_typed, session['random_number'])
    # Getting random number from session.
    random_from_session = session['random_number']
    objectMastermind.list_dict.append(to_send)
    session['list_dict'] = objectMastermind.list_dict

    if len(session['list_dict']) <= 9 or to_send['result'] == '1111':
        if to_send['result'] == '1111':
            if session.get('USERNAME') is not None:
                record = len(session['list_dict'])
                update_dict = {"record": record}
                dao.updating_user(session['USERNAME'], update_dict)
            return render_template('mastermind.html', title='game', tentativas=session['list_dict'], nav_bar=True,
                                   button_disabled=True, success=True, category='success',
                                   message_category='Parabéns, você acertou.',
                                   random_from_session=random_from_session), 200
        else:
            return render_template('mastermind.html', title='Game', tentativas=session['list_dict'], nav_bar=True), 200
    else:
        return render_template('mastermind.html', title='Game', tentativas=session['list_dict'], nav_bar=True,
                               button_disabled=True, success=True, category='danger',
                               message_category='Você chegou ao limite de tentativas, você perdeu.',
                               random_from_session=random_from_session), 200
