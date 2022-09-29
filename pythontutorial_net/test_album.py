import unittest
from unittest.mock import MagicMock, patch

from album import find_album_by_id


class TestAlbum(unittest.TestCase):

    @patch('album.requests')
    def test_find_album_by_id_success(self, mock_requests):
        # mock the response
        print("mock_requests-----",type(mock_requests))
        mock_response = MagicMock()
        print("mock_requests-----",type(mock_response))
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'userId': 1,
            'id': 1,
            'title': 'hello',
        }

        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response

        # call the find_album_by_id and test if the title is 'hello'
        self.assertEqual(find_album_by_id(1), 'hello')