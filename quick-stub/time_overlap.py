lists = [[1,10],[8,10],[2,15]]
lists = [[1,10]]

compare_list = lists[-1]
b= set(range(compare_list[0], compare_list[1]+1))
# print(b)
for i in range(0,len(lists)-1):
    a= set(range(lists[i][0], lists[i][1]+1))
    # print(a)
    b = b-a
    
# print (b)
try:
    b = [min(b),max(b)]
except:
    b =[]
print (b)
