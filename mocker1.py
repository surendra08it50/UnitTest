
# ###***************** As a pytest fixture⚑********************************
import pytest
import requests
from requests_mock.mocker import Mocker


# def test_url(requests_mock: Mocker):
#     requests_mock.get('http://test.com', text='data')
#     assert 'data' == requests.get('http://test.com').text


###################As a function decorator⚑###############################
@Mocker()
def a_function(m):
    print(m)
    print("hello")
#      m.get('http://test.com', text='resp')
#      return requests.get('http://test.com').text

print(a_function())
#'resp'

# ###################As a context manager⚑########################

# import requests
# import requests_mock

# with requests_mock.Mocker() as m:
#      m.get('http://test.com', text='resp')
#      requests.get('http://test.com').text

# ##'resp'
