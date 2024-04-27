TABLE_SIZE = 5

contacts = [
    ("Bob", 1234),
    ("Ikram", 5678),
    ("Pankaj", 9101),
    ("Peter", 2134),
    ("Jo", 1516),
    ("Maria", 1718),
]


def my_hash_function(key):
    return len(key) % TABLE_SIZE  # There are many possible hash functions.


def insert(contact, hash_table):
    if None not in hash_table:
        print("Hash table is full.")
        return
    index = my_hash_function(contact[0])  # contact[0] is the key.
    print(f"Hash value of key is {index}")
    while hash_table[index] is not None:
        index += 1
        if index >= TABLE_SIZE:
            index = 0
    print(f"Inserting {contact} at index {index}.")
    hash_table[index] = contact


def lookup(search_key, hash_table):
    index = my_hash_function(search_key)
    mark = index  # Keep track of where we started to avoid infinite loop.
    while hash_table[index] and hash_table[index][0] != search_key:
        index += 1
        if index >= TABLE_SIZE:
            index = 0
        if index == mark:
            return None
    if hash_table[index] is not None:
        return hash_table[index]


my_hash_table = [None] * TABLE_SIZE

# Add some contacts
for contact in contacts:
    insert(contact, my_hash_table)
    print(my_hash_table)
    # input("Press Enter to continue.")
    print()

print("Search results:")
print(lookup("Pam", my_hash_table))
print(lookup("Pankaj", my_hash_table))
print(lookup("Jo", my_hash_table))
