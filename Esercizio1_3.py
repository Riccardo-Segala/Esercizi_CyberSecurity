import Esercizio1_1
import Esercizio1_2

valid_words = {}
total_points = 0

for line in open("words.txt","r"):
    if(Esercizio1_1.check_word(line.strip(),'ACDLORT', 'R')):
        valid_words[line] = Esercizio1_2.score_word(line.strip(),'ACDLORT')
        total_points += Esercizio1_2.score_word(line.strip(),'ACDLORT')

print(valid_words)
print("Total points: "+ str(total_points))