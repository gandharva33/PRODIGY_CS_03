# 🔐 Password Complexity Checker

A beginner-friendly Python terminal tool that analyses password strength in real time, scores it across five security rules, and gives actionable tips to help you create stronger passwords.

---

## 📋 Table of Contents

- [Demo](#demo)
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Strength Scoring](#strength-scoring)
- [Project Structure](#project-structure)
- [Concepts Used](#concepts-used)
- [Contributing](#contributing)
- [License](#license)

---

## Demo

```
  Welcome to the Password Strength Checker!
  (Your password is hidden as you type)

  Enter a password to check (or press Enter to quit): ············

========================================
       PASSWORD STRENGTH REPORT
========================================

  Strength     : [==========] Very Strong
  Rules passed : 5 / 5

  Checklist:
✔  12+ characters
✔  Uppercase letter
✔  Lowercase letter
✔  Number
✔  Special character

  Tips:
    → Excellent! Save this password in a password manager.

========================================
```

---

## Features

- ✅ **Five-rule security check** — length, uppercase, lowercase, numbers, and special characters
- 🚫 **Common password detection** — flags passwords like `password`, `123456`, and `qwerty`
- 📊 **Visual strength bar** — instant at-a-glance feedback with an ASCII progress bar
- 💡 **Personalised tips** — specific advice for every rule that fails
- 🔒 **Hidden input** — password is masked as you type using `getpass`
- 🔁 **Loop mode** — check as many passwords as you like in one session

---

## How It Works

Every password is evaluated against five rules:

| Rule | Requirement |
|------|-------------|
| Length | At least 12 characters |
| Uppercase | At least one letter A–Z |
| Lowercase | At least one letter a–z |
| Number | At least one digit 0–9 |
| Special character | At least one symbol e.g. `!`, `@`, `#`, `$` |

The number of rules passed maps to a strength label:

```
0–1 rules (or common password) → Very Weak  [=         ]
2 rules                        → Weak       [===       ]
3 rules                        → Fair       [=====     ]
4 rules                        → Strong     [=======   ]
5 rules                        → Very Strong[==========]
```

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required — uses only the Python standard library

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/password-complexity-checker.git

# Navigate into the project folder
cd password-complexity-checker
```

### Run the Program

```bash
python password_complexity_checker.py
```

---

## Usage

1. Run the script as shown above.
2. Type a password when prompted — it will be hidden as you type.
3. Read the strength report and follow the tips.
4. Press **Enter** with no input to quit.

**Example session:**

```
Enter a password to check (or press Enter to quit): ············

  Strength     : [=======   ] Strong
  Rules passed : 4 / 5

  Checklist:
✔  12+ characters
✔  Uppercase letter
✔  Lowercase letter
✔  Number
✘  Special character

  Tips:
    → Add a special character (e.g. !, @, #, $).
```

---

## Strength Scoring

| Label | Score | Rules Passed | What It Means |
|-------|-------|--------------|---------------|
| Very Weak | 1 | 0–1 or common password | Guessable in seconds |
| Weak | 2 | 2 | Easily cracked with basic tools |
| Fair | 3 | 3 | Acceptable but improvable |
| Strong | 4 | 4 | Good password with one small gap |
| Very Strong | 5 | 5 | All rules passed — recommended |

> **Note:** Even if a password passes multiple rules, it is automatically rated **Very Weak** if it appears in the built-in common passwords list.

---

## Project Structure

```
password-complexity-checker/
│
├── password_complexity_checker.py   # Main program
└── README.md                        # This file
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `check_password(password)` | Runs all five rule checks, calculates score, builds tips list; returns a result dictionary |
| `show_results(result)` | Prints the formatted terminal report with strength bar, checklist, and tips |
| `main` (script block) | Runs the input loop using `getpass`; exits cleanly on empty input |

---

## Concepts Used

This project is a great way to practise the following Python fundamentals:

- **Regular expressions** (`re` module) — pattern matching for character types
- **String methods** — `len()`, `.lower()`, membership with `in`
- **Boolean logic** — `True`/`False` flags for each rule
- **`sum()` on a list of booleans** — counting passed rules (`True == 1`, `False == 0`)
- **Dictionaries** — storing and passing structured results between functions
- **`getpass` module** — secure hidden input at the OS level
- **`while True` loop** — continuous prompt until the user exits

---

## Contributing

Contributions are welcome! Here are a few ideas for extending the project:

- Add more entries to the `COMMON_PASSWORDS` list (or load from a file)
- Estimate crack time based on password entropy
- Add a password generator that meets all five rules
- Build a GUI version using `tkinter`

To contribute:

```bash
# Fork the repo, then create a branch
git checkout -b feature/your-feature-name

# Make your changes and commit
git commit -m "Add your feature description"

# Push and open a Pull Request
git push origin feature/your-feature-name
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

> Built with Python 🐍 — no external dependencies required.
