import requests,json
fin=0
x=requests.get('http://saral.navgurukul.org/api/courses')
y=x.json()
s=json.dumps(y,indent=4)
with open('courses.json','w') as file:
    file.write(s)
files=open('courses.json','r')
aaa = json.load(files)
id = []
counter = 1
for i in aaa["availableCourses"]:
    print(counter, i["name"], i["id"])
    id.append(i["id"])
    counter = counter + 1
user = int(input('Please enter the program no. : '))
bitsr = id[user - 1]
desk=requests.get('http://saral.navgurukul.org/api/courses/'+bitsr+'/exercises')
yep=desk.json()
site=json.dumps(yep,indent=4)
with open('s.json','w') as file:
    file.write(site)
now=open('s.json')
check=1
dino=json.load(now)
for i in dino['data']:
    print(check,i['name'])
    if i['childExercises']!=[]:
        c=1
        for k in i['childExercises']:
            print('   ',c,k['name'])
            c=c+1
    check+=1
ask=int(input('Give the topic no.:- '))
check=1
for i in dino['data']:
    if check==ask:
        if i['childExercises']==[]:
            see=i['slug']
        else:
            ask=int(input('Give the subtopic no.- '))
            check=1
            for k in i['childExercises']:
                if check==ask:
                    see=k['slug']
                check+=1
    check+=1
with open('child_data.json','w') as yout:
    desk=requests.get('http://saral.navgurukul.org/api/courses/'+bitsr+'/exercise'+'/getBySlug?slug='+see)
    yep=desk.json()
    site=json.dumps(yep,indent=4)
    yout.write(site)
best=open('child_data.json')
beta=json.load(best)
print(beta['content'])