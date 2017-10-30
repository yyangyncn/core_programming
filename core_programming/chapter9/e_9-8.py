# 模块研究

mod_name = input('modular name :')
module = __import__(mod_name)
print(dir(module))

for i in dir(module):
    print('name', i)
    print('type:', type(getattr(module, i)))
    print('value:', getattr(module, i))