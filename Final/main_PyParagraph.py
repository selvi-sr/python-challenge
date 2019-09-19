import csv
import os
import re


input_file= os.path.join("..", "Resources","paragraph.txt")
#input_file="paragraph.txt"

with open(input_file, 'r')as f:
    read_data = f.read()
    #print(read_data)
     
    word = len(re.findall(r'\w+', read_data))
    sent_count=read_data.count('.')
    letter_count=len(read_data)
    avg_sent_len=int(word/sent_count)
    avg_let_count=letter_count/word

print("Paragraph Analysis")
print("---------------------")
print ("Approximate Word Count: " +  str(word))
print('Approximate Sentence Count:' + str(sent_count))
print('Average Sentence Length: ${:.1f}'.format(avg_sent_len))
print ('Average Letter Count: ${:.1f}'.format(avg_let_count))
    
