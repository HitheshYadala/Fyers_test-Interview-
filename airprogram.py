csv_file=open('airlines.csv')
l=[]
lst=[]
st={}
i=0
l1=[]
d=dict()
for row in csv_file:
    ap_names=(row.split(',')[0])
    lst=l.append(ap_names)
##print(l)
del l[0]
st=set(l)
print('UNIQUE AIRPORT CODES: \n',st,'\n\n')
for i in st:
    counter=(i+':'+str(l.count(i)))
    l1.append(counter)

    
################################################################
##print(str(l1))
##d={}.fromkeys(l1,0)
##print(d)                      Ignore this portion of code
##for data in st:
##    if d in data:
##        d[data]+=1
##
##print(d)
######################################################################


d=dict()
for i in st:
    d[i]=l.count(i)

print('AIRPORT COUNT: \n',d,'\n\n')
#print(max(d))

max_value=max(d.values())
max_keys=[k for k, v in d.items() if v==max_value]
print('MAX COUNT OF AIR PORT: ',max_keys,max_value)

min_value=min(d.values())
min_keys=[k for k, v in d.items() if v==min_value]
print('MIN COUNT OF AIR PORT: ',min_keys,min_value)
   



