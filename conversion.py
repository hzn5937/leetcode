import pyperclip
string = input("Enter your stirng: ")
new = string.replace(". ",".")
new = new.replace(" ", "_")
new = new.lower()
new += ".py"
print(new)
pyperclip.copy(new)
