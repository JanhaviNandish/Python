/*
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n . The second line contains an array a[]
   of n integers each separated by a space.

contraints
* 2<=n<=10
*-100<=a[i]<=100

output

print the runner up score

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5

/*
n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))

