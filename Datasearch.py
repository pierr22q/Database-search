#Qiana Pierre Assignment 5 09/29/2020
#Description: This program mimics a database search. It will use two sets of integer values, one representing a database
# and the other representing values that will be searched for
# Attribution for any sources: Ruth, GeeksforGeeks

import sys

def sortArray(list):
    ''' Selection Sort
        returns a list '''
    for i in range(len(list)):
      min_value = min(list[i:])  # [i:] so that it looks post the ordered elements until end
      minIndex = list.index(min_value)
      move_this = list[i]
      list[minIndex] = move_this
      list[i] = min_value
    return list


def binary_search_rec(a_list, item):
    '''a recursive binary search function. For each value in seek, search through the data to
    determine if it’s present or not. Return Boolean '''
    if len(a_list) == 0:
	        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)

def copySeekToList(line):
    '''reads/copy in seek values into a list
       returns list'''
    seekValues = []
    seekValues = line.split()
    # changes string in list to int
    for i in range(0, len(seekValues)):
        seekValues[i] = int(seekValues[i])

    return seekValues

def copyDataToList(line):
    '''reads/copy in data values into a list
    returns list'''
    dataValues = []
    dataValues = line.split()
    # changes string in list to int
    for i in range(0, len(dataValues)):
        dataValues[i] = int(dataValues[i])

    dataValues = sortArray(dataValues) # sorts list
    return dataValues

def searchForSeek(seekList,dataList):
    '''  searches for seek values in dataList
    if seek[i] is found, then found[i] should be set to 1
    otherwise set found[i] to 0'''
    foundValues = [ ]
    for i in seekList:
        if binary_search_rec(dataList,i) == True:
            foundValues.append(1)
        else:
            foundValues.append(0)
    return foundValues


def main ():
  filename = sys.argv[1]# get the input file name
  fi = open(filename, "r") # open file in read mode
  line = fi.readline()
  while line != '': # EOF char is an empty string
  # do all the processing of the line that was read
        seekList= copySeekToList(line) # print everything except \n
      # get the next line
        line = fi.readline()
  fi.close() # close the file after it’s all been read main()

  filename = sys.argv[2]# get the input file name
  fi = open(filename, "r") # open file in read mode
  line = fi.readline()
  while line != '': # EOF char is an empty string
  # do all the processing of the line that was read
        dataList = copyDataToList(line) # print everything except \n
      # get the next line
        line = fi.readline()
  fi.close() # close the file after it’s all been read main()

  foundList = searchForSeek(seekList,dataList)
  fo = open("output.txt​ t",'w')

  for i in range(len(seekList)):
      if foundList[i] == 0:
          fo.write(str(seekList[i]) + ":" + "No" + "\n")
      else:
          fo.write(str(seekList[i]) + ":" + "Yes" + "\n")
  fo.close()
main()
