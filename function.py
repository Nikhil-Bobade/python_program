# # # def login():
# # #     username=input("Enter you User name: ")
# # #     password=input("Enter you password : ")

# # #     if username=="Nikhil" and password=="5050":
# # #         print("Login succesfully")
# # #     else:
# # #         print("Login faild")    

# # # login()



        




# # def login(username,password):  # parameters
# #     if username=="Nikhil" and password=="5050":
# #         print("Login successful")
# #     else:
# #         print("Login failed")


# # login("Nikhil","5050")


# # def prime(n):
# #     for i in range(2,n):
# #         if n%i==0:
# #             print("Not a prime number")
# #             break

# #         else:    
# #             print("It is prime number")

# # prime(3)



# # def prime(n):
# #     i=2
# #     while i<=100:
# #         if n%i==0:
# #             print("Not a prime number")
# #             break
# #         else:
# #             print("It is prime number")

# # prime(60)


# num=int(input("Enter a number: "))

# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("It is not prime number")
#             break
#     else:
#         print("It is prime nummber")
# else:
#     print("Please enter number greater than 1")



for i in range(2,100):
    for j in range(2,i):
        if i%2==0:
            break
    else:
        print(i)    
        

    