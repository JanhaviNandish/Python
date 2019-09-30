#haker rank nested list
/*
Given the names and grades for each student in a Physics class of n students,
 store them in a nested list and print the name(s) of any student(s)
 having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new 
line.

Input Format

The first line contains an integer, n , the number of students. 
The  2n subsequent lines describe each student over 2  lines;
 the first line contains a student's name, 
and the second line contains their grade.

Constraints

*2<=n<=5
*There will always be one or more students having the second lowest grade

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; 
if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry

Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
 so we order their names alphabetically and print each name on a new line.

*/
n=int(input())
l=[]
j=0
while j<n:
    name=input()
    physis=float(input())
    l.append([name,physis])
    j+=1
x=[]
for i in l:
    x.append(i[1])
x.sort()
sbig=0
k=0
while k<len(x):
    if x[k]!=x[k+1]:
        sig=x[k+1]
        break
    k+=1
x=[]
for i in l:
    if i[1]==sbig:
        x.append(i[0])
x.sort()
for i in x:
    print(i)