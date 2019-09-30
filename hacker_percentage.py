/*
You have a record of  students. Each record contains the student's name, 
and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer  followed by the names and marks for  students. 
You are required to save the record in a dictionary data type. The user then enters a student's name. 
Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer , the number of students. 
The next  lines contains the name and marks obtained by that student separated by a space. 
The final line contains the name of a particular student previously listed.

Constraints

*2>=n<=10
*0<=marks<=100

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00

*/

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        record = input().split()
        name,marks = record[0], record[1:]
        marks = list(map(float, marks))
        student_marks[name] = marks
    query = input()
    print("{0:.2f}".format(*[(sum(scores)/len(scores)) for name, scores in student_marks.items() if name == query]))