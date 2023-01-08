
import csv
csv_path= "./PyPoll/Resources/election_data.csv"
Ballot_ID=[]
County=[]
Candidate=[]
count=0
unique_data1=[]
unique_data2=[]
unique_data3=[]
output=[]

# read the excel file
with open(csv_path) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    csv_header=next(csv_reader)
    print(f"csv header: {csv_header}")

#find a list of all the columns information and count the total number of rows
    for row in csv_reader:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        data=[Ballot_ID, County, Candidate]
        count=count+1
        
    # finding the unique candidates
    unique_candidate=list(set(Candidate))
    print(unique_candidate)
    
print("Election Results")
print("------------------")
print(f"Total Votes: {count}")
print("------------------")

### preparing the output folder to export to the text file
output=[f"Election Results", "--------------",f"Total Votes: {count}",  "--------------"]

for j in unique_candidate:
    count_c=Candidate.count(j) 
    percentage=count_c/count*100
    unique_data1.append(count_c)
    unique_data2.append(percentage)
    unique_data3.append(j)
    unique_data=[unique_data1,unique_data2,unique_data3]
    print(f"{j}: {round(percentage,3)}% ({count_c})")
    # appending these results to the output folder to furthur write to a text file
    output_t=f"{j}: {round(percentage,3)}% ({count_c})"
    output.append(output_t)

print("------------------")
output.append("--------------")

## make a list our of the candidates with their total votes
unique_data=[unique_data1,unique_data2,unique_data3]
#print(unique_data)
# finding the maximum vote count
most_vote=max(unique_data[0])
# finding the index of the maximum vote count
most_vote_index=unique_data[0].index(most_vote)
# print the winner
print(f"Winner: {unique_data[2][most_vote_index]}")
print("------------------")
output.append(f"Winner: {unique_data[2][most_vote_index]}")
output.append("--------------")


# export the results to a text file
text_path="./PyPoll/analysis/export.txt"
with open(text_path, 'w') as text_file:
    text_file.write('\n'.join(output))
    