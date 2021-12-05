#already used functions with outputs
length = len(formatted_name)

#return as early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to turn the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide a valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

#if you highlight the brackets below you can see the note
format_name()


