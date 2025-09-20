
def readSingleDataFile(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            dataText = f.read()
            return(dataText)
            
    except Exception:
        print(f"Error when reading file {fileName}")
        

def writeSingleFile(fileName, fileStr):
    try:
        with open(fileName, 'w+', encoding='utf-8') as f:
            f.write(fileStr)
            
    except Exception:
        print(f"Error when writing to file {fileName}")