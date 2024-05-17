import User
import Questions


########################################################

print("********** Welcome to krok exam **********")
ifNew = input("Are you new user ? Y/N :   ").lower()
if ifNew == "y" :
   User.register()
else :
   User.Login()

################################################################

print("**********Choose 3 Categories from : **********")
print("1. Math \n2. Physics \n3. Chemistry \n4. Sports \n5. iq\n")

cat1 = input("select 1st category : ").lower()
cat2 = input("select 2nd category : ").lower()
cat3 = input("select 3rd category : ").lower()

grade1 = Questions.generate(cat1)
grade2 = Questions.generate(cat2)
grade3 = Questions.generate(cat3)

print("\n******************** Your Report ********************\n")
print( "Total Score = ", grade1 + grade2 + grade3)
print( cat1 , "Score = " , grade1)
print( cat2 , "Score = " , grade2)
print( cat3 , "Score = " , grade3)   