message = input("->")
words = message.split(' ')
emojies = {
    ":)" : "😊" ,
    ":(" : "😞" ,
    ":0" :"😮" 
}
output = ""
for word in words:
    output += emojies.get(word, word) + " "
print(output)