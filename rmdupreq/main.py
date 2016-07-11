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
print array

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
            temp = n+2
        if (a == 4):
            for x in range(temp,len(array)):
                id_to_new.append(array[x][0])
    n = n+1

print "is a new_id : " +new_id
# print "is a new_tax : " +new_tax
# print  new_addr
# print id_to_new
file = open("newfile.txt", "w")
# file.write("hello world in the new file\n")
# file.write("and another line")
# file.close()

print "UPDATE requester SET TAX_ID = '"+new_tax+"' WHERE REQSTR_ID = '"+new_id+"'; "
file.write("UPDATE requester SET TAX_ID = '"+new_tax+"' WHERE REQSTR_ID = '"+new_id+"'; \n")

for i in id_to_new :
    print "UPDATE request SET REQSTR_ID = '"+new_id+"' WHERE REQSTR_ID ='"+i+"';"
    file.write("UPDATE request SET REQSTR_ID = '"+new_id+"' WHERE REQSTR_ID ='"+i+"';\n")
    print "UPDATE factory SET OWNER_ID = '"+new_id+"' WHERE OWNER_ID ='"+i+"';"
    file.write("UPDATE factory SET OWNER_ID = '"+new_id+"' WHERE OWNER_ID ='"+i+"';\n")

for i in new_addr :
    print "UPDATE permit SET REQSTR_ID = '"+new_id+"', REQSTR_ADD = '"+i+"', TAX_ID = '"+new_tax+"' WHERE REQSTR_ID ='"+i+"';"
    file.write("UPDATE permit SET REQSTR_ID = '"+new_id+"', REQSTR_ADD = '"+i+"', TAX_ID = '"+new_tax+"' WHERE REQSTR_ID ='"+i+"';\n")
    print "UPDATE requester SET REQ_ADDR = CONCAT(REQ_ADDR, ',', '"+i+"' )  WHERE REQSTR_ID = '"+new_id+"'; "
    file.write("UPDATE requester SET REQ_ADDR = CONCAT(REQ_ADDR, ',', '"+i+"' )  WHERE REQSTR_ID = '"+new_id+"'; \n")

    print "UPDATE requester_addr SET REQSTR_ID = "+new_id+"  WHERE REQSTR_ADD = '"+i+"'; "
    file.write("UPDATE requester_addr SET REQSTR_ID = "+new_id+"  WHERE REQSTR_ADD = '"+i+"';  \n")

l3 = [x for x in id_to_new if x not in new_addr]
# print l3
for i in l3 :
    print "UPDATE permit SET REQSTR_ID = '"+new_id+"', REQSTR_ADD = '"+new_addr[0]+"', TAX_ID = '"+new_tax+"' WHERE REQSTR_ID ='"+i+"';"
    file.write("UPDATE permit SET REQSTR_ID = '"+new_id+"', REQSTR_ADD = '"+new_addr[0]+"', TAX_ID = '"+new_tax+"' WHERE REQSTR_ID ='"+i+"';\n")
l4 = [x for x in id_to_new if x not in new_id]
for i in l4 :
    print "DELETE FROM requester WHERE REQSTR_ID ='"+i+"';"
    file.write("DELETE FROM requester WHERE REQSTR_ID ='"+i+"';\n")
file.close()
