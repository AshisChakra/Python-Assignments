OUTPUT_FILE = 'output.txt'

def read_write_operation():
    input1 = input("Enter text to write to the file: ")
    try:
        write_file = open(OUTPUT_FILE, 'w')
        write_file.write(input1 + "\n")
        print("data successfully written to the file")
        write_file.close()
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    input2 = input("\nEnter text to append to the file: ")
    try:
        append_file = open(OUTPUT_FILE, 'a')
        append_file.write(input2 + "\n")
        print("data successfully appended to the file")
        append_file.close()
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")


read_write_operation()
print("\nFinal contents of the file:")
outputFile = open(OUTPUT_FILE, 'r')
print(outputFile.read())