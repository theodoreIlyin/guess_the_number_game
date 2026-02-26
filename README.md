# 🎯 Guess the Number Game

A simple console-based Python game where the player tries to guess a randomly generated number between **1 and 10**.

---

## 📌 Description

The program randomly selects a number, and the player attempts to guess it.

After each guess, the game provides hints:

* **"Higher"** — if the secret number is greater
* **"Lower"** — if the secret number is smaller
* **Victory message** when the number is guessed 🎉

The game also tracks the number of attempts.

---

## ⚙️ How It Works

The game is built using several functions:

| Function            | Description                               |
| ------------------- | ----------------------------------------- |
| `generate_number()` | Generates a random number from 1 to 10    |
| `get_user_guess()`  | Gets and validates user input             |
| `check_guess()`     | Compares the guess with the secret number |
| `play_game()`       | Controls the game flow                    |

---

## 🧠 Game Logic

1. A random number is generated
2. The player enters a guess
3. The program checks:

   * If the guess is too low → prints **"Higher"**
   * If the guess is too high → prints **"Lower"**
   * If correct → player wins
4. The number of attempts is counted

---

## ▶️ How to Run

Make sure you have **Python 3** installed.

Run the script:

```bash
python main.py
```

---

## 🛡 Input Validation

If the player enters something that is not a number, the game will not crash 🙂

It will display:

```
ERROR! That's not a number! Try again.
```

---

## 📊 Statistics

The game uses a `stats` dictionary to track wins:

```python
stats['wins']
```

---

## 🚀 Possible Improvements

You can expand the game by adding:

* Replay option
* Difficulty levels
* Best score tracking
* Custom number range
* Saving statistics

---

## 👨‍💻 Author

A practice project for learning:

* Functions
* Loops
* Error handling
* Random number generation

---
