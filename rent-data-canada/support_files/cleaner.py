import json

data = []
with open("unique_data_sets.json", "r") as file:
    data = json.loads(file.read())


with open("cleaned_up_datasets.json", "a+") as cufile:
    cldata = list(set(map(tuple, data)))
    cufile.write(json.dumps(cldata))
