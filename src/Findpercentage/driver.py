from util import calculate_avg
 
n=int(input())
stud={}
for i in range(n):
    data=input().split()
    name=data[0]
    mark=list(map(int,data[1:]))
 
    stud[name]=mark
 
 
query_name=input()
marks_of_stud=stud[query_name]
 
avg=calculate_avg(marks_of_stud)
 
print(f"{avg:.2f}")
