# a= int(input("Enter First Number: "))
# # second_num = int(input("Enter Second Number: "))
# # third_num = int(input("Enter Third Number: "))

# # average = (first_num+second_num+third_num)/3
# # print(type(average))
# # print(average)

# operator = input("Enter Operator: ")
# b = int(input("Enter Second Number: "))

# if operator=="+":
#     print(a+b)
# elif operator=="-":
#     print(a-b)
# elif operator=="*":
#     print(a*b)
# elif operator=="/":
#     print(a/b)
# else:
#     print("Invalid Number......")
# a = int(input("Enter a First Number: "))
# b = int(input("Enter a Second Number: "))

# sum = a + b
# print(type(sum))
# print("The Sum of two Numbers is: "+str(sum))

#print("The Sum of Two Numbers is: " + int(sum))
# name = "Hello Brother"
# print(name.lower())
# nameOfEmployee = input("Enter Name of Employee: ")
# salary = int(input("Enter salary of Employee: "))

# if(salary==15000):
#     print("The Name of Employee is: " + nameOfEmployee)
#     print("The salary of Employee is: " + str(salary))
# elif(salary==20000):
#     print("The Name of Employee is: " + nameOfEmployee)
#     print("The salary of Employee is: " + str(salary))
# else:
#     print("Invalid Data.........")
# a = 3
# b = 4

# print(a!=b)
# age = int(input("Enter age of Voter: "))

# if age>=18:
#     print("you are able to vote")
# else:
#     print("Not Eligible for vote")
# print("Thank you for being here yet again")

# name = "Osama Malik"
# print('Malik' in name)

# print(4//2)
# a = 10
# a = a + 10
# print(a)
# result = (2 + 3) * 5
# print(result)
# numbers = range(5) # 0 , 1 , 2 , 3 , 4 but 5 is not included
# print(numbers)
# Now we are going to learn about loops
# i = 10
# while i>=1:
#     print(i * "*")
#     i = i - 1
# name = "OsamaMalik"
# for character in name:
#     print(character)
# here we declare list data type
# list = ["Osama" , "Faizan" , "Shamsher" , "Khalid"]
# print(list)
# for item in range(1 , 10 , 2):
#     print(item)
# name = "OsamaMalik"
# length = len(name)
# for number in range(length):
#     print(number , " = " , name[number])
# a = input("Enter a: ")
# b = input("Enter b: ")

# sum = int(a) + int(b)
# print("The Sum of Two Numbers is : " + str(sum))
# list = [1 , 2 , 3 , 4 , 5 , 6]
# print(list[2])
# name = "OsamaMalik"
# for numbers in name:
#     print(numbers)
# else:
#     print("End of the program and controller is out of loop")
# marks = [99 , 89 , 100 , 123]
#marks.append(67)
#marks.insert(0 , 500)
# marks.remove(99)
# for item in marks:
#     print(item)
# i = 1
# while i<=len(marks):
#     print(i)
#     i = i + 1
# marks.clear()
# print(marks)

#print(12 in marks)
# students = ["Osama" , "Khasif" , "Faisal" , "Khurram" , "Rana" , "Faizan"]
# students[0] = "Uzair"
# for student in students:
#     if student == "Khurram":
#         continue
#     print(student)
# marks = [45 , 56 , 67 , 89 , 89 ,89]
# print(marks.count(89))

# tuple Example
# marks = (45 , 67 , 78 ,78 , 78 , 78 , 89) # tuple is immutable

# print(marks.index(67))
# marks = {45 , 56 , 78 , 78 , 78 , 78 }
# for i in marks:
#     print(i)
# Now we are going to study about dictionary
# marks = {"English": 78 , "Physics" : 67}

# print(marks["English"])
# marks["Math"] = 89
# print(marks)
# marks["English"] = 100
# print(marks)
# name = "Osama Malik"

# print('g' in name)
# import time

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year to all of you!")

# rows = int(input("Enter rows: "))
# columns = int(input("Enter Columns: "))
# symbol = input("Enter symbol: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")

#     print()

# while True:
#     name = input("Enter Name: ")
#     if(name!=""):
#         break

# marks = [ 67 , 56 , 78 , 90 , 56]
# for items in marks:
    
#     if(items == 90):
#          continue
#     print(items , end="  ")

# for i in range(1 , 22):
#     if i == 15:
#         continue
#     else:
#         print(i , end="  ")

food = ["pizza" , "Karhai" , "Mutton" , "Burger"]
food[0] = "Chicken"

print(food)
food.insert(2 , "pasta")
print(food)


