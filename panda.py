import pandas as po
courses={
    'trainer':['sai','nani','ram','venkat'],
    'course':['python','django','api','mysql'],
    'fee':[2000,2500,1000,500]
}
data=po.DataFrame(courses)#
print(data)#
values=['zero','first','second','third']
data=po.DataFrame(courses,index=values)#
print(data)#
data=po.DataFrame(data,columns=['course','trainer','fee'])#
print(data)#
data=data.set_value('third','fee',4000)#
print(data)#
import numpy as np
data['area']=np.NAN#
print(data)#
areas=['hyd','bang','pune','che']
data['area']=areas#
print(data)#
data=data.drop('fee',axis=1)#
print(data)#
import pandas as po

df1=po.DataFrame(
    {"A":['ao','a1','a2','a3'],
     "B":['b0','b1','b2','b3'],
     "C":['c0','c1','c2','c3'],
     "D":['d0','d1','d2','d3']
     },
    index=[0,1,2,3]
)
df2=po.DataFrame(
    {'A':['a4','a5','a6','a7'],
     'B':['b4','b5','b6','b7'],
     'C':['c4','c5','c6','c7'],
     'D':['d4','d5','d6','d7']
     },
    index=[4,5,6,7]
)
print(df1)
print(df2)
frames=[df1,df2]
data=po.concat(frames)
print(data)

