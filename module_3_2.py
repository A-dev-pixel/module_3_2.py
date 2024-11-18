def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params("String")
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list=[4,False,0.8]
values_dict={"a":7, "b":True, "c":9}
print_params(*values_list)
print_params(**values_dict)
values_list_2=[0.7,False]
print_params(*values_list_2, 42)
