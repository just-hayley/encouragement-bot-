name = input("What is your name?")
print("Hello " + name)
print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("tomorrow will be a better day and the anger will go away")
      counter += 1
    if each_word == "frustrated":
      feelings_list.append("frustrated")
      encouragement_list.append("tomorrow will be a better day and the frustration will go away")
      counter += 1      
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("excellent! you should always be happy and keep smiling")
      counter += 1
    if each_word == "annoyed":
      feelings_list.append("annoyed")
      encouragement_list.append("tomorrow will be a better day and it is better to put away everything else and be happy")
      counter += 1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("tomorrow will be a better day and it is better to put away everything else and be happy")
      counter += 1      
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("do something you like and enjoy yourself! your revision can come later. what matters most is your health :)")
      counter += 1
    if each_word == "confident":
      feelings_list.append("confident")
      encouragement_list.append("that's great! all the best for your exams")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
