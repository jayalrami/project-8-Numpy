import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None

    # ---------- ARRAY CREATION ----------
    def create_array(self):
        print("\nSelect Array Type:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            data = list(map(int, input("Enter elements: ").split()))
            self.array = np.array(data)

        elif choice == 2:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            data = list(map(int, input(f"Enter {r*c} elements: ").split()))
            self.array = np.array(data).reshape(r, c)

        elif choice == 3:
            d = int(input("Enter depth: "))
            r = int(input("Enter rows: "))
            c = int(input("Enter columns: "))
            data = list(map(int, input(f"Enter {d*r*c} elements: ").split()))
            self.array = np.array(data).reshape(d, r, c)

        print("\nArray Created Successfully:")
        print(self.array)

    # ---------- INDEXING & SLICING ----------
    def indexing_slicing(self):
        print("\n1. Indexing")
        print("2. Slicing")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            idx = tuple(map(int, input("Enter index values: ").split()))
            print("Indexed Value:", self.array[idx])

        elif ch == 2:
            r1, r2 = map(int, input("Enter row range (start end): ").split())
            c1, c2 = map(int, input("Enter column range (start end): ").split())
            print("Sliced Array:")
            print(self.array[r1:r2, c1:c2])

    # ---------- MATHEMATICAL OPERATIONS ----------
    def math_operations(self):
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        ch = int(input("Enter your choice: "))

        data = list(map(int, input("Enter same size array elements: ").split()))
        arr2 = np.array(data).reshape(self.array.shape)

        if ch == 1:
            print("Result:\n", self.array + arr2)
        elif ch == 2:
            print("Result:\n", self.array - arr2)
        elif ch == 3:
            print("Result:\n", self.array * arr2)
        elif ch == 4:
            print("Result:\n", self.array / arr2)
        elif ch == 5:
            print("Dot Product:\n", np.dot(self.array, arr2))

    # ---------- COMBINE & SPLIT ----------
    def combine_split(self):
        print("\n1. Combine Arrays")
        print("2. Split Array")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            data = list(map(int, input("Enter second array elements: ").split()))
            arr2 = np.array(data).reshape(self.array.shape)
            print("Combined Array (Vertical Stack):")
            print(np.vstack((self.array, arr2)))

        elif ch == 2:
            parts = int(input("Enter number of splits: "))
            print("Split Arrays:")
            print(np.array_split(self.array, parts))

    # ---------- SEARCH, SORT, FILTER ----------
    def search_sort_filter(self):
        print("\n1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            val = int(input("Enter value to search: "))
            print("Found:", val in self.array)

        elif ch == 2:
            print("Sorted Array:")
            print(np.sort(self.array, axis=None))

        elif ch == 3:
            val = int(input("Show values greater than: "))
            print(self.array[self.array > val])

    # ---------- AGGREGATES, STATISTICS & CORRELATION ----------
    def statistics(self):
        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation Coefficient")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Sum:", np.sum(self.array))

        elif ch == 2:
            print("Mean:", np.mean(self.array))

        elif ch == 3:
            print("Median:", np.median(self.array))

        elif ch == 4:
            print("Standard Deviation:", np.std(self.array))

        elif ch == 5:
            print("Variance:", np.var(self.array))

        elif ch == 6:
            print("Minimum:", np.min(self.array))

        elif ch == 7:
            print("Maximum:", np.max(self.array))

        elif ch == 8:
            p = int(input("Enter percentile: "))
            print(f"{p}th Percentile:", np.percentile(self.array, p))

        elif ch == 9:
            data = list(map(int, input("Enter second array elements: ").split()))
            arr2 = np.array(data)

            a1 = self.array.flatten()
            a2 = arr2.flatten()

            print("Correlation Coefficient Matrix:")
            print(np.corrcoef(a1, a2))


# ---------- MAIN PROGRAM ----------
obj = DataAnalytics()

print("Welcome to the NumPy Analyzer!")

while True:
    print("\n===== MAIN MENU =====")
    print("1. Create a NumPy Array")
    print("2. Indexing & Slicing")
    print("3. Perform Mathematical Operations")
    print("4. Combine or Split Arrays")
    print("5. Search, Sort, or Filter Arrays")
    print("6. Compute Aggregates and Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.create_array()
    elif choice == 2:
        obj.indexing_slicing()
    elif choice == 3:
        obj.math_operations()
    elif choice == 4:
        obj.combine_split()
    elif choice == 5:
        obj.search_sort_filter()
    elif choice == 6:
        obj.statistics()
    elif choice == 7:
        print("Thank you for using the NumPy Analyzer! Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
