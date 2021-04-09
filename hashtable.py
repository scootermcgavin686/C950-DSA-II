

# # HashTable class using chaining.
# class ChainingHashTable:
#     # Constructor with optional initial capacity parameter.
#     # Assigns all buckets with an empty list.
#     def __init__(self, initial_capacity=40):
#         # initialize the hash table with empty bucket list entries.
#         self.table = []
#         for i in range(initial_capacity):
#             self.table.append([])
#
#     # Inserts a new item into the hash table.
#     def insert(self, key, item):
#         # get the bucket list where this item will go.
#         bucket = hash(key) % len(self.table)
#         bucket_list = self.table[bucket]
#
#         # update key if it is already in the bucket
#         for kv in bucket_list:
#             # print(key value)
#             if kv[0] == key:
#                 kv[1] = item
#                 return True
#
#         # insert the item to the end of the bucket list.
#         key_value = [key, item]
#         bucket_list.append(key_value)
#         return True
#
#     # Searches for an item with matching key in the hash table.
#     # Returns the item if found, or None if not found.
#     def search(self, key):
#         # get the bucket list where this key would be.
#         bucket = hash(key) % len(self.table)
#         bucket_list = self.table[bucket]
#
#         # search for the key in the bucket list
#         for key_value in bucket_list:
#             # find the item's index and return the item that is in the bucket list.
#             if key_value[0] == key:
#                 return key_value[1]
#         return None
#
#
# myHash = ChainingHashTable()


class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, value):
        hash_key = hash(key) % len(self.table)
        key_exists = False
        bucket = self.table[hash_key]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))


    def search(self, key):
        hash_key = hash(key) % len(self.table)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.table)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Item deleted for key {}'.format(key))
        else:
            print('Key {} not found'.format(key))


myHash = ChainingHashTable()
print()



# These statements were used to see if my hash function is working properly
# I believe the problem is how I have my for loops loop through the len(myHash.table)
# and now it is only 10 buckets deep. Will have to think of a different way to have
# it loop through list.


# myHash.insert(43, 'Training Day')
# myHash.insert(23, 'Out of time')
# myHash.insert(13, 'Remember the titans')
#
# print(myHash.table)
#
# print(myHash.search(13))
#
# myHash.delete(23)
#
# print(myHash.search(23))

