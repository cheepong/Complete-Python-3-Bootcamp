import string

def cap_text(text):
    return string.capwords(text)  
    # replace .capitalize() with .title()
    # then subsequently replace text.title() to string.capwords(text)