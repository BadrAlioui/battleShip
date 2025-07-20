# Ultimate BATTLESHIPS

Ultimate BATTLESHIPS is a modern take on the classic naval warfare game, implemented in Python. Engage in strategic combat on a 5×5 grid, either directly in your terminal or via the Heroku mock terminal.

[**Play Now**](https://app-battleship.herokuapp.com/)

---

## Getting Started

1. **Launch the game** locally by running:

   ```bash
   python battlefield.py
   ```

   or play online through the Heroku mock terminal.
2. When prompted, enter your **name** (letters only).
3. You and the computer each have **4 ships** hidden on a **5×5 grid**.
4. You have up to **5 turns** per session:

   1. Enter a **row** (0–4) and **column** (0–4) to fire upon.
   2. A successful **hit** (🔥) sinks the opponent’s ship; a **miss** (❌) marks an empty cell.
   3. The computer then makes its move.
5. The side with the most sunk ships after all turns (or the first to 4 hits) is declared the **winner**.

---

## Key Features

* **Randomized Ship Placement**: Four ships are automatically positioned without overlap for both players.
* **Terminal Feedback**: Clear, color-coded symbols indicate hits, misses, and untouched cells.
* **Turn-Based Mechanics**: Players alternate turns, with the human player always firing first.
* **Independent Guess Tracking**: The game prevents repeat guesses by maintaining separate histories for player and computer.
* **Live Scoreboard**: Current turn count and score are displayed continuously.

---

## Input Validation

* **Name**: Letters only (no numbers or special characters).
* **Coordinates**: Integers between 0 and 4 inclusive.
* **Duplicate Guesses**: The game disallows firing at the same coordinates more than once.
* **Error Handling**: Invalid inputs trigger clear, user-friendly error messages.

---

## Exiting & Restarting

* Type `exit` at any prompt to terminate the current game session.
* To start a new game after completion, simply rerun the script.

---

## Testing & Quality

* **Manual Tests**: Extensively tested in both GitPod and Heroku mock terminals, covering valid and invalid input scenarios.
* **PEP8 Compliance**: The codebase is linted with `flake8` and adheres to PEP8 standards.

  ```bash
  pip install flake8
  flake8 .
  ```

---

## Known Limitations

No critical issues at present. All anticipated edge cases and invalid inputs are gracefully managed.

---

## Deployment Guide

1. **Create a Heroku application** in the EU region:

   ```bash
   heroku create <your-app-name> --region eu
   ```
2. **Configure environment variable** `PORT` = `8000` under **Settings > Config Vars**.
3. **Prepare deployment files**:

   * `requirements.txt`:

     ```bash
     pip freeze > requirements.txt
     ```
   * `.python-version`: set to `3.13`
   * `Procfile`:

     ```
     web: gunicorn app:app
     ```
4. **Deploy to Heroku**:

   ```bash
   git add .
   git commit -m "Setup Heroku deployment"
   git push heroku main
   heroku ps:scale web=1
   ```

---

## Acknowledgements

* **Flask**: Elegant web framework – [flask.palletsprojects.com](https://flask.palletsprojects.com/)
* **Gunicorn**: Production-grade WSGI server – [gunicorn.org](https://gunicorn.org/)
* **Colorama**: Cross-platform terminal colors – [pypi.org/project/colorama](https://pypi.org/project/colorama/)
* Heroku deployment scaffold provided by Code Institute.
* Developed by **Badr Alioui**.
