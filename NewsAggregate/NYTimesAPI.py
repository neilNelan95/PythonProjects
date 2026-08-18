class NYTimesAPI:

    import requests


    def __init__(self, api_key, api_secret):
        self.base_url = "https://api.nytimes.com/svc"
        self.api_key = api_key
        self.api_secret = api_secret


    def get_top_stories(self, section):
        full_url = f"{self.base_url}/topstories/v2/{section}.json"
        api_key = self.api_key

        r = self.requests.get(url =full_url, params = {"api-key" : api_key})

        r.raise_for_status()

        return r.json()

    #def search_articles()