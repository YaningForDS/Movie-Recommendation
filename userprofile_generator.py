print('')
print('')
print('############################################')
print('#   Randomly Generate User Profile         #')
print('############################################')
print('')
print('')

import numpy as np 
import scipy
import csv

f = open('/Users/Yaning/Desktop/CloudComputing/Movie_project/data/overview_theme.csv','rb')
reader = csv.DictReader(f)
A = set()
for row in reader:
    tempt = row['movie theme'].replace("'",'').replace('[','').replace(']','').split(',')
    for item in tempt:
        item = item.strip()
        A.add(item)
res = list(A)[1:]
print len(res)
dictionary = {}
i = 1
for line in res:
    dictionary[i] = line
    i = i + 1
#print dictionary

'''
Generate character-theme matrix
each type of user possibly like 10 themes
Assume independence of user, hence the expectation = 400 = n*p => 0.025
It is a 40*405 sparse matrix, which means that there are 40 types of characters corresponding to 405 themes 
'''

mymat = np.random.binomial(n=1,p=0.025,size = 40).reshape(40,1)

'''
[[0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 ..., 
 [0 0 0 ..., 0 0 1]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]]
'''
# b = np.where(mymat!=0)
# print len(b[0]) the number of non-zeros elements
for i in range(404):
    tmp = np.random.binomial(n=1,p=0.012,size = 40).reshape(40,1)
    mymat = np.concatenate((tmp,mymat),axis = 1)


print('#############################################')
print('#   Randomly Generate User prefered themes  #')
print('#############################################')

'''
the user vector will be a 40*1 vector, which map to 40 different characters, 
1 entries mean that the user has this character, otherwises,0
'''

def theme_generator(mymat):
    prefer_list = []
    ## random generate user's type 
    user = np.random.binomial(n=1,p=0.05,size = 40)
    num_theme = len(np.where(user!=0)[0])
    for i in range(num_theme):
        tmp = mymat[np.where(user!=0)[0]][i]
        mytheme = np.where(tmp!=0)[0] ##return the index that is not zero
        theme_list = [theme for theme in mytheme]
        for item in theme_list:
            if item not in prefer_list:
                prefer_list.append(item)
    preferred_theme = set()
    #myprefer = theme_generator(mymat)
    for index in prefer_list:
        preferred_theme.add(dictionary[index])
    preferred_theme = list(preferred_theme) 
    return preferred_theme ## return a list of user's preferred theme


'''
Sample result of preferred themes

['baseball players', 'kidnapping', 'death of a friend', 'widows and widowers', 'rogue cops', 
'woman in jeopardy', 'immortality', 'marriages of convenience', 'authority figures k', 'rise and fall stories', 
'finding a way back home', 'college life', 'perfect crime', 'biotechnology anime']

'''
