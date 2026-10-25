class Bucket:
    def __init__(self, depth, size):
        self.depth = depth
        self.size = size
        self.items = {}

    def is_full(self):
        return len(self.items) >= self.size


class ExtendibleHashTable:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [Bucket(self.global_depth, bucket_size) for _ in range(2)]

    def hash(self, key):
        return hash(key) & ((1 << self.global_depth) - 1)

    def double_directory(self):
        self.global_depth += 1
        self.directory += self.directory  # duplicate references

    def split_bucket(self, index):
        old_bucket = self.directory[index]
        local_depth = old_bucket.depth
        old_bucket.depth += 1

        # create a new bucket
        new_bucket = Bucket(old_bucket.depth, self.bucket_size)

        # redistribute items
        items = list(old_bucket.items.items())
        old_bucket.items.clear()

        # update directory pointers
        for i in range(len(self.directory)):
            if self.directory[i] is old_bucket and (i >> local_depth) & 1:
                self.directory[i] = new_bucket

        for k, v in items:
            self.insert(k, v)

    def insert(self, key, value):
        index = self.hash(key)
        bucket = self.directory[index]

        if key in bucket.items:  # update existing
            bucket.items[key] = value
            return

        if not bucket.is_full():
            bucket.items[key] = value
        else:
            if bucket.depth == self.global_depth:
                self.double_directory()
                index = self.hash(key)  # recompute index
            self.split_bucket(index)
            self.insert(key, value)  # retry insert

    def search(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        return bucket.items.get(key, None)

    def delete(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        if key in bucket.items:
            del bucket.items[key]
            print(f"Key {key} deleted")
        else:
            print("Key not found")

    def display(self):
        print(f"\nGlobal Depth: {self.global_depth}")
        seen = set()
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                seen.add(id(bucket))
                print(f"Bucket {i}: depth={bucket.depth}, items={bucket.items}")


# ---------------- Main Program ----------------
if __name__ == "__main__":
    ht = ExtendibleHashTable(bucket_size=2)

    while True:
        print("\n--- Extendible Hash Table ---")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.insert(key, value)

        elif choice == 2:
            key = input("Enter key to search: ")
            result = ht.search(key)
            if result is not None:
                print(f"Value found: {result}")
            else:
                print("Key not found")

        elif choice == 3:
            key = input("Enter key to delete: ")
            ht.delete(key)

        elif choice == 4:
            ht.display()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
