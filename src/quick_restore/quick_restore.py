import pickle


a_dict = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
a_list = [a_dict, a_dict, 0]


# # save
# f1 = open('dict.txt', 'w'); f2 = open('list.txt', 'w')
# f1.write(str(the_dict)); f2.write(str(the_list))
# f1.close(); f2.close()
#
# # read
# f = open('dict.txt', 'r')
# the_dict = eval(f.read())
# f.close()
# print(the_dict)
#
# f = open('list.txt', 'r')
# the_list = eval(f.read())
# f.close()
# print(the_list)


# save
f1 = open('dict.pkl', 'wb'); f2 = open('list.pkl', 'wb')
f1.write(pickle.dumps(a_dict)); f2.write(pickle.dumps(a_list))
f1.close(); f2.close()

# read
f1 = open('dict.pkl', 'rb')
my_dict = pickle.loads(f1.read())
print(my_dict)

f2 = open('list.pkl', 'rb')
my_list = pickle.loads(f2.read())
print(my_list)

f1.close(); f2.close()
