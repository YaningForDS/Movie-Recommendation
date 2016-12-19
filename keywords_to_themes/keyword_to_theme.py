import json
from watson_developer_cloud import NaturalLanguageClassifierV1
from credential import *
from collections import defaultdict
import os
import random

current_file_path = __file__
upper_dir = os.path.dirname(os.getcwd())

data_dir = os.path.join(upper_dir, 'data')
filename = os.path.join(data_dir, 'Allmovie_Title_theme.csv')
 
natural_language_classifier = NaturalLanguageClassifierV1(
  username = username,
  password = password)
classifier_id = "ff1c2bx159-nlc-340"


def predict(keyword):
	classes = natural_language_classifier.classify(classifier_id, keyword)
	return classes

def load_data():
    """
    This method reads the dataset, and returns a list of rows.
    Each row is a list containing the values in each column.
    """
    import csv
    
    with open(filename, 'rb') as f:
        f.seek(0)
        reader = csv.reader(f)
        return [l for l in reader]

def get_movie(themes):
	data = load_data()
	ThemeCollect = dict()
	ThemeTitle = defaultdict(list)
	for row in data:
	    for i in xrange(1,7):
	        if row[i] == "":
	            break
	        ThemeCollect[row[i].strip()] = ThemeCollect.get(row[i].strip(), 0) + 1
	        ThemeTitle[row[i].strip()].append(row[0])
	
	list_1 = ThemeTitle[themes[1]]
	list_2 = ThemeTitle[themes[1]]
	list_3 = ThemeTitle[themes[1]]

	threeIntersect = set(list_1).intersection(list_2).intersection(list_3)

	# recommend 5 movie if intersection > 5
	if len(threeIntersect) > 5: return random.sample(threeIntersect, 5)

	# recommend from first selected theme if intersection = 0
	elif len(threeIntersect) == 0: return random.sample(set(list_1), 3)

	return recommended

	#remove empty list
	if '""' in ThemeCollect:
	    del ThemeCollect['""']
	if '""' in ThemeTitle:
	    del ThemeTitle['""']	    
	#remove themes with only one or two movie
	for key, value in ThemeCollect.items():
	    if value < 3:
	        del Th


##--- From Keyword to theme ---###
result = predict('["storm","sink","ship"]')
theme_class =  result['classes']

recommendTheme =[]

print('')
print('')
print('#############################################')
print('#   The top 3 themes you might be interested #')
print('#############################################')
for i in xrange(3):

	print "Theme" +  str(i+1) + ':'
	print theme_class[i]['class_name']
	recommendTheme.append(theme_class[i]['class_name'])



print('')
print('')
print('############################################')
print('#   The top 5 movies you may like          #')
print('############################################')
##--- From Theme to movie ---##
recommendMovie = get_movie(recommendTheme)
for item in recommendMovie:
	print item


