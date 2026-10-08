# ####lamda functins#######

# s = lambda x,y:x+y
# print(s(2,3))

####### even/odd #######
s = lambda x:"even" if x%2==0 else "odd"
print(s(4))

###### largest of 2 no ##############3
s = lambda x,y:"x is greatest"if x>y else "y greater"
print(s(2,3))

########square#########

s = lambda x:x*x
print(s(5))

######cube ##########
s = lambda x:x**3
print(s(5))

########positive negative#####
s = lambda n:"positive"if n>0 else "negative"
print(s(-5))