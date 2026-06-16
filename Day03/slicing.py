# Slicing = create a substring by extracting elements from
#           another string indexing[] or slice[]
#           [start:stop:step]

name = "Arun Boban"
# 012... like this the address or order of name of the letter
first_name = name[:4] # it will help to select 1st 4 letter from the text
last_name = name[5:] # it will help to select the text from 5th to till the end
rev = name[::-1] # "::-1 means from the last to 1st"
part = name[5:8] # "n:m" means from a 
print(first_name)
print(last_name)
print(rev)
print(part)