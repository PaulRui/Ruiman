#import re
# text="""Giraffes have aroused of _PLURAL_NOUN_ since the living _BODYPART_
#         it legs and _BODY_."""
# def mad_libs(mls):
#     hints=re.findall("_.*?_",mls)
#     if hints is not None:
#         for word in hints:
#             q="Enter a {}".format(word)
#             new=input(q)
#             mls=mls.replace(word,new)
#         print("\n")
#         #mls=mls.replace("\n","")
#         print(mls)
#     else:
#         print("invalid mls")
#
#
# mad_libs(text)
# line="I love $"
# l=re.findall("\$",line,re.IGNORECASE)
# print(l)
# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#    print( matchObj.group())
#    print( matchObj.group(1))
#    print( matchObj.group(2))
# else:
#    print("No match!!")
# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#    print("match --> matchObj.group() : ", matchObj.group())
# else:
#    print("No match!!")
#
# searchObj = re.search( r'dogs', line, re.M|re.I)
# if searchObj:
#    print("search --> searchObj.group() : ", searchObj.group())
# else:
#    print("Nothing found!!")



# import re
#
# phone = "2004-959-559 # This is Phone Number"
#
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print("Phone Num : ", num)
#
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print("Phone Num : ", num)





from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello,World"

app.run(port='8000')
