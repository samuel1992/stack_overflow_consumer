import unittest

from stackoverflow.stackoverflow import Question

from bot import message

class TestssageBot(unittest.TestCase):
    def setUp(self):
        self.questions = [
            Question(title='teste', score=0, link=''),
            Question(title='teste2', score=1, link='')
        ]

    def test_message_reply_format(self):
        got = message(self.questions)
        want = 'Title: teste2\nVotes: 1\nLink: \n\n'
        want += 'Title: teste\nVotes: 0\nLink: \n\n'

        self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
