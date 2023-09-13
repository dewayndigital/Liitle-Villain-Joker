import json

# Define the unique ID for the Ordinal
unique_id = "the-little-joker-ordinal-1"  # You can use a unique ID of your choice

# Define the collection name
collection_name = "The Little Joker"

# Define the CID, IPFS URL, and image link
cid = "bafybeieglw4kgnyfj2k2krqtgnm24n6zlkuoedi65gzt5sklqwsifbdvhi"
ipfs_url = "ipfs://bafybeieglw4kgnyfj2k2krqtgnm24n6zlkuoedi65gzt5sklqwsifbdvhi"
image_link = "https://bafybeigixatg24tmqsekpla4klge57fvkmueyecfgmhco7d3ozqysrys24.ipfs.nftstorage.link/?filename=Little+Villain+Joker.jpg"

# Define the traits for the Little Joker
traits = [
    {
        "trait_type": "Hair",
        "value": "Green"
    },
    {
        "trait_type": "Suit",
        "value": "Purple"
    },
    {
        "trait_type": "Shirt",
        "value": "Orange Button-Up"
    },
    {
        "trait_type": "Tie",
        "value": "Green"
    },
    {
        "trait_type": "Face Paint",
        "value": "The Joker"
    },
    {
        "trait_type": "Eyes",
        "value": "Blue"
    },
    {
        "trait_type": "Character",
        "value": "Little Joker"
    }
]

# Create the Ordinals collection entry
ordinal_collection = {
    "id": unique_id,
    "meta": {
        "name": collection_name,
        "icon": ipfs_url,  # Using the provided IPFS URL as the icon
    },
    "attributes": [
        {
            "trait_type": "CID",
            "value": cid
        },
        {
            "trait_type": "IPFS URL",
            "value": ipfs_url
        },
        {
            "trait_type": "Image Link",
            "value": image_link
        }
    ]
}

# Add the traits to the collection entry
ordinal_collection["attributes"].extend(traits)

# Save the Ordinals collection entry to a JSON file
with open('the-little-joker-ordinal.json', 'w') as json_file:
    json.dump(ordinal_collection, json_file, indent=2)

print("The Little Joker Ordinal collection JSON created successfully.")
