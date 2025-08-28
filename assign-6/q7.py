
sampleDict = {'a': 100, 'b': 300, 'c': 400}


# value_to_check = 200

value_to_check = 100
if value_to_check in sampleDict.values():
    print(f"{value_to_check} exists in the dictionary")
else:
    print(f"{value_to_check} does not exist in the dictionary")

