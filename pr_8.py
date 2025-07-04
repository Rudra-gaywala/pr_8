import numpy as np
import pandas as pd

class datanalytics :
    def __init__(self):
        self.array = None

    def creat_numpy_array(self):
        print("Select the types of array to creat\n")
        print("1. 1D array")
        print("2. 2D array")
        print("3. 3D array\n")
        c = int(input("Enter your choice :"))

        if c==1:
            size = int(input("enter the number of elements: "))
            input_elem = input(f"enter {size} elements for the array separated by space: ")
            elem = list(map(int , input_elem.split()))
            if len(elem) != size :
                print("Invalid no. of elements......... ")
                return
            self.array = np.array(elem)
            print("===================================================")
            print("Array created successfully: ")
            print(self.array)
            print("===================================================")

            while True:

                print("\nSelect an operation: \n")

                print("1. Indexing")
                print("2. Slicing")
                print("3. Go back\n")

                ch = int(input("Enter your choice : "))

                if ch == 1:
                    i = int(input("Enter index: "))
    
                    print("===================================================")
                    print("Element at index", i, "is:", self.array[i])
                    print("===================================================")

                

                elif ch == 2:

                    s = input("Enter slice (start:end): ")
                    parts = s.split(":")

                    start = int(parts[0]) 
                    end = int(parts[1])

                    sliced = self.array[start:end]

                    print("Sliced Array:", sliced)
                    

                    # rng = input("Enter slice (start:end or start:end:step): ")

                    # parts = list(map(lambda x: int(x) if x else None, rng.split(":")))

                    # sliced = self.array[slice(*parts)]

                    # print("===================================================")
                    # print("Sliced Array:", sliced)
                    # print("===================================================")

                elif ch == 3:
                    break
                    

                else :
                    print("Invalid choice.......... please try again.......... ")



        elif c==2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            size = rows * cols

            elements = input(f"Enter {size} for the array separeted by space :")
            elems = list(map(int, elements.split()))

            if len(elems) != size:
                print("Invalid no. of elements......... ")
                return
            
            self.array =  np.array(elems).reshape(rows,cols)
            print("===================================================")
            print("Array created successfully: ")
            print(self.array)
            print("===================================================") 

            while True:

                print("\nSelect an operation: \n")

                print("1. Indexing")
                print("2. Slicing")
                print("3. Go back\n")

                ch = int(input("Enter your choice : "))

                if ch == 1:
                    idx = int(input("Enter index: "))
                    if 0 <= idx < len(self.array):
                        print("===================================================")
                        print(f"Element at index {idx} is: {self.array[idx]}")
                        print("===================================================")


                    else:
                        print("Index out of range.")

                elif ch == 2:
                    row = input("Row range (start:end): ")
                    col = input("Col range (start:end): ")

                    r1, r2 = map(int, row.split(":"))
                    c1, c2 = map(int, col.split(":"))


                    print("===================================================")
                    print("\nSliced Array:")
                    print(self.array[r1:r2, c1:c2])
                    print("===================================================")

                elif ch == 3:
                    main()
                    break

                else :
                    print("Invalid choice.......... please try again.......... ")


        elif c==3:
            d1 = int(input("Enter size of first dimension: "))
            d2 = int(input("Enter size of second dimension: "))
            d3 = int(input("Enter size of third dimension: "))
            size = d1 * d2 * d3

            elements = input(f"Enter {size} for the array separeted by space :")
            elems = list(map(int, elements.split()))

            if len(elems) != size:
                print("Invalid no. of elements......... ")
                return
            
            self.array =  np.array(elems).reshape(d1,d2,d3)
            print("===================================================")
            print("Array created successfully: ")
            print(self.array)
            print("===================================================") 

        else :
            print("Invalid choice.......... please try again.......... ")

            while True:

                print("\nSelect an operation: \n")

                print("1. Indexing")
                print("2. Slicing")
                print("3. Go back\n")

                ch = int(input("Enter your choice : "))

                if ch == 1:
                    idx = int(input("Enter index: "))
                    if 0 <= idx < len(self.array):
                        print("===================================================")
                        print(f"Element at index {idx} is: {self.array[idx]}")
                        print("===================================================")


                    else:
                        print("Index out of range.")

                elif ch == 2:
                    row = input("Row range (start:end): ")
                    col = input("Col range (start:end): ")

                    r1, r2 = map(int, row.split(":"))
                    c1, c2 = map(int, col.split(":"))


                    print("===================================================")
                    print("\nSliced Array:")
                    print(self.array[r1:r2, c1:c2])
                    print("===================================================")


                elif ch == 3:
                    main()
                    break
                    

                else :
                    print("Invalid choice.......... please try again.......... ")
        

    def mathematical_operations(self):

        if self.array is None:
            print("No array available. Please create an array first.")
            return

        print("Choose a mathematical operations:\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int(input("Enter your choice : "))

        size = self.array.size
        shape = self.array.shape

        input_elem = input(f"Enter the same size array elements ({self.array.size} elements saperated by space): ")
        elem = list(map(int , input_elem.split()))
        second_array = np.array(elem).reshape(shape)

        if size != len(elem) :
            print("Invalid no. of elements......... ")
            return

        
        if ch==1:
           
            ans = self.array + second_array
            print("Original array: ")
            print(self.array)
            print("\n")

            print("Second array: ")
            print(second_array)
            print("\n")

            print("Result of addition: ")
            print(ans)
            print("\n")

        elif ch==2:
            ans = self.array - second_array
            print("Original array: ")
            print(self.array)
            print("\n")

            print("Second array: ")
            print(second_array)
            print("\n")

            print("Result of subtraction: ")
            print(ans)
            print("\n")

        elif ch==3:
            ans = self.array * second_array
            print("Original array: ")
            print(self.array)
            print("\n")

            print("Second array: ")
            print(second_array)
            print("\n")

            print("Result of multiplication: ")
            print(ans)
            print("\n")
        
        elif ch==4:
            ans = self.array / second_array
            print("Original array: ")
            print(self.array)
            print("\n")

            print("Second array: ")
            print(second_array)
            print("\n")

            print("Result of division: ")
            print(ans)
            print("\n")

        else :
            print("Invalid choice.......... please try again.......... ")


    def combine_split_array(self):

        if self.array is None:
            print("No array available. Please create an array first.")
            return

        print("Choose an operations:\n")
        print("1. Combine array")
        print("2. Split array")

        ch = int(input("Enter your choice : "))

        size = self.array.size
        shape = self.array.shape
        

        if ch == 1:

            input_elem = input(f"Enter the elements of another array to combine ({self.array.size} elements saperated by space): ")
            elem = list(map(int , input_elem.split()))
            second_array = np.array(elem).reshape(shape)

            if size != len(elem) :
                print("Invalid no. of elements......... ")
                return

            vstacked = np.vstack((self.array , second_array))
            hstacked = np.hstack((self.array , second_array))

            print("Original array: ")
            print(self.array)
            print("\n")

            print("Second array: ")
            print(second_array)
            print("\n")

            print("Result of combine (vertical stacked): ")
            print(vstacked)
            print("\n")

            print("Result of combine (horisontally stacked): ")
            print(hstacked)
            print("\n")

        elif ch == 2:
            print("Your current array:")
            print(self.array)

            num = int(input("Enter number of splits: "))
            try :
                if self.array.ndim==1:
                    ans = np.array_split(self.array , num)
                    print("Splitted array: ")
                    print(ans)

                elif self.array.ndim==2:
                    v = np.vsplit(self.array , num)
                    h = np.hsplit(self.array , num)

                    print("Result of split (vertical split): ")
                    print(v)
                    print("\n")

                    print("Result of split (horisontally split): ")
                    print(h)
                    print("\n") 

                else:
                    print("Split not supported for arrays more than 2D.")
                    return

            except Exception as e:
                print("Error..........:", e)


        else :
            print("Invalid choice.......... please try again.......... ")



    def search_sort_filter(self):
        if self.array is None:
            print("No array available. Please create an array first.")
            return

        print("Choose an operations:\n")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        ch = int(input("Enter your choice : "))

        if ch==1:
            val = int(input("Enter the element to search: "))
            result = np.where(self.array == val)

            if result[0].size == 0:
                print(f"Element {val} not found in the array.")
            else:
                print(f"Element {val} found at index : {result}")

        elif ch==2:
            if self.array.ndim == 1:
                s_array = np.sort(self.array)
                print("Sorted array:")
                print(s_array)

            elif self.array.ndim == 2:
                axis = int(input("Sort by:\n - columns\n - rows\nEnter your choice: "))
                sorted_array = np.sort(self.array, axis=axis)
                print("Sorted array:")
                print(sorted_array)

            else :
                print("sorting of 3D array is not supporting ...........")

        elif ch==3:
            print("\nSelect an operations: \n")
            print("1. print even numbers")
            print("2. print odd numbers")
            print("3. print greater than 50 ")
            print("4. print less than 50 \n")

            c = int(input("Enter your choice: "))

            if c ==1 :
                print(self.array[self.array %2==0])

            elif c == 2:
                print(self.array[self.array %2!=0])

            elif c == 3:
                print(self.array[self.array > 50])

            elif c == 4: 
                print(self.array[self.array < 50])

            else :
                print("Invalid choice.......... please try again.......... ")
            
        else :
            print("Invalid choice.......... please try again.......... ")



    def aggrigates_statics(self):
        print("\nChoose an aggrigates/staticstical operations: \n")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance\n")

        c = int(input("Enter your choice : "))

        if c == 1:
            print(self.array)
            print("\n")
            print(f"Sum of array: {self.array.sum()}")

        elif c == 2:
            print(self.array)
            print("\n")
            print(f"Mean of array: {self.array.mean()}")

        elif c == 3:
            median = np.median(self.array)
            print(self.array)
            print("\n")
            print(f"Median of array: {median}")

        elif c == 4 :
            srd = np.std(self.array)
            print(self.array)
            print("\n")
            print(f"standard deviation of array: {srd}")

        elif c == 5:
            var = np.var(self.array)
            print(self.array)
            print("\n")
            print(f"Variation of array: {var}")

        else :
            print("Invalid choice.......... please try again.......... ")

class main:
    print("Welcome To The Numpy Analyzer !!!")
    print("===================================================")
    da = datanalytics()

    while True:
        print("\nchoose an option\n")
        print("1. Creat a numpy array")
        print("2. Perform mathematical operations")
        print("3. Combine or split arrays")
        print("4. Search , sort or filter arrays")
        print("5. Compute aggregates and statistics")
        print("6. Exit\n")

        choice = int(input("Enter your choice :"))

        match choice:
            case 1:
                da.creat_numpy_array()
            case 2:
                da.mathematical_operations()
            case 3:
                da.combine_split_array()
            case 4:
                da.search_sort_filter()
            case 5:
                da.aggrigates_statics()
            case 6:
                print("Thank you for using Numpy Analizer ! Goodbye !")
                break
            case _:
                print("Invalid choice.......... please try again.......... ")