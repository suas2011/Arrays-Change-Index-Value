#Arrays1..10

import array
floatarray=array.array('f',[2.3,4.4,56.2,5.5])#storing floats
for i in floatarray:
 print(round(i,1))


intarray=array.array('i',[2,3,4,5,25,53,75])#storing integers
print('_________')

a=int(input('enter index value: '))
b=int(input('enter new data value: '))
intarray.insert(a,b)
print(intarray)
for i in intarray:
 print(i)

#storing Unicodes
unicodearr = array.array('u',[u'\u0050',u'\u0059',u'\u0054',u'\u0048',u'\u004F',u'\u004E'])
uca = unicodearr.tounicode()
print(uca)


