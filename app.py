import sys

from stackoverflow.stackoverflow import StackOverFlow

def main():
    text_to_search = sys.argv[0]
    questions = StackOverFlow().search(text_to_search)

    for question in questions:
        print('----------x----------')
        print(f'Title: {question.title}')
        print(f'Votes: {question.score}')
        print(f'Link: {question.link}')

if __name__ == '__main__':
    main()
