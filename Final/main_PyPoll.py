#importing dependecies
import csv
import os
#input file loc
input_file = os.path.join("..", "Resources","election_data.csv")
#input_file="election_data.csv"
#output_file="election_data_out.txt"
output_file=os.path.join("..", "Resources","election_data_out.txt")

outFile=open(output_file, "w+")
def printOut(feed):
     print(feed)
     outFile.write(feed)
     outFile.write("\n")




candidate_vote_count_d = {}
# read file
with open(input_file, "r") as input_data:
   csvreader = csv.reader(input_data, delimiter=",")
   # skip header
   csv_header = next(csvreader)
   total_votes = 0
   vote_count = 0
   # reading the input file one row at a time
   for row in csvreader:
       candidate_name = row[2]
       total_votes = total_votes + 1
       

       if candidate_name in candidate_vote_count_d:
           vote_count = candidate_vote_count_d.get(candidate_name)
           vote_count = vote_count + 1
           candidate_vote_count_d[candidate_name] = vote_count
       

# fetching candidate names as key 
       else:
           candidate_vote_count_d[candidate_name] = 1
   # calculate percentage for each candidate
   # display winner
# display output
printOut("Election Results")
printOut("---------------------------")
printOut("Total Votes: {}".format(total_votes))
printOut("---------------------------")



#iterating through candidate_vote_count dictionary
for candidate, votes in candidate_vote_count_d.items():
   
   #calculate vote percenatge and format to print
   vote_percent = format((votes/total_votes)*100,".3f")
   
   printOut("{} : {}% ({})".format(candidate, vote_percent ,votes))
   
  #find the winner
   winner_votes = max(candidate_vote_count_d.values())
   if votes == winner_votes:
       winner = candidate
printOut("---------------------------\n")
printOut("Winner: {}".format(winner))
printOut("---------------------------")



