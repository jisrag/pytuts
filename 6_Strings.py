#Example 1 - Multuplying strings
def double_word(word):
    return word*2 + str(len(word*2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#Exampl 2 - String Indexing

def first_and_last(message):
    if message!="":
        msg1=message[0]
        msg2=message[-1]
        if msg1 == msg2 :
            return True
    else:
                return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#Example 3 - Slice String
color="Orange"
print(color[1:4])
print(color[:4])
print(color[4:])
