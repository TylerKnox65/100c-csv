#!python3

"""
Create a function called getData()
getData takes no input parameters
return: file contents as a list of lists

"""
def getData():
    '''
    Function will read data.csv
    split the file into a list, with 1 line per element
    then, split each element into a list using "," as the delimiter
    you should return a list of lists
    

    '''
    db = []
    c = open("data.csv","r")
    data = c.read()
    li = data.split('\n')
    for li in li:
        line = li.split(",")
        db.append(line)
    
    return db

def main():
    data = getData()
    assert len(data) == 148
    assert len(data[0]) == 18
    assert data[1] == ['1', '134662', 'Acer Chromebook 3205U-1.5GHz 4GB 16GB-SSD MAC 6c29953e18f9', 'West Delta Middle School', '', 'NXEF2AA0055080800D7600', '', 'ACER', '', 'CBC- E-5', '', '', 'Microserve', '22-06-2016', '"-1', '678"', '', '', 'CHROMEBOOK CART']
    assert data[1][1] == '134662'

if __name__ == "__main__":
    main()