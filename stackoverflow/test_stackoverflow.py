import unittest

from unittest.mock import patch

from stackoverflow import (StackOverFlow, Question, ApiResponse, ApiRequest,
        ApiResponseError)

class TestApiRequest(unittest.TestCase):
    def setUp(self):
        params = {'site': 'stackoverflow.com', 'q': 'search test'}
        self.request = ApiRequest(params)

    @patch('stackoverflow.requests.request')
    def test_a_request(self, mock_request):
        mock_request.return_value.status_code = 200

        response = self.request.send()

        self.assertIsInstance(response, ApiResponse)

class TestApiResponse(unittest.TestCase):
    def test_a_success_response_body(self):
        items = [{'test': True}]
        content = {'items': items}
        response = ApiResponse(200, content)

        self.assertEqual(response.body, items)

    def test_a_unsuccess_response_body(self):
        response = ApiResponse(404, None)

        with self.assertRaises(ApiResponseError):
            response.body

class TestStackOverFlowSearch(unittest.TestCase):
    @patch('stackoverflow.ApiRequest.send')
    def setUp(self, mock_request):
        self.title = 'test title'
        self.score = 0
        self.link = 'https://testlink.com'
        items = {'items': [
            {'title': self.title, 'score': self.score, 'link': self.link}
        ]}
        mock_request.return_value = ApiResponse(200, items)

        self.questions = StackOverFlow().search()

    def test_search_return(self):
        self.assertIsInstance(self.questions, list)

    def test_if_search_returns_questions(self):
        self.assertIsInstance(self.questions[0], Question)

    def test_question_content(self):
        question = self.questions[0]

        self.assertEqual(question.title, self.title)
        self.assertEqual(question.score, self.score)
        self.assertEqual(question.link, self.link)


if __name__ == '__main__':
    unittest.main()
