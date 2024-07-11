#This program reads salesperson data from file and show output based on sales for each person
def main():
#Declaring variables and initialize
    salesData = []
    average = []
    strippedAverage = []
    nameList = []
    salesPercentage = 0.00
    totalMonths = 0
    name = ""
    inFile1 = ""
    inFile2 = ""
    outFile = ""

    inFile1 = open('salesperson.txt', 'r')
    for line in inFile1:
        #Split each line by space and remove any empty strings
        data = line.strip().split()
        for i in range(1, len(data)):
            data[i] = int(data[i])
        #Append to salesData list
        salesData.append(data)

    #Read average sales data from file
    inFile2 = open("average.txt", "r")
    average = inFile2.readlines()
    for item in average:
        #Strip the new line
        strippedAverage.append(int(item.rstrip('\n')))
        
    outFile = open("output.txt", "w")
    
    WriteHeadings(outFile) #Call function for headings
    for item in salesData:
        nameList = item[0].split(",")
        name = nameList[1] + " " + nameList[0]
        totalMonths = len(salesData[1:])
        aboveAverageCount = 0
        
        #Iterate over sales figures and compare with average
        for i in range(1, len(item)):
            if item[i] > strippedAverage[i - 1]:
                aboveAverageCount += 1
        
        salesPercentage = aboveAverageCount / len(data[1:]) * 100
        salesLevels = CalculateSalesLevels(salesPercentage) #Call function to get sales levels      

        #Write the results of the precessing to output file
        outFile.write('\t\t{0:8s}{1:<13s}{2:4s}{3:<7s}{4:5s}{5:<6.1%}{6:6s}{7:<8s}\n'.format("", name, "", f"{aboveAverageCount} of {totalMonths}", "", salesPercentage/100, "", salesLevels))
       

def CalculateSalesLevels(salesPercentage):
#This function is used to get sales level based on the sales percentage
    if salesPercentage < 60:
        return "ONE"
    elif salesPercentage < 75:
        return "TWO"
    elif salesPercentage < 90:
        return "THREE"
    elif salesPercentage == 100:
        return "FOUR"

        
def WriteHeadings(outFile):
#This function is used to write the headings to file
    outFile.write("\t\t\t\t-------------------------")
    outFile.write("\n\t\t\t\t    MONTHLY SALES DATA")
    outFile.write("\n\t\t\t\t-------------------------")
    outFile.write("\n\t\t{0:8s}{1:13}{2:3s}{3:8s}{4:4s}{5:8s}{6:5s}{7:8s}".format("", "", "", "Month's", "", "Percent", "", ""))
    outFile.write("\n\t\t{0:8s}{1:13s}{2:3s}{3:8s}{4:4s}{5:8s}{6:5s}{7:8s}".format("", "", "", " Above", "", " Above", "", ""))
    outFile.write("\n\t\t{0:8s}{1:13s}{2:3s}{3:8s}{4:4s}{5:8s}{6:5s}{7:8s}".format("", "SalesPerson", "", "Average", "", "Average", "", "Level"))
    outFile.write("\n\t\t{0:8s}{1:13s}{2:3s}{3:8s}{4:4s}{5:8s}{6:5s}{7:8s}\n".format("", "-------------", "", "--------", "", "--------", "", "-----"))


main()
