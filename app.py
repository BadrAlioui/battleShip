import os
import random
from flask import Flask, session, request, redirect, url_for, render_template_string

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret')

TEMPLATE = '''
<!doctype html>
<title>Ultimate BATTLESHIPS</title>
<h1>Ultimate BATTLESHIPS</h1>
<p>{{ message }}</p>
<p>Turns: {{ turns }} / 5 | Score: You {{ player_score }} - Computer {{ computer_score }}</p>
<form method="post">
  Row (0-4): <input name="row" type="number" min="0" max="4" required>
  Col (0-4): <input name="col" type="number" min="0" max="4" required>
  <button type="submit">Guess</button>
</form>
<table border="1" cellpadding="5">
  {% for row in board %}
  <tr>
    {% for cell in row %}
      <td style="width:30px; text-align:center;">
      {% if cell == '$' %}
        🔥
      {% elif cell == 'X' %}
        ❌
      {% else %}
        {{ cell }}
      {% endif %}
      </td>
    {% endfor %}
  </tr>
  {% endfor %}
</table>
{% if game_over %}
  <p><strong>Game Over!</strong></p>
{% endif %}

<p><a href="{{ url_for('reset') }}">Restart Game</a></p>

'''

def init_game():
    session['player_board'] = [['-' for _ in range(5)] for _ in range(5)]
    session['computer_board'] = [['-' for _ in range(5)] for _ in range(5)]
    session['display_board'] = [['-' for _ in range(5)] for _ in range(5)]
    session['guessed'] = []
    session['turns'] = 0
    session['player_score'] = 0
    session['computer_score'] = 0

    def place(board, symbol):
        ships = set()
        while len(ships) < 4:
            r, c = random.randint(0, 4), random.randint(0, 4)
            if (r, c) not in ships:
                ships.add((r, c))
                board[r][c] = symbol

    place(session['player_board'], 'P')
    place(session['computer_board'], 'C')

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'player_board' not in session:
        init_game()

    message = ''
    game_over = False

    if request.method == 'POST':
        row = int(request.form['row'])
        col = int(request.form['col'])
        if (row, col) in session['guessed']:
            message = 'You already guessed that location.'
        else:
            session['guessed'].append((row, col))
            session['turns'] += 1
            if session['computer_board'][row][col] == 'C':
                session['display_board'][row][col] = '$'
                session['player_score'] += 1
                message = 'Hit!'
            else:
                session['display_board'][row][col] = 'X'
                message = 'Miss!'

            # Computer turn
            while True:
                r, c = random.randint(0, 4), random.randint(0, 4)
                if (r, c) not in session['guessed']:
                    session['guessed'].append((r, c))
                    break
            if session['player_board'][r][c] == 'P':
                session['player_board'][r][c] = '£'
                session['computer_score'] += 1

            if (session['turns'] >= 5 or
                session['player_score'] >= 4 or
                session['computer_score'] >= 4):
                game_over = True

    return render_template_string(
        TEMPLATE,
        board=session['display_board'],
        message=message,
        turns=session.get('turns', 0),
        player_score=session.get('player_score', 0),
        computer_score=session.get('computer_score', 0),
        game_over=game_over
    )

@app.route('/reset')
def reset():
    init_game()
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
