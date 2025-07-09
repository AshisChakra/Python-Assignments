marksheet = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Diana": 88,
    "Akash": 95,
    "Ashis": 80,
    "Ravi": 70,
}

name = input("Enter the name of the student to get their score: ")
def get_score(name):
    if name in marksheet:
        print(f"{name} marks : {marksheet[name]}") 
    else:
        print("Student not found.") 
    
get_score(name)
