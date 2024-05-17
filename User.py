def register() :
   print("******************** Create a new account ******************** ")
   user_name = input("Enter your user name : ")
   password = input("Enter your password : ")

   file = open(r"D:\Codes\Quiz\userFile.txt", "a")
   file.close()

   file = open(r"D:\Codes\Quiz\userFile.txt", "r")
   content = file.read()
   file.close()

   if user_name in content and password in content :
      print("Sorry!! User already exist")

   else :
      print("Congratulation. A new account created succefully")
      file = open(r"D:\Codes\Quiz\userFile.txt", "a")
      file.write(user_name)
      file.write("\n") 
      file.write(password)
      file.write("\n")
      file.close()
################################################################  
def Login () :
   file = open(r"D:\Codes\Quiz\userFile.txt", "r")
   content = file.read()
   file.close()

   user_name = input( "User name : ")
   if user_name in content :
      password = input( "Password : ")
      if password in content :
         print( "Get Ready to the Krok exam -_- ")
      else :
         print ("Incorrect Password! ")
   else :
      print ( "User name not found! ")
################################################################