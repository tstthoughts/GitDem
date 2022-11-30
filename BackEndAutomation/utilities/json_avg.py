#2.      Coding Question: Given 2 JSON objects
# that have marks of 2 students, create a json object that returns the average marks in each subject.
Student1 =  {
            "english": 90,
            "maths": 50,
            "science": 80,
            }
#dict2 = {x:Student1[x] for x in keys}
Student2 =  {
            "english": 70,
            "maths": 70,
            "science": 70,
            }

tot = {}
for subject in Student2:
    tot.update({subject : (Student1[subject] + Student2[subject]) / 2})

print(tot)