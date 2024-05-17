import random

def generate(category):
   category_to_int = {
        "math": 0,
        "physics": 1,
        "chemistry": 2,
        "sports": 3,
        "iq": 4
    }
   questions = [
        # math_questions
        [
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is 5 multiplied by 3?", "answer": "15"},
            {"question": "What is the square root of 9?", "answer": "3"},
            {"question": "What is 10 divided by 2?", "answer": "5"},
            {"question": "What is 3 squared?", "answer": "9"},
            {"question": "What is the sum of angles in a triangle?", "answer": "180"},
            {"question": "What is the perimeter of a square with sides of length 4 units?", "answer": "16"},
            {"question": "What is the area of a rectangle with length 6 units and width 4 units?", "answer": "24"},
            {"question": "What is the circumference of a circle with radius 5 units (use π = 3.14)?", "answer": "31.4"},
            {"question": "What is the value of 3 to the power of 4?", "answer": "81"}
        ],
        # physics_questions
        [
            {"question": "What is the unit of force in the International System of Units (SI)?", "answer": "Newton"},
            {"question": "What is the acceleration due to gravity on Earth's surface (approximately)?", "answer": "9.8"},
            {"question": "What is the SI unit of energy?", "answer": "Joule"},
            {"question": "What is the SI unit of power?", "answer": "Watt"},
            {"question": "What is the SI unit of electric charge?", "answer": "Coulomb"},
            {"question": "What is the SI unit of electric current?", "answer": "Ampere"},
            {"question": "What is the number of newton law that states that for every action, there is an equal and opposite reaction?", "answer": "3"},
            {"question": "What is the speed of light in a vacuum ... m/s ?", "answer": "300,000,000"},
            {"question": "What is the SI unit of frequency?", "answer": "Hertz"}
        ],
        # chemistry_questions
        [
            {"question": "What is the chemical symbol for gold?", "answer": "Au"},
            {"question": "What is the chemical symbol for water?", "answer": "H2O"},
            {"question": "What is the state of matter with no fixed shape or volume?", "answer": "Gas"},
            {"question": "What is the process of converting a solid directly into a gas?", "answer": "Sublimation"},
            {"question": "What is the opposite of reduction in a redox reaction?", "answer": "Oxidation"},
            {"question": "What is the lightest element on the periodic table?", "answer": "Hydrogen"},
            {"question": "What is the chemical name for table salt?", "answer": "Sodium chloride"},
            {"question": "What is the atomic number of carbon?", "answer": "6"},
            {"question": "What is the chemical name for rust?", "answer": "Iron oxide"},
            {"question": "What type of bond shares electrons between atoms?", "answer": "Covalent"}
        ],
        # sports_questions
        [
            {"question": "What sport is played with a cue and balls on a rectangular table covered with cloth?", "answer": "Billiards"},
            {"question": "In which sport do athletes throw a heavy metal ball as far as possible?", "answer": "Shotput"},
            {"question": "What sport involves hitting a shuttlecock back and forth over a net with a racket?", "answer": "Badminton"},
            {"question": "In which sport do participants use a board to ride on waves?", "answer": "Surfing"},
            {"question": "What sport involves jumping over a bar set at increasing heights?", "answer": "High jump"},
            {"question": "What sport involves hitting a small, hard ball into a series of holes on a course using the fewest possible strokes?", "answer": "Golf"},
            {"question": "In which sport do teams of players try to throw a ball into the opposing team's net to score points?", "answer": "Basketball"},
            {"question": "What sport involves using your feet to kick a ball into a goal to score points?", "answer": "Soccer"},
            {"question": "In which sport do athletes compete to see who can run the fastest over a specific distance?", "answer": "Sprint"},
            {"question": "What sport involves hitting a round ball with a bat and running around bases to score runs?", "answer": "Baseball"}
        ],
        # iq_questions
        [
            {"question": "What is the next number in the sequence: 1, 4, 9, 16, ...?", "answer": "25"},
            {"question": "If all apples are fruits and some fruits are oranges, can you conclude that some apples are oranges? yes/no", "answer": "No"},
            {"question": "Which word does not belong in the following group: apple, banana, carrot, potato? ", "answer": "Carrot"},
            {"question": "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?", "answer" : "5"},
            {"question": "What is the missing number in the sequence: 2, 4, 8, 16, ...?", "answer": "32"},
            {"question": "A baseball bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?", "answer": "0.05"},
            {"question": "If 5 cats can catch 5 mice in 5 minutes, how many cats are needed to catch 100 mice in 100 minutes?", "answer": "5"},
            {"question": "Which number is the odd one out: 2, 3, 5, 7, 11?", "answer": "2"},
            {"question": "What comes next in the sequence: 1, 4, 9, 16, 25, ...?", "answer": "36"},
            {"question": "How many triangles are in the following figure?\n*\n**\n***\n****\n*****", "answer": "15"}
      ]
   ]
   grade = 0
   index = []
   for count in range( 1 , 6):
      i = random.randint(0 , 9)
      while i  in index :
         i = random.randint(0 , 9)
      index.append(i)
      Ques = questions[category_to_int.get(category)][i]
      # Printing the first question
      print("Question:", Ques["question"])
      Ans = input("Answer : ")
      if Ans.lower() == Ques["answer"].lower() :
         grade = grade + 1
      file = open(r"D:\Codes\Quiz\QuizAns.txt", "a")
      #file.write(Ques)
      # file.write( " : " )
      # file.write( Ques)
      file.write( "\n")
      file.write("Your Answer : " )
      file.write( Ans)
   return grade
   
      
      
      
   

  

   

