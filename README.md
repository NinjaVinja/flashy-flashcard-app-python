# Flashy 🃏 — French Flashcard App

A simple desktop flashcard app built with **Python** and **Tkinter** to help you learn French vocabulary. It shows a French word, flips after 3 seconds to reveal the English translation, and keeps track of which words you already know — so you only get quizzed on the ones you don't.

## Features

- 🖼️ Card flips automatically after 3 seconds (French → English)
- ✅ Mark a word as "known" — it's removed from future rounds and saved to `data/words_to_learn.csv`
- ❌ Mark a word as "unknown" — it stays in the pool and a new random card is shown
- 💾 Progress persists between runs — next time you open the app, it picks up from `words_to_learn.csv` if it exists, otherwise starts fresh from `french_words.csv`

## Project Structure

```
flashy/
├── main.py
├── data/
│   ├── french_words.csv       # full word list (French, English)
│   └── words_to_learn.csv     # auto-generated as you learn words
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── README.md
```

## Requirements

- Python 3.x
- pandas

Install dependencies:
```bash
pip install pandas
```

## How to Run

```bash
python main.py
```

## How It Works

1. A random French word is shown on the card.
2. After 3 seconds, the card flips to show the English translation.
3. Click ✅ if you knew the word — it's removed from the learning list and saved.
4. Click ❌ if you didn't — a new random word appears.
5. Your progress is saved automatically to `data/words_to_learn.csv`, so the next session only quizzes you on words you haven't marked as known yet.

## Credits

Word data (`french_words.csv`) and card images used for a language-learning flashcard exercise.
