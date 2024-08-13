# print("Hello World")

# num1= -25.0
# print(num1)
# print(type(num1))



# st =  "Anam @2003"
# st =  'Anam @2003'
# st =  """Anam @2003
# 2
# 3
# dafaf"""
# print(st)
# print(type(st))

#indexing
# st= 'AnamAbdin'
# print(st[3])
# print(st[1:4])
# print(st[:3])
# print(st[3:])

#jump index
# st= 'AnamAbdin'
# print(st[::2])
# print(st[::1])
# print(st[::3])

#converts into uppercase
# st= 'AnamAbdin'
# print(st.upper())
# #converts into lowercase
# print(st.lower())

# functions
# st= 'AnamAbdin'
# print(st.title())
# print(st.capitalize())
# print(st.count("n"))
# print(len(st))
# print(st.find('A'))#prints the index
# print(st.find('a')) #prints the index

# st= 'Anam Abdin'
# print(st.split())

# st= 'Anam,Abdin'
# print(st.split())
# print(st.replace(',',' '))
# print(st.replace("Anam","hello"))
# print(st.replace("Anam"," "))

# st= 'Anam Abdin'
# print(st.endswith('s'))
# print(st.startsswith('A'))

#data type __boolean__
# var1= True
# var2= False
# print(var1,var2)
# print(type(var1),type(var2))
# var = False
# print(var)

# ---------------list--------------------(mutable)
# ls=[10,20,30,40,50,25,41,2.3,'anam',False]
# print(ls)
# print(type(ls))
# print(ls[4])
# print(ls[-6])

# ls= [10,20,30,40,50,60,70,80]
# print(ls[2:])

#insert,delete
# student_name=['mohit','vikram','kanha','anam']
# print(student_name)
# student_name.append('abhipsa')
# print(student_name)
# student_name.pop(0)
# print(student_name)

# student_name=['mohit','vikram','kanha','anam']
# student_name[-1] = "rohit"
# student_name.append('rohit')
# student_name.insert(0,'Manshi')
# print(student_name)

# ls=[12,23,343,54,32,2,45,56,76,57]
# print(ls.count(54))
# print(len(ls))
# ls.sort()
# ls.reverse()
# ls.index()
# ls.clear()

# ls= [10,20,30,40,50,False,[2,4,1,5,'Anam'],12]
# print(ls[6])
# ls[6][4]='flipkart'
# print(ls)

#--------------- TUPLE-----------------------(immutable)
# tpl=(12,43,54,65,23,12.3,23.4,5.5,'anam')
# print(tpl)
# print(type(tpl))
# tpl.count()
# tpl.index()
# print(tpl[2:])

# access==yes
# remove==No
# insert==No
# update==no

# tpl= 12,43,54,65,23,12.3,23.4,5.5,'anam'
# print(type(tpl))


#---------------SET-----------
#duplicates will not allow
# doesn't maintain order
#immutable
#indexing not allowed
# st={12,43,54,65,23,12.3,23.4,5.5}
# print(st)
# print(type(st))
# st.remove(43) #raises error
# print(st)
# st.discard(54) #not error
# print(st)
# st.add(3)
# print(st)

#--------------DICTIONARY----------
# dt = {10,20,30,40,50}
# dt={'A':10,'B':12,'C':14,'D':16}
# dt={0:12,1:23,2:34}
# dt={0:[12],1:{23},2:34}
# dt={'A':10,'B':12,'C':14,'D':16}
# print(dt['B'])
# print(type(dt))

# dt={'A':10,'B':12,'C':14,'D':16}
# print(dt)
# dt['D'] = 300 #to update
# dt['E'] = 50  #to insert
# print(dt)
# dt.pop('A')
# print(dt)

# dt={'A':10,'B':12,'C':14,'D':16}
# print(dt.keys())
# print(dt.values())

# student_marks = {"name": ['manshi','ram','kishan','harsh'],"marks":[25,41,52,63],"subject":'Science'}
# print(student_marks)
# print(type(student_marks))
# print(student_marks['marks'])
# student_marks["name"].pop(1)
# student_marks["marks"].pop(1)
# student_marks["name"].insert(1,'Anam')
# student_marks["marks"].insert(1,'55')
# student_marks["name"][1]="abhipsa"
# print(student_marks)
# student_marks["subject"]="Data Science"
# print(student_marks)
# dir(student_marks)

# ---------CONDITIONAL STATEMENTS-------
# age = 22
# if age > 21:
#     print('You are eligible')
# if age<=21 :   
#     print("You cannot vote") 

# print(task)
# print(type(task))
# int(),str(),float(),list(),set(),tuple(),dict()
# int=->float

##to change datatype
# num1 =10.25
# num1 = int(num1)
# print(num1)
# print(type(num1))


## WRITE A PROGRAM
# name=input("Enter your name")
# print("hello",name)
# message="""How may I help you 

# Please select any of them option,
# Type 1 >>>> CHECK BALANCE.
# Type 2 >>>> DEPOSIT.
# Type 3 >>>> WITHDRAWL."""

# print(message)
# task= int(input('plz choose any option: '))
# available_amount=5000

# if task >=1 and task <=3:
#     print('welcome to the virtual world')
#     if task == 1:
#         #check balance
#         print("Thanks for visiting us, your availble amount is: ", available_amount)
#     elif task ==2:
#         #deposit amount
#         deposit_amount = int(input("plz enter your deposit amount:"))
#         if deposit_amount>=500:
#             available_amount = available_amount + deposit_amount
#             print('You have successfully deposit your amount:',deposit_amount)
#             print('You have successfully deposit your amount:',available_amount)
#         else:
#             print("Please deposit atleast 500")
#     else: #3
#        withdrawl_amount= int(input("plz enter your withdrawal amount:"))
#        if  withdrawl_amount < available_amount:
#            print("You have successfully withdrawl your amount:",withdrawl_amount)
#            print("Available amount:", available_amount- withdrawl_amount)
#        else:
#            print("Amount available is insufficient")
# else:
#     print('please choose correct option!')    


#EXCEPTION AND ERRORS
# EXception-unwanted and unexpected situations ko handle karne ke lia.
# try, except, else, finally
#checks errors
# try:
#   name=input("please enter your name ")
#   print("Hello :" ,name)
#   age=input("please enter your age ")
#   print(f"hey! this is {name} i am {age} old")
# #when error occurs
# except:
#   print("please enter valid input")
#   #when no error occurs
# else:
#   print("you have entered valid input")
# #always execute
# finally:
#   print("thank you for using our service")

# print("this is important line please execute it 1")
# print("this is important line please execute it 2")
# print("this is important line please execute it 3")
# print("this is important line please execute it 4")
# print("this is important line please execute it 5")

##Module
