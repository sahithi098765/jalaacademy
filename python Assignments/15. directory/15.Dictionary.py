#Dictionary


#Creating a dictionary with 5 key value pairs.
d= {1: "Sahi", 2: "Raju", 3: "Likki", 4: "Devi", 5: "Ram"}

#1.1 Adding a value.
d[6] = "Sam"
print("After Adding:",d)

# 1.2 Updating a value
d[3] = "Rosy"  
print("After Updating:", d)

# 1.3 Accessing a value
print("Student with ID 4:", d[4])

# 1.4 Creating a nested dictionary
nd = {
    1: {"ID": 1, "Name": "Raju"},
    2: {"ID": 2, "Name": "Ravi"},
}

# 1.5 Accessing a value from nested dictionary
print("Name of student 2:", nd[2]["Name"])

# 1.6 Printing all keys
print("Keys in dictionary:", d.keys())

# 1.7 Deleting a value
del d[4]
print("After Deletion:", d)
