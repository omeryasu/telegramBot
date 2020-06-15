import requests
import json
import configparser as cp


class telegramChatBot():

    def __init__(self, config):
        self.token = self.read_token(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset = None):
        url = self.base + "/get_updates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_massage(self, msg, chat_id):
        url = self.base + "sendMassage?chat_id={}&text={}".format(chat_id,msg)
        if url is not None:
            requests.get(url)

    def read_token(self, config):
        parser = cp.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

