import json

variable = {"name" : "Paweł",
            "surname" : "Admczyk",
            "age" : 36,
            "pets" : ["dog", "cat", "fish"]
            }

print(json.dumps(variable, indent=4, sort_keys=True))