def option9():
     answer = input("What is your string? ")
     encoded_str = ""
     for i in answer:
        encoded_char = chr(ord(i)+1)
        print(i + '=' + encoded_char)
        encoded_str += encoded_char
        #encoded_str = encoded_str + encoded_char
        print(encoded_str)

option9()