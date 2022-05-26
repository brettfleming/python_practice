#this is last semesters gradebook its set up as a 2D list
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#list of subjects for this semster of class
subjects = ['physics', 'calculus', 'poetry', 'history']
#grades for the classes listed above
grades = [98, 97, 85, 88]

#combining the lists above into a 2D list
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
#print(gradebook)

#adding the new subject and grade to the end of the list
gradebook.append(['computer science', 100])
#print(gradebook)

#adding the finale suject and grade to the end of the list
gradebook.append(['visual arts', 93])
#print(gradebook)

#selecting the visual arts grade and adjusting the garde
gradebook[-1][-1] += 5
#print(gradebook)

#removing the grade for poetry
gradebook[2].remove(85)
#print(gradebook)

#adding the pass/fail element to the poetry list 
gradebook[2].append('Pass')
#print(gradebook)

#combining last semseters gradebook with the new gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)