"""
Instructions
You are going to write a program that calculates the highest score from a List of scores.
e.g.student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
    The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output
The highest score in the class is: 91
"""

student_scores = input("Enter the list of score seperated by space : ").split()

for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

largest = 0

for i in student_scores:
    if i > largest:
        largest = i
print("The highest score in the class is: ",largest)
