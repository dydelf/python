from collections import OrderedDict

favourite_languages = {
    'jen': 'python',
    'arthur': 'C++',
    'sylvia': 'java',
    'jesus': 'pascal',
}
friends = ['jesus']
print("jesus's favourite language is: " +
     favourite_languages['jesus'].title())

print(favourite_languages['jesus'])

person_1 = {
    'name': 'maciek',
    'surname': 'gajewski',
    'age': '26',
    'gender': 'male'
}

#printing the dictionary
for name, language in favourite_languages.items():
    print(name.title() +
    "'s favourite language is " +
    language.title())

#printing special message to keys included in a previous list
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        print("hello " + name)

#printing message for someone not in a dictionary
if 'someone' not in favourite_languages.keys():
    print("hey someone, print your work!")

#printing values in languages but only one time,
# set function omits doubles
print("the following languages were mentioned: ")
for language in set(favourite_languages.values()):
    print(language.title())
