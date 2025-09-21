from os import listdir, path, makedirs, walk

from cleanData import removeHeaders, removeSpeakerTag, removeUtternaceInfo,  removeSpecialChar, removeRepeats, replaceSpeNegConstruction, replaceRegNegConstruction, replaceIsConstruction, replaceOtherConstruction
from readFile import readSingleDataFile, writeSingleFile
from config import PROJECT_ROOT_PATH

def preprocessData(dataDirPath):
    createDirFile(dataDirPath, path.join(PROJECT_ROOT_PATH, "clean"))
    
    # read each .cha files
    for dirPath, _, fileNames in walk(dataDirPath):
        if any('.cha' in fileName for fileName in fileNames):
            for fileName in fileNames:
                # remove extraneous information
                if '.cha' in fileName:
                    fileTxt = readSingleDataFile(path.join(dirPath, fileName))
                    if fileTxt:
                        fileTxt = removeHeaders(fileTxt)
                        fileTxt = removeUtternaceInfo(fileTxt)
                        fileTxt = removeSpeakerTag(fileTxt)
                        fileTxt = removeSpecialChar(fileTxt)
                        #fileTxt = replaceConstraction(fileTxt)
                        fileTxt = removeRepeats(fileTxt)
                        fileTxt = replaceIsConstruction(fileTxt)
                        fileTxt = replaceSpeNegConstruction(fileTxt)
                        fileTxt = replaceRegNegConstruction(fileTxt)
                        fileTxt = replaceOtherConstruction(fileTxt)

                    else:
                        print(f"fileTxt is empty for file {path.join(dirPath, fileName)}!")
                
                newDataPath = path.join(dirPath, fileName).replace('data', 'clean', 1)
                writeSingleFile(newDataPath, fileTxt)
                

def createDirFile(rootSrcPath, rootTarPath):
    makedirs(rootTarPath, exist_ok=True)
    
    for item in listdir(rootSrcPath):
        # we reach the bottom when we see the cha files, abort the directory creation
        if path.isfile(path.join(rootSrcPath, item)):
            if '.cha' in item:
                return
        else:
            createDirFile(rootSrcPath + '/' + item, rootTarPath + '/' + item)

