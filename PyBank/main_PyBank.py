# Importing the operating system module
import os
# Importing the csv file needed to work with
import csv
#Calling or setting the csv file path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Defining the variable list

count = 0    #count of each row
total_months = 0 # total months in the data set
average_changes = 0 # average change
net_total = 0 # total profit/loss
current = 0
total_change = 0 #total change from month 1 to last month
greatest_increase = 0 
greatest_decrease = 0
greatest_increase_date = "" #greatest increase date
greatest_decrease_date = "" #greatest decrease date

m_changes_profit_loss = 0 #monthly change
total_profit = 0 # total profit
total_change_profits = 0
profit_loss = []
ini_profit_loss = 0 # initital starting profit
dates = []
monthly_change = []
prev_change = 867884

# Open the csv file to read    
with open(budget_data_csv) as csv_file:

    # Initiating the csv reader
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)

    count = 0
    net_total = 0
    dates = []

    # Reading through each row of data after reading the header
    for row in csv_reader:

        dates.append(row[0])  
        profit_loss.append(row[1])
        count += 1
        net_total += float(row[1])
        current = float(row[1])
        net_change = current - prev_change
        average_changes += float(row[1])
        total_profit = total_profit + int(row[1])
        final_profit_loss = int(row[1])

        #calculating monthly profits and losses
        monthly_change.append(net_change)
        total_change_profits = sum(monthly_change)
        ini_profit_loss = final_profit_loss
        average_changes = round((total_change_profits/count), 2)
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
        greatest_increase_date = dates[monthly_change.index(greatest_increase)]
        greatest_decrease_date = dates[monthly_change.index(greatest_decrease)]
        prev_change = current
    # Generating the output
    output = os.path.join("Analysis/financialanalysis.txt")

    with open(output, 'w')as txtfile:
       #output =[  
            txtfile.write(f"Financial Analysis Results"  "\n")
            txtfile.write(f"-------------------------------------------------- \n")
            txtfile.write(f"Total Number of Months: {count}  \n")
            txtfile.write(f"Net Total Amount of 'Profit/Losses': ${net_total} \n")
            txtfile.write(f"Average Change in 'Profits/Losses': ${average_changes} \n")
            txtfile.write(f"The Greatest Increase in Profits: {str(greatest_increase_date)} ${str(greatest_increase)} \n")
            txtfile.write(f"The Greatest Decrease in Profits: {str(greatest_decrease_date)} ${str(greatest_decrease)} \n")
            txtfile.write(f"-------------------------------------------------\n")
              # ]
    # Printing the results
    print(f"Financial Analysis Results")
    print(f"---------------------------------------------------------------")
    print(f"Total Number of Months:", str(count))
    print(f"Net Total Amount of 'Profit/Losses':" + " $" + str(net_total))
    print(f"Average Change in 'Profits/Losses':" + " $" + str(average_changes))
    print(f"The Greatest Increase in Profits: " + str(greatest_increase_date) + " $" + str(greatest_increase))
    print(f"The Greatest Decrease in Profits: " + str(greatest_decrease_date) + " $" + str(greatest_decrease))
    print(f"---------------------------------------------------------------")
