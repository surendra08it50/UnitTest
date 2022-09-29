from unittest import TestCase
from unittest.mock import patch, Mock
import json

class TestBlog(TestCase):
    @patch('main_request.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'message body'
            }
        ]

        response = blog.posts()
        print(response)
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)



"""
You can see from the code snippet that the test_blog_posts function is decorated with the @patch decorator. When a function is decorated using @patch, a mock of the class, method or function passed as the target to @patch is returned and passed as an argument to the decorated function.

In this case, @patch is called with the target main.Blog and returns a Mock which is passed to the test function as MockBlog. It is important to note that the target passed to @patch should be importable in the environment @patch is being invoked from. In our case, an import of the form from main import Blog should be resolvable without errors.

Also, note that MockBlog is a variable name to represent the created mock and can be you can name it however you want.

Calling blog.posts() on our mock blog object returns our predefined JSON. Running the tests should pass.

"""        