#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 32
y = 6
print(x==y)


# In[2]:


#
x = 98
y = 54
if x > y:
    print(x)
    


# In[3]:


'''
if<expr>/bool:
    <statement>
<statement>
'''

x = 20
y = 5
if x < y:
    print("jangan pergi")
    print(y)
    
print("yuhuiiii")


# In[4]:


Q = "Cofd"
r = 2

if Q in "Coffe is a good":
    print("Masuk rumah")
    
    if r < 4:
        print("Jalan sakura")
        print("nilai r lebih kecil dari empat")
    print("kembali masuk rumah")
    
    if r >10:
        print("Jalan mentari")
        print("nilai r lebih besar dari sepuluh")
    print("Jangan masuk rumah")
    
print("pergi ke jalan anggrek")


# In[5]:


x = 20
b = 5
if x>b:
    print("x lebih besar dari b")
    print (x)
else:
    print("x lebih kecil dari b")
    print(b)


# In[6]:


Q = "Cof"
r = 2

if Q in "Coffe is a good":
    print("Masuk rumah")
    
    if r < 4:
        print("Jalan sakura")
        print("nilai r lebih kecil dari empat")
    else:
        print("else Jalan sakura")
        print("nilai r lebih kecil dari empat")
    print("kembali ke jalan sakura")
    
    if r >10:
        print("Jalan mentari")
        print("nilai r lebih besar dari sepuluh")
    else:
        print("else Jalan mentari")
        print("nilai r lebih besar dari sepuluh")
    print("kembali lagi ke jalan sakura")
    
print("pergi ke jalan anggrek")


# In[7]:


HargaTempe = 5000
HargaAyam = 25000
Uang = 15000

if Uang > HargaTempe:
    print("beli tempe")
elif Uang > HargaAyam:
    print("beli ayam")
else:
    print("uang kurang")


# In[8]:


x = 100
b = 600
maximum = x if x > b else b
print(maximum)


# In[9]:


raining = False
print(" Ke pasar" if not raining else "masak yang ada")


# In[10]:


raining = True
print(" Ke pasar" if not raining else "masak yang ada")


# In[ ]:





# In[11]:


a = 100
b = 10
if a > b:
    pass
print(a)


# In[ ]:





# In[ ]:





# In[12]:


'''
while <expr>/bool:
   <statement>
   <statement>
   <statement>
   <statement>
<statement>

'''


# In[13]:


# 1 + 2 + 3 + ... + 100

n = 1
un = 10
s =0

while n <= un:
    print(n)
    s += n # s = s+n
    n += 1
    
#print(s)


# In[14]:


print(n)


# In[15]:


i = 0
while i < 10:
        print(i)
        if i == 5:
            break
        print("di bawah break")
        i += 1
        
print("di luar looping")


# In[16]:


i = 0
while i < 10:
        i += 1
        if i == 5:
            continue
        print(i)
        print("di bawah continue")
        
print("di luar looping")


# In[17]:


i = 0
while i < 10:
    i += 1
    print(i)
else:
    print("loop selese")
print("di luar loop")


# In[18]:


i = 0
while i < 10:
        print(i)
        if i == 5:
            break
        print("di bawah break")
        i += 1
else:
     print("loop selese")
        
print("di luar looping")


# In[19]:


a = ['p','q','r','s']
n = len(a)

i=0

while i<10:
    print(i)
    j = 0
    while j < n:
        print(a[j], end=" ")
        j += 1
    i+=1
    print()
    


# In[21]:


n = 4
while n > 0: n-=1; print(n)


# In[ ]:





# In[25]:


Q = ['ba','bi','bu']
i = 0

for s in Q:
    print('i' in s)


# In[33]:


d = {'ba' : 1, 'bi' :2, 'bu':3}

for h in d:
    print(h)


# In[34]:


d.items()


# In[35]:


for h, v in d.items():
    print(h, "-",v)


# In[36]:


coor = [(1,1,1),(2,3,5),(4,5,6)]
for x,y,z in coor:
    print(x,y,z)


# In[37]:


for i in range(9,3,-1):
    print(i)


# In[41]:


# i=0
#while i<10:
#  i+=1
#  if i==6
#    Continue
#  print(i)
#  print("di bawah continue")

for i in range (0,11):
    if i == 6:
        continue
    print(i)
    print("di bawah break")


# In[42]:


for i in range (0,11):
    if i == 6:
        break
    print(i)
    print("di bawah break")
else:
    print("done")


# In[ ]:




