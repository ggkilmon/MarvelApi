from yaml import load, BaseLoader
from classes.marvelService import MarvelService

with open('./config.yaml', 'r') as file:
    config = load(file, Loader=BaseLoader)

svc = MarvelService(config['BaseUrl'], config['PublicKey'], config['PrivateKey'])
print(svc.request("comics"))