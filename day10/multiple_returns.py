# function with multiple return statements
def format_name (fname,lname):
    if fname == "" or lname == "":
        return "you have not provided names"
    
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"Result: {formatted_fname,formatted_lname}"

print(format_name(input("whats your first name \t"), input("what is your last name \t")))