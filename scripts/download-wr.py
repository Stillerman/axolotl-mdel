from datasets import load_dataset
from tqdm import tqdm
import json

ds = load_dataset("bigcode/the-stack-dedup", data_dir="data/mathematica", split="train", streaming=True)

# write to file
with open("/workspace/axolotl-mdel/mathematica.txt", "w") as f:
    for example, n in tqdm(zip(ds, range(1000))):
        # completion raw corpus for axoltol
        jsonl = {"text": example["content"]}
        f.write(json.dumps(jsonl) + "\n")