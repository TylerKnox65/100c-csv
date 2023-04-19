#!python3
import csv

"""
Create a function called getData()
getData takes no input parameters
return: file contents as a string

"""
#H:\Documents\GitHub\100c-csv\data.csv
def getData():
    db = []
    searchresult = []
    c = open("data.csv","r")
    data = c.read()
    return data
    li = data.split('\n')
    for li in li:
        line = li.split(",")
        db.append(line)
    '''
    for i in db:
        if '13' in i[1]:
            #print(i)
            searchresult.append(i)
    '''
    return db

def main():
    db = getData()
    #print(db)

    assert ("Placed in Service" in db) == True
    assert ("MAC 6c299551c1b5" in db) == True    
    assert db.find("No.,Equipment Item N") == 0
    assert db.find("Barry") == 27089

if __name__ == "__main__":
    main()

