student_scores = [78,92,65,45,56,68,89,56,68,8]

max_score = 0                                                   #Find Max Score
for score in student_scores :
    if score > max_score :
        max_score = score

min_score = max_score                                            #Find Minimun Score
for score in student_scores :
    if score < min_score :
        min_score = score

total_score=0                                                      #Find Average Score 

for score in student_scores:
    total_score = score+total_score
    
average_score = total_score/len(student_scores)
                                                                    
print(f"Highest Score is {max_score}.")                                #Show result
print(f"Minimun Score is {min_score}.")
print(f"Average Score is {average_score:.2f}")


