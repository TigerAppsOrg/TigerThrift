import requests
import json
import base64
import os


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]


class ActiveDir:
    def __init__(self):
        self.configs = Configs()

    # wrapper function for _getJSON with the users endpoint.
    def get_user(self, netid):
        return self._getJSON(self.configs.USERS, uid=netid)

    """
    This function allows a user to make a request to 
    a certain endpoint, with the BASE_URL of 
    https://api.princeton.edu:443/active-directory/1.0.5

    The parameters kwargs are keyword arguments. It
    symbolizes a variable number of arguments 
    """

    def _getJSON(self, endpoint, **kwargs):
        req = requests.get(
            self.configs.BASE_URL + endpoint,
            params=kwargs if "kwargs" not in kwargs else kwargs["kwargs"],
            headers={"Authorization": "Bearer " + self.configs.ACCESS_TOKEN},
        )
        text = req.text

        # Check to see if the response failed due to invalid credentials
        text = self._updateConfigs(text, endpoint, **kwargs)

        return json.loads(text)

    def _updateConfigs(self, text, endpoint, **kwargs):
        if text.startswith("<ams:fault"):
            self.configs._refreshToken(grant_type="client_credentials")

            # Redo the request with the new access token
            req = requests.get(
                self.configs.BASE_URL + endpoint,
                params=kwargs if "kwargs" not in kwargs else kwargs["kwargs"],
                headers={"Authorization": "Bearer " + self.configs.ACCESS_TOKEN},
            )
            text = req.text

        return text


class Configs:
    def __init__(self):
        self.CONSUMER_KEY = "rnyPfDVzQiAiEvdtICGvwRzICf4a"
        self.CONSUMER_SECRET = "9TVFeND29h2ygtx2XQCsReRoPm0a"
        self.BASE_URL = "https://api.princeton.edu:443/active-directory/1.0.5"
        self.USERS = "/users"
        self.REFRESH_TOKEN_URL = "https://api.princeton.edu:443/token"
        self._refreshToken(grant_type="client_credentials")

    def _refreshToken(self, **kwargs):
        req = requests.post(
            self.REFRESH_TOKEN_URL,
            data=kwargs,
            headers={
                "Authorization": "Basic "
                + base64.b64encode(
                    bytes(self.CONSUMER_KEY + ":" + self.CONSUMER_SECRET, "utf-8")
                ).decode("utf-8")
            },
        )
        text = req.text
        response = json.loads(text)
        self.ACCESS_TOKEN = response["access_token"]


if __name__ == "__main__":
    netid = "ntyp"
    r = ActiveDir().get_user(netid)
    if not r:
        err = f"Failed to get user data for {netid}"
        print(err)
        raise Exception(err)
    r = r[0]

    if r["pustatus"] != "undergraduate":
        err = f"{netid} is not an undergraduate"
        print(err)
        raise Exception(err)

    user_info = {
        "first_name": r["displayname"].split(" ")[0],
        "last_name": r["sn"],
        "full_name": r["displayname"],
        "netid": netid,
        "email": r["mail"],
        "class_year": r["department"].split(" ")[-1],
    }

    print(user_info)
