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

## Deploy to Vercel

Vercel uses the FastAPI webhook at `/api/webhook`; it cannot run
`app.run_polling()` because serverless functions are not long-lived processes.

Add these Vercel environment variables:

```text
TELEGRAM_BOT_TOKEN
TELEGRAM_WEBHOOK_SECRET
```

After deployment, register the webhook once:

```bash
curl -X POST \
  "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebhook" \
  -d "url=https://YOUR_VERCEL_DOMAIN.vercel.app/api/webhook" \
  -d "secret_token=$TELEGRAM_WEBHOOK_SECRET"
```

## API

Jokes are provided by [JokeAPI](https://jokeapi.dev/).

## License

This project is for learning and portfolio purposes.
