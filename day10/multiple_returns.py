# function with multiple return statements
def format_name (fname,lname):
#   docstring to document your code -> """ below is docstring hover
#  on that function to get its detail and 
# must be return after declaration of that function
# """ 
    """takes first name and last name from user returns formatted names"""
    if fname == "" or lname == "":
        return "you have not provided names"
    
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"Result: {formatted_fname,formatted_lname}"

print(format_name(input("whats your first name \t"), input("what is your last name \t")))