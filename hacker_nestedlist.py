/*
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n . The second line contains an array a[]
   of n integers each separated by a space.
/*
marks=[]
scores=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    marks+=[[name,score]]
    scores+=[score]
b=sorted(list(set(scores)))[1] 
for a,c in sorted(marks):
    if c==b:
        print(a)