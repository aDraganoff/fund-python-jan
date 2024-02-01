my_list = ['test', 'test1', 'test1', 'test2']

my_list = list(map(lambda x: x.replace("test1", "JustTest"), my_list))

print(my_list)