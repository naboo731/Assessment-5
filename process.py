log_file = open("um-server-01.txt")
# This line opens the file and saves it to the variable 'log_file'


def sales_reports(log_file):
    # line 5: this declares a function called 'sales_reports' that passes in the variable 'log_file'
    for line in log_file:
        # line 7: this begins a for loop to read through each iteration 'line' in 'log_file'
        line = line.rstrip()
        # line 9: this line ammends the line variable using the rstrip method which will removes trailing characters.
        day = line[0:3]
        # line 11: this line declares the variable 'day'. line[0:3] dennotes that the day variable will equal the slicing of lines from 0 to 3. 0 is the starting line, : notes slicing, and 3 is the ending line.
        if day == "Mon":
            # if day == "Tue":
            # line 14: this is a conditional where if the day variable is equal to "Tues", a resoltant action will occur (in this case, it is a print method on line 15).
            print(line)
            # line 15: a print method that will print the value of the line variable.


sales_reports(log_file)
# line 19: this invokes the sales_report function passing in the log_file variable that opens the txt document.
