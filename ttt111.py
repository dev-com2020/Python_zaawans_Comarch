import json
import random
import unittest
import requests
import responses



def random_cat_fact():
    response = requests.get('https://cat-fact.herokuapp.com/facts').json()
    facts = [fact['text'] for fact in response['all']]
    return random.choice(facts)


class RandomCatFactsTestCase(unittest.TestCase):

    @responses.activate
    #@mock.patch("requests.get")
    def test_random_cat_fact(self):
        facts = ["A cat has five toes on his front paws"]
        content = {
            'all': [{'text': fact} for fact in facts]
        }
        responses.add(
            responses.GET,
            'https://cat-fact.herokuapp.com/facts',
            body=json.dumps(content),
            content_type='application/json')

        fact = random_cat_fact()
        self.assertIn(fact, facts)


if __name__ == "__main__":
    unittest.main()
