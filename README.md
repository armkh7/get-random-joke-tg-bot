# Get Random Joke 😂

A Telegram bot that provides random jokes from different categories using [JokeAPI](https://jokeapi.dev/).

## Features

* Choose a joke category
* Get a random joke
* Get another joke from the same category
* Change the selected category
* Supports Programming, Misc, Dark, Pun, Spooky, Christmas, and Any categories

## How It Works

Start the bot in Telegram and choose a category:

```text
💻 Programming
🎲 Misc
🌑 Dark
🎭 Pun
👻 Spooky
🎄 Christmas
🎯 Any
```

The bot then fetches a random joke from JokeAPI and sends it to you.

## Technologies

* Python
* Telegram Bot API
* JokeAPI

## Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/get-random-joke.git
cd get-random-joke
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your Telegram bot token to `.env` and run:

```bash
python bot.py
```

## API

Jokes are provided by [JokeAPI](https://jokeapi.dev/).

## License

This project is for learning and portfolio purposes.
