import pandas as pd
import numpy as np
import sys

def create_item_df():
    amulet_data = pd.read_csv("amulets.csv")
    ring_data = pd.read_csv("rings.csv")
    item_df = amulet_data.merge(right=ring_data,how="outer")
    item_df.index = item_df["item_name"]
    return item_df

def display_data(item_name):
    capitalized_name = ""
    capped_words = [word.capitalize() + " " for word in item_name.split(' ')]
    for word in capped_words:
        capitalized_name += word
    item_df = create_item_df()
    entry = item_df.loc[capitalized_name[:-1]]
    print(entry)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        name = sys.argv[1].lower()
    else:
        name = input("Item name: ")
    item_df = create_item_df()
    lower_items = [i.lower() for i in item_df["item_name"].values]
    if name.lower() in lower_items:
        display_data(name.lower())
    else:
        print(f"No data for {name}")
