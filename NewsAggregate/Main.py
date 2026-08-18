from NYTimesAPI import NYTimesAPI

class Main:
    def __init__(self):
        api_key = "LaNqbcVgwmvgVplqa0t5wgaa0ZYQupOYVQhe3JzWEhbikY01"
        api_secret = "OA7AO58gIfXYrMap0alDK2EkEDLyfmeILrGFOTsNeVXyyt9G4VDygVwtvkmJa0qt"
        self.nyt_client = NYTimesAPI(api_key, api_secret)


    def run(self):
        technology = self.nyt_client.get_top_stories("technology")["results"]

        titles = []

        for article in technology :
            titles.append(article["title"])

        print(titles)

Main().run()