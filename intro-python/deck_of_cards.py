# Python 3.10.5
# Coding = utf - 8
# 模版有待完善


import requests

response = requests.get('https://deckofcardsapi.com/api/deck/new/')

if response.status_code == 200:
    deck_id = response.json()['deck_id']
    requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/")
else:
    print(f"Request unsuccessful. Status code: {response.status_code}")
    exit()

draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")

draw = draw_response.json()

i = 1

for card in draw['cards']:
    print(f"Card {i} is {card['value']} of {card['suit']}")
    i +=1