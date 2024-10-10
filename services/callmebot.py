import requests


class CallMeBot:

    def __init__(self):
        self.__base_url = ''
        self.__phone_number = ''
        self.__api_key = ''

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__phone_number}&text={message}&apikey={self.__api_key}'
        )
        return response.text
