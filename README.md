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


# Some additionals:
- I decide to use a telegram python library because I though the main challenge here was not to make the telegram bot itself.
So I foccus on the main application and use the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).
- First I started the application with two modules inside the `stackoverflow` directory: `api` and `stackoverflow`.
But because the python imports I had some problems to write the unit test, then I though it was ok to join them in same file.
I was searching some python3.8 standart libraries to see how they approach this kind of module test, and saw that is
quite normal to join more then one basic class in the same file. Ex: [python calendar](https://github.com/python/cpython/blob/master/Lib/calendar.py) 
and it`s [unit test](https://github.com/python/cpython/blob/master/Lib/test/test_calendar.py).
For more complex applications I would use something like blueprint for a better module structure.
- More about the tests. I just wrote tests for functions that I created. I did not made unit test for the telegram bot resources 
that I warapped inside my functions in `bot.py`.
