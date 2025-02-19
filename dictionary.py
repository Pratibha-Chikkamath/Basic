dic={}
print(type(dic))

dic['name']="pratibha"
dic['age']=24
dic['email']="prathibhachikkamath@gmail.com"
dic['number']=9900887766
print(dic)

dic['name']="anjali"
print(dic)

for i in dic:
    print(i)

for i in dic:
    print(dic[i])

for i in dic:
    print(i,dic[i])