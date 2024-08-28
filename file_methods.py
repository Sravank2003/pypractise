#open file using python code:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
# content=sravan.read()
# print(content)

#Read method using python code:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","a")
# sravan.write("We are dealing with python handling methods")
# sravan.close()
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
# content=sravan.read()
# print(content)

#Writable method:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","a")
# print(sravan.writable())

#Readable method:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","a")
# print(sravan.readable())

#Write Lines:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","a")
# sravan.writelines(["We are dealing with python handling methods\n",
#              "We are dealing with python handling methods\n",
#              "We are dealing with python handling methods\n",
#              "We are dealing with python handling methods\n"])
# sravan.close()
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
# content=sravan.read()
# print(content)

#Read Lines:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
# print(sravan.readlines())

#Close Methos:
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
# print(sravan.read())
# sravan.close()

#Truncate Method:used for resizing the file size(kind of log notations)
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","a+")
# sravan.truncate(100)
# sravan.close()
# sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
# print(sravan.read())

#Seek Method:Position of the file
sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
sravan.seek(0)
print(sravan.readline())

#Untruncate Method:
sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","a+")
sravan.seek(100)
sravan.write("\x00")
sravan=open("C:\\Users\\VARA PRASAD\\OneDrive\\Documents\\Desktop\\test folder\\Sravan.txt","r")
print(sravan.readline())