# Dictionaries are used to store elements in key:value pairs.
# Unordered,mutable and don't allow duplicates.
"""
info = {
    "name": "Wahida",
    "dob": "20-Nov-1997",
    "age": 27,
    "is_adult": True
}
print(info)
print(info.keys())
print(info.values())
print(info.items())
info["name"] = "Wahida Borbhuyan"
print(info.items())
print(info["age"])
"""
# ===============NESTED DICTIONARIES========================
"""
Students = {
    "name": "Wahida",
    "age ": 27,
    "Scores": {
        "Phy": 70,
        "Math": 80,
        "Chem": 80
    }

}
print(Students)
new_dict = {"place": "Digboi",
            "Country": "India"}
Whattodo = Students.update(new_dict)
print(Students.items())
"""
# ============================sets============================
# Sets is the collection of unordered items,no duplicate items.
# Each element in the set is unique and immutable.
# null_set = ()
collection = {1, 3, "Hello", "World"}
for x in collection:
    print(x)
collection.add("Wahida")  # Adds element to the set
print(collection)
collection.remove("Wahida")  # removes element to the set
print(collection)
collection.pop()  # Deletes random element to the set
print(collection)
collection.clear()  # Clears the set
print(collection)
