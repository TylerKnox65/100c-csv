#!python3
from x103b import getData
"""
You will need to search through the document and find information that is being searched for by the user.
Search for the Equipment Item Number
show the Serial Number

If there are multiple matches, return a list of the serial numbers

Method 1:
Search the entire file, line by line to see if your search string (the needle) is located on the line.
Add the line to a list for later analysis.

For each item in your list, display the relevant information for the line.

"""

def findSerial(needle):
    """
    input: 
    str needle: This is the string to look for
    
    return:
    str: Serial number if there is only 1match
    list: list of str serial numbers if there are multiple matches
    None if no matches
    """
    filename = "data.csv"
    data = getData()
    ls = []
    for i in data:
        x = i[1]
        y = i[5]
        if needle in x:
            ls.append(y)
    #print(ls)
    length = len(ls)
    if length == 0:
        return None
    else:
        ls = ", ".join( repr(e) for e in ls )
        ls = ls.replace("'","")
        return ls

def main():
    findSerial("141769")
    assert findSerial("141769") == "4MLLN73"
    assert findSerial("141") == ['NXEF2AA005608103CA7600', 'BMNWN13', '4MLLN73']
    assert findSerial("134432") == None

if __name__ == "__main__":
    main()
        

