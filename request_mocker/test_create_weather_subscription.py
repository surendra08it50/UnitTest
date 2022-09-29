import requests_mock
import unittest

from create_weather_subscription import create_weather_subscription

class TestSubscribeWeather(unittest.TestCase):
    """
    Test create_weather_subscription function
    """

    @classmethod
    def setUpClass(cls):
        cls.user_id = 10
        cls.package_id = 'dummy-package-id-2'
        cls.start_date = '2020-10-01'
        cls.end_date = '2020-12-31'

    def test_create_weather_subscription_success(self):
        """
        Simply test when subscription is created successfully.
        """
        return_value = {
            'id': 101,
            "user_id": self.user_id,
            "package_id": self.package_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        with requests_mock.Mocker() as rm:
            rm.post('https://dummy-weather-service.com/weather/subscribe/', json=return_value, status_code=201)
            response = create_weather_subscription(
                self.user_id, self.package_id, self.start_date, self.end_date
            )

            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",response.status_code)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",response.content)
            # self.assertEqual(response, 'Weather data subscribed successfully!')
            self.assertEqual(response.status_code, 201)
            
            
            
            
            
            
            

    # def test_create_weather_subscription_authorization_error(self):
    #     """
    #     Test when subscription failed because of authorization error.
    #     """
    #     return_value = {'message': 'Unauthorized'}
    #     with requests_mock.Mocker() as rm:
    #         rm.post('https://real-weather-service.com/weather/subscribe/', json=return_value, status_code=401)
    #         response = create_weather_subscription(
    #             self.user_id, self.package_id, self.start_date, self.end_date
    #         )

    #         self.assertEqual(response, 'Unauthorized')

    # def test_create_weather_subscription_overlap(self):
    #     """
    #     Test when subscription failed because there is overlapping subscription for
    #     the dates specified for the user.
    #     """
    #     return_value = {'message': 'New subscription overlaps existing subscription'}
    #     with requests_mock.Mocker() as rm:
    #         rm.post('https://real-weather-service.com/weather/subscribe/', json=return_value, status_code=400)
    #         response = create_weather_subscription(
    #             self.user_id, self.package_id, self.start_date, self.end_date
    #         )

    #         self.assertEqual(response, 'New subscription overlaps existing subscription')


# if __name__ == '__main__':
#     unittest.main()