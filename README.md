# Python version
- 3.8

obs: I tested it with python 3.6 and 3.7 and worked fine too.

# Install

The application uses pipenv to manager its dependencies. So you must have it installed then just run `pipenv install`

# Running

- first start the pipenv shell: `pipenv shell`
- running the command line application: `python app.py "text to search on stackoverflow"`
- running the telegram bot: `python bot.py`


# Running the tests

In project root

- `python stackoverflow/test_stackoverflow.py`
- `python test_bot.py`

# Telegram bot

The name of telegram bot is `stackoverflow_searcher` and to search something you just text the command
`/search and some text to search here`.
