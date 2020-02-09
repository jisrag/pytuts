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


#Example 4 Index Method

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

#Example 5 in condition
print("zuperc" in word)

#Example 5 - Real Wolrd
#In this example we have to replace the old domain hotmail
# to the new domain  gmail in every call of the function
def replace_domain(email, old_domain, new_domain):
    if "@"+old_domain in email:
        index=email.index("@"+old_domain)
        new_email=email[:index]+"@"+new_domain
        return new_email
    return email


print(replace_domain("dragonich@gmail.com", "hotmail.com", "gmail.com"))
print(replace_domain("pepe@hotmail.com", "hotmail.com", "gmail.com"))
print(replace_domain("dragonich@hotmail.com", "hotmail.com", "gmail.com"))

#Example 6 - Lower
answer="YES"
if answer.lower()=="yes":
    print("User said yes")

#Example 7 delete spaces
sent=" yes ".strip()
print(sent)

sent=" yes ".lstrip()
print(sent)
sent=" yes ".rstrip()
print(sent)

print("The number of times e occurs in this strinsg is 4".count("e"))
print("The number of times e occurs in this strinsg is 4".endswith("is 4"))
print("Forest".isnumeric())
print("1234566".isnumeric())
print("_".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("This is another example of split".split())

#Example 8 with strings
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS