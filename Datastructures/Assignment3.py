person_details = {
    "name": "Narendra Modi",
    "age": 67,
    "salary": 2_00_000,
    "role": "CM of Gujarat",
    "role": "PM of India",  # latest will be stored

}
for index,(each_key, each_value) in enumerate(person_details.items()):
    print(f"{each_key}\t{each_value}")