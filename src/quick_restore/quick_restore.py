# save
the_dict = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
the_list = [the_dict, the_dict, 0]
f1 = open('dict.txt', 'w'); f2 = open('list.txt', 'w')
f1.write(str(the_dict)); f2.write(str(the_list))
f1.close(); f2.close()

# read
f = open('dict.txt', 'r')
the_dict = eval(f.read())
f.close()
print(the_dict)

f = open('list.txt', 'r')
the_list = eval(f.read())
f.close()
print(the_list)
