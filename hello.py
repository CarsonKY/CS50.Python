# print user name
print ("Winston is coool");
name = input ("Who is this  ") ;
print ("Nice to meet you "+ name); 

# print user name but stay on same line
print ("Nice to meet you ", end="")
print (name); 

#change space to symbols. Sep is a parameter
print ("Nice to meet you ", name,  sep="!$!$")
 
# strip out any extra spaces
name = name.strip()

# Cap first word
name = name.capitalize()
print (name); 

# Cap all words
name = name.title()
print (name); 

# strip and title
name = name.strip().title()
print (name); 

#combine one line
name2 = input ("Who is this  ").strip().title() ;
print ("Nice to meet you "+ name2); 

# testing home commit
