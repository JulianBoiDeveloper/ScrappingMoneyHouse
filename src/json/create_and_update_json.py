import os
import json

# TODO : definir un boolean pour savoir si le fichier est vide
def create_and_update_json(data, json_name_file):
    try:
        with open(json_name_file, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    except json.decoder.JSONDecodeError:
        existing_data = []
    
    if isinstance(existing_data, list):
        for item in data:
            if isinstance(item, dict):
                found = False
                for existing_item in existing_data:
                    if isinstance(existing_item, dict) and set(item.keys()) == set(existing_item.keys()):
                        existing_item.update(item)
                        found = True
                        break
                if not found:
                    existing_data.append(item)
            else:
                existing_data.append(item)
    elif isinstance(existing_data, dict):
        for key in data:
            if key in existing_data:
                if isinstance(existing_data[key], list) and isinstance(data[key], list):
                    for item in data[key]:
                        if isinstance(item, dict):
                            found = False
                            for existing_item in existing_data[key]:
                                if isinstance(existing_item, dict) and set(item.keys()) == set(existing_item.keys()):
                                    existing_item.update(item)
                                    found = True
                                    break
                            if not found:
                                existing_data[key].append(item)
                        else:
                            existing_data[key].append(item)
                elif isinstance(existing_data[key], dict) and isinstance(data[key], dict):
                    existing_data[key].update(data[key])
                else:
                    existing_data[key] = data[key]
            else:
                existing_data[key] = data[key]
    else:
        existing_data = data
    
    with open(json_name_file, "w") as file:
        json.dump(existing_data, file)


# Exemple de données à insérer
data = [
    {
        "person1": {
            "name": "John",
            "age": 30,
            "city": "New York",
            "hobbies": ["reading", "traveling"]
        }
    },
    {
        "person2": {
            "name": "Jane",
            "age": 25,
            "city": "London",
            "hobbies": ["painting", "dancing"]
        }
    }
]

# On crée un fichier JSON vide pour commencer
with open("people.json", "w") as file:
    json.dump([], file)

# On ajoute la première entrée
data = [
    {
        "name": "John",
        "age": 30,
        "hobbies": ["reading", "running"]
    }
]
create_and_update_json(data, "people.json")

# On met à jour John avec un nouveau hobby
data = [
    {
        "name": "John",
        "hobbies": ["reading", "running", "swimming"]
    }
]
create_and_update_json(data, "people.json")

# On vérifie que John a bien été mis à jour
with open("people.json", "r") as file:
    people = json.load(file)
    john = next(p for p in people if p["name"] == "John")
    assert john == {
        "name": "John",
        "age": 30,
        "hobbies": ["reading", "running", "swimming"]
    }