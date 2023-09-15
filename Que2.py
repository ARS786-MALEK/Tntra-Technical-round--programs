""""Determine whether a given string is Palindrome or not"""""
n=list(input("enter the list ").split())
def fun(list):
     for i in list:
         if i[::-1]==i:
             print("the string is pallindrome")
         else:print("not")
fun(n)
