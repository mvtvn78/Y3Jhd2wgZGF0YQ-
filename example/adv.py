import requests


def log():
    def __init__(self):
        self.s = requests.session()
        # Headers
        headers = {"accept-language", "sec-xx-xx", "user-agent"}
        # Apply
        self.s.headers.update(headers)
        data = {"atr1": "val1"}
        #
        sg_in = self.s.post("endpoint", timeout=10)
        self.s.cookies.update(sg_in.cookies)

    def get_ck(self):
        return self.s.cookies.get_dict()

    def hanle():
        pass
