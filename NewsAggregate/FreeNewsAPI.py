#Creation of an API wrapper which encompases several NY Times endpoints.
class FreeNewsAPI:
    #The requests library offers a suite of tools for simple API requests
    import requests

     #Here we define the API Wrapper object to be used in our Main module. 
    def __init__(self, api_key):
        self.base_url = "https://api.freenewsapi.io/v1"
        self.api_key = api_key
        

    def search_articles(self, query):
        full_url = f"{self.base_url}/search"
        requests.get(url=full_url, params = {"q" : query}, headers= {"x-api-key" : self.api_key})