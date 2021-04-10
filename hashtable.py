
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

