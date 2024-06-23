car_colors = {1: 'blue', 2: 'green', 3: 'white', 4: 'black'}

def f_separate():
    print("#################")

# with print
def car_f():
    print("car colors")
car_f()
f_separate()
# with return
def carf2():
    msg = 'color of cars'
    return msg
print(carf2())
f_separate()

def f_parameter(num):
    #return 'car_color = ' + car_colors[num]
    return f'car_color = {car_colors[num]}' 

print(f_parameter(2))
f_separate()

def car_col(n, text="Salam"):
    return f'{text} car_col:  {car_colors[n]}' 

print(car_col(2))
f_separate()

def car_info(*args, **kwargs):
    print(args)
    print(kwargs)

cities = ['Tehran', 'Paris']
specs = {'year': 1965, 'city': 'Hoston'}

car_info(*cities, **specs)