monday_class = {"Alice","bob","charlie","Diana"}
Wednesday_class ={"bob","Diana","Eve","frank"}

monday_class.add("Grace")
print("Monday Class",monday_class)
print("Wednesday class",Wednesday_class)
bothClass = monday_class & Wednesday_class
print("Attend both class",bothClass)
allstudent = monday_class | Wednesday_class
print("attended either class",allstudent)
onlyOne = monday_class ^ Wednesday_class
print("only one class",onlyOne)
print("is monday subset of all students ?",monday_class <= allstudent)
