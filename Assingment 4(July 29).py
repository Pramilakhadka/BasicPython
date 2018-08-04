#Question no 1
dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}
dic4={**dic1, **dic2, **dic3}

print(dic4)


#Question no 2

my_dictionary = {

"a": 1,

"b": True,

"c": [1, 2, 3, 4],

"d": {"Hello": 5, "World": 5}

}
my_dictionary.update({"xyz":None})
print(my_dictionary)

if 'pqe' in my_dictionary:
    print("True")

else:
    print("False")

print(my_dictionary.values())
del my_dictionary["xyz"]
print(my_dictionary)


#Question no 3:

my_list = list(range(0, 10))
def func (my_list):
     return sum (my_list)
print(func(my_list))


#Question no 4:

another_list = [4, 5, 9, 1, 0, 2, 3]
print(max(another_list))
print(min(another_list))

#Question no 5:
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
