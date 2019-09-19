import csv
import os

input_file= os.path.join("..", "Resources","budget_data.csv")
#input_file="budget_data.csv"
#output_file="budget_data_out.txt"
output_file= os.path.join("..", "Resources","budget_data_out.txt")

outFile=open(output_file, "w+")
def printOut(feed):
     print(feed)
     outFile.write(feed)
     outFile.write("\n")



with open(input_file, 'r')as fileholder:
    csvreader=csv.reader(fileholder, delimiter = ",")
    next(csvreader)


    profit=0
    loss=0
    count=0
    change=[]
    initial_value=0
    totalMonths=0
    total=0
    average_change=0
    G_change={}
    for row in csvreader:
    
    
    
        # number of rows is total months
       totalMonths = totalMonths + 1
       #sum of all profit/loss is the total
       total = int(row[1]) + total
       current_value = int(row[1])
       # calculate each profit/loss change
       change_value = current_value - initial_value
       #dict will store change value and corresponding date
       G_change[change_value] = row[0]
       initial_value = current_value
       
    change_val_l=list(G_change.keys())		
    del change_val_l[0]
    new_total=totalMonths-1   
    average_change=(sum(change_val_l)/new_total)
    
    
    #get largest key for greatest increase
    greatest_increase = max(G_change.keys())
    greatest_inc_date = G_change.get(greatest_increase)
                #get smallest key for greatest decrease
    greatest_decrease = min(G_change.keys())
    greatest_dec_date = G_change.get(greatest_decrease)



printOut("Financial Analysis")
printOut("-------------------------------")
printOut('Total Months: {}'.format(totalMonths))
printOut('Total : {}'.format(total))
printOut('Average Change : ${:.2f}'.format(average_change))
printOut('Greatest Increase in Profits: {} (${})'.format(greatest_inc_date,greatest_increase))
printOut('Greatest Decrease in Profits: {} (${})'.format(greatest_dec_date,greatest_decrease))





