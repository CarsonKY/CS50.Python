# creating a dictionary with multiple values

dognames = [
    {"name": "Albert", "owner": "Kramers", "type": "cat"},
    {"name": "Mandy", "owner": "myself", "type": "corgi"},
    {"name": "Winston", "owner": "myself", "type": "corgi"},
    {"name": "Pookie", "owner": "Angell", "type": "mutt"}
]

for dogname in dognames:
    print(dogname["name"], dogname["owner"], sep=", ")