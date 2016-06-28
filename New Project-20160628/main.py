array = []
array2 = []
new_id = ''
new_tax = ''
new_addr = []
id_to_new = []
a = 0
n = 0 
temp = 0
with open("text.txt", "r") as f:
  for line in f:
    array.append(line.splitlines())
# print array

for i in array :
    if (i == ['']):
        a = a+1
        if (a == 1):
            new_id = array[n-1][0]
        if (a == 2):
            new_tax = array[n-1][0]
            temp = n+1
        if (a == 3):
            for x in range(temp,n):
                new_addr.append(array[x][0])
            temp = n+1  
        if (a == 4):
            for x in range(temp,n):
                id_to_new.append(array[x][0])
    n = n+1
    
# print "is a new_id : " +new_id
# print "is a new_tax : " +new_tax
# print  new_addr
# print id_to_new

for i in id_to_new : 
    print "UPDATE request SET REQSTR_ID = '"+new_id+"' WHERE REQ_ID ='"+i+"';"