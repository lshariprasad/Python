def emojies_converter(message):
    words = message.split(' ')
    emojies = {
        ":)" : "😊" ,
        ":(" : "😞" ,
        ":0" :"😮" 
    }
    output = ""
    for word in words:
        output += emojies.get(word, word) + " "
    return output


message = input("->")
print(emojies_converter(message))