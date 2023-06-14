##def get_full_name(first_name, last_name, formatter):
##    return formatter(first_name, last_name)
##
##full_name = get_full_name(
##    'John',
##    'Doe',
##    lambda first_name, last_name: f"{first_name} {last_name}"
##)
##print(full_name)
##
##full_name = get_full_name(
##    'John',
##    'Doe',
##    lambda first_name, last_name: f"{last_name} {first_name}"
##)
##print(full_name)

##def times(n):
##    return lambda x: x * n
##double = times(2)
##result = double(2)
##print(result)
##
##result = double(3)
##print(result)

callables = []
for i in (1,2,3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
    
