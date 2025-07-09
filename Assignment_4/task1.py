
def file_read_operation():
    try:
        file = open('sample.txt', 'r')  
        print("Reading the file contents:")
        print("Line1: ", file.readline().strip()) 
        print("Line2: ", file.readline())
        file.close()
    except FileNotFoundError:
        print("The file 'sample.txt' was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

file_read_operation()
    