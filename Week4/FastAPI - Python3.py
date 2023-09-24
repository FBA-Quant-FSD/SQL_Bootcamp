'''
# print() : 파이썬 내장 함수

print("Hello and welcome to functions!")


def my_function():
    print("Inside my_function")
#이것만 하면 Run 했을 때 아무일도 안 일어남

#출력
my_function()  # 괄호 안 : parameter(매개변수)



def print_my_name(name):
    print(f"Hello {name}!")
    
print_my_name('Eric')



#여러 개 parameter 넣기
def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    
print_my_name("Steve","Jobs")



def print_color_red():
    color = "Red"   # local variable - 함수 안에서만 적용
    print(color)

color = "Blue"      # global variable
print_color_red()       # Red 출력



def print_numbers(highest_num, lowest_num):
    print(highest_num)
    print(lowest_num)
 
print_numbers(lowest_num = 3, highest_num = 10)



def multiply_numbers(a,b):
    return a*b

multiply_numbers(10,3)      #이렇게 하면 안됨!

solution = multiply_numbers(10,3)
print(solution)



# parameter로 list 넣기
def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)
        
number_list = [1,2,3,4,5]
print_list(number_list)



def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

final_cost = buy_item(50)
print(final_cost)



# Functions Assignment
# 답1

def name_age(firstname, lastname, age):
    sol = {f'firstname : {firstname}'
           f'lastname: {lastname}' 
           f'age:{age}'}
    return sol

seungyeop = name_age('David','King',155)
print(seungyeop)


'''
# 답2
def name_age(firstname, lastname, age):
    sol = {'firstname' : firstname,
           'lastname': lastname, 
           'age':age}
    return sol

seungyeop = name_age('David','King',155)
print(seungyeop)

