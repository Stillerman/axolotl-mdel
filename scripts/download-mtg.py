from tqdm import tqdm
from datasets import load_dataset
import json

dataset = load_dataset("MechaCroc/magic-the-gathering")

def prettyCard(card):
    text = (card['text'] or 'None').replace('\n', ' ')
    return f"Name:{card['name']}|ManaCost:{card['manaCost']}|Type:{card['type']}|Text:{text}|Power:{card['power']}|Toughness:{card['toughness']}"

with open("./mtg.txt", "w") as f:
    for card in tqdm(dataset['train_clean']): 
        # jsonl = {"text": prettyCard(card)}
        # f.write(json.dumps(jsonl) + "\n")
        f.write(prettyCard(card) + "\n")