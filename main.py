# Weighted Mark Calculator

# Knowledge
knowledge = float(input("Please enter your knowledge weighting: "))
knowledge = knowledge/100
knowledge_outof = float(input("Please enter your knowledge out of: "))
knowledge_marks = float(input("Please enter your knowledge marks: "))
kmark = knowledge_marks/knowledge_outof
kfinal = kmark*knowledge

# Communication
communication = float(input("\nPlease enter your communication weighting: "))
communication = communication/100
communication_outof = float(input("Please enter your communication out of: "))
communication_marks = float(input("Please enter your communication marks: "))
cmark = communication_marks/communication_outof
cfinal = cmark*communication

# Thinking
thinking = float(input("\nPlease enter your thinking/inquiry weighting: "))
thinking = thinking/100
thinking_outof = float(input("Please enter your thinking/inquiry out of: "))
thinking_marks = float(input("Please enter your thinking/inquiry marks: "))
tmark = thinking_marks/thinking_outof
tfinal = tmark*thinking

# Application
application = float(input("\nPlease enter your application weighting in decimals: "))
application = application/100
application_outof = float(input("Please enter your application out of: "))
application_marks = float(input("Please enter your application marks: "))
amark = application_marks/application_outof
afinal = amark*application

# Adds each mark and multiplies it to 100 to make it a percent.
final_mark = 100*(float(kfinal) + float(cfinal) + float(tfinal) + float(afinal))
final_mark_rounded = round(final_mark, 1)

if 100 >= final_mark_rounded >= 0:
    print("Your final mark is:", final_mark_rounded, "%")

else:
    print("Error, mark is not between 0 and 100%")
