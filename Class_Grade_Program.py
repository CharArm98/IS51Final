


""" Structured English 
start
create a list to store 24 numbers (float)
capture users input 24 times for their grades
each time we capture the user's input, we append the number to the list 
sort the list ascending, then splice the item starting at index 1
displaying the number of grades, the average, and the percentage of grades above the average
output a messsage to the user

"""

""" Pseudocode
Number of grades: 24
Average grade: 83.25
Percentage of grade: 83.25
Average: 54.17 percent 

Enter one of five grades: 84
Enter one of five grades: 96
Enter one of five grades: 88
Enter one of five grades: 77
Enter one of five grades: 90
Average grade : 91.33

"""

def main():
    ## Display final grades
    Finaldict = createDictFromFile("Final.txt")
    displayInfoAboutFinalGrades(finalDict)

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()


for i in range( len(grades)):
        grades [i] = int(grades [i])
average = sum (grades) / len (grades)
num = 0 # number of grades above average
for grade in grades:
    if grade > average:
         num +=1
print("Number of grades:", len (grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%" .format(100 * num / len(grades)))
