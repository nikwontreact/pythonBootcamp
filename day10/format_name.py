# Funtions with output 

def format_name(f_name,l_name):
   formatted_fname = f_name.title()
   formatted_lname = l_name.title()
   return f"{formatted_fname,formatted_lname}"
print (format_name("SOde","NIKHIL"))

# passing fun_1's output as input to fun_2

def fun_1(text):
   return text+text

def fun_2(text):
   return text.title()

output = fun_2(fun_1("hello"))
print(output)