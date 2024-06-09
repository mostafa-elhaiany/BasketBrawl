import requests

class Poller:
    def __init__(self, poll_id) -> None:
        self.url = f'https://api.strawpoll.com/v3/polls/{poll_id}/results'
        self.headers = {
        'Accept': 'application/json',
        'X-API-Key': "123"
        }
        self.votes = [0,0]
        
    def apply_results(self, player1, player2):
        if(self.votes[0]>self.votes[1]):
            player1.add_points(5)
        elif(self.votes[1]>self.votes[0]):
            player2.add_points(5)
        else:
            player1.add_points(5)
            player2.add_points(5)

    def get_results(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            option_1_votes = data["poll_options"][0]["vote_count"]
            option_2_votes = data["poll_options"][1]["vote_count"]
            self.votes = [option_1_votes, option_2_votes]
            return self.votes
        else:
            print(response.text)
            return self.votes
