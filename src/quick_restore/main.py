# encoding: utf-8
"""
@author: zxcvb6958
@date: 2019/10/17
@last modified: 2019/10/17
"""

import pickle
import torch


a_dict = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
a_list = [a_dict, a_dict, 0]
a_tensor = torch.Tensor([1, 2, 3])


# save
f1 = open('dict.pkl', 'wb'); f2 = open('list.pkl', 'wb'); f3 = open('tensor.pkl', 'wb')
f1.write(pickle.dumps(a_dict)); f2.write(pickle.dumps(a_list)); f3.write(pickle.dumps(a_tensor))
f1.close(); f2.close(); f3.close()

# read
f1 = open('dict.pkl', 'rb')
my_dict = pickle.loads(f1.read())
print(my_dict)

f2 = open('list.pkl', 'rb')
my_list = pickle.loads(f2.read())
print(my_list)

f3 = open('tensor.pkl', 'rb')
my_tensor = pickle.loads(f3.read())
print(my_tensor)

f1.close(); f2.close(); f3.close()
