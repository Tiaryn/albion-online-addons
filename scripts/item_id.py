# Helper script used to generate backend/assets/item_ids.txt
# Args: items.xml generated by ao-id-extractor
# Usage python scripts/item_id.py items.xml > backend/assets/item_ids.txt

import json
import re
import sys
import xml.etree.ElementTree as ET

file = sys.argv[1]

id = 0
def add_item(db, name):
    global id

    db[id] = name
    print(f'{id},{name}')
    id = id + 1

nd = {}
tree = ET.parse(file)
root = tree.getroot()

for child in root:
    if not 'uniquename' in child.attrib:
        continue

    add_item(nd, child.attrib['uniquename'])


    ench = child.find("enchantments")

    if ench:
        for e in ench:
            add_item(nd, f"{child.attrib['uniquename']}@{e.attrib['enchantmentlevel']}")

