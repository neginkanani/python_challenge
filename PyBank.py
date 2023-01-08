import csv


##### read the csv file and print the results
csv_path="./PyBank/Resources/budget_data.csv"
count_row=0
net=0
change_v=0

with open (csv_path) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    ### finding the header of the columns
    csv_header=next(csv_reader)
    print(f"Originol CSV headers were: {csv_header}")
    # change the header of hte csv file to month, year, profit/losses
    csv_header_modified= ["Month", "Year", "Profit/Losses", "Change"]
    print(f"New CSV headers are: {csv_header_modified}")

    for row in csv_reader:
        count_row=count_row+1
        month_year_profit=row[0].split("-")
        month_year_profit.append(row[1])
        #print(month_year_profit)
        net=int(month_year_profit[2])+net

        # finding the average and greatest change per month
        if count_row == 1:
            month_year_profit.append(0)
            greatest_Increase_change=0
            greatest_Decrease_change=0
            greatest_Increase_change_index=row[0]
            greatest_Decrease_change_index=row[0]

        if count_row != 1:
            month_current=month_year_profit[2]
            # calculating the change
            change=int(month_current)-int(month_before)
            month_year_profit.append(change)

            # calculating the greatest increase change
            if greatest_Increase_change > month_year_profit[3]:
                greatest_Increase_change_index=greatest_Increase_change_index
            else:
                greatest_Increase_change_index=row[0]
            greatest_Increase_change=max(month_year_profit[3],greatest_Increase_change)
            
            # calculating the greatest decrease change
            if greatest_Decrease_change < month_year_profit[3]:
                greatest_Decrease_change_index=greatest_Decrease_change_index
            else:
                greatest_Decrease_change_index=row[0]
            greatest_Decrease_change=min(month_year_profit[3],greatest_Decrease_change)

        month_before=month_year_profit[2]
        print(month_year_profit)

        # calculating the total average change
        change_v=int(month_year_profit[3])+change_v

        
        

    avg_change=change_v/(count_row-1)
    print(f"Total Months: {count_row}")
    print(f"Total: {net}")
    print(f"Average Change: {avg_change}")
    print(f"Greatest Increase in Profits: {greatest_Increase_change_index} (${greatest_Increase_change})")
    print(f"Greatest Decrease in Profits: {greatest_Decrease_change_index} (${greatest_Decrease_change})")


### write the results to a text file
text_path="./PyBank/analysis/export.txt"
lines=[f"Total Months: {count_row}", f"Total: {net}", f"Average Change: {avg_change}",
 f"Greatest Increase in Profits: {greatest_Increase_change_index} (${greatest_Increase_change})",
 f"Greatest Decrease in Profits: {greatest_Decrease_change_index} (${greatest_Decrease_change})"  ]
with open(text_path, 'w') as text_file:
    text_file.write('\n'.join(lines))
    