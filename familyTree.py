#!/usr/bin/python
#Annie Kirklin

import sys

def isChild(name1, name2):               #checks if name2 is in list of name1 and therefore a child of name1
    if not name1 in familyTree or not name2 in familyTree:    #immediately returns false if one name isn't in the familyTree (in all methods)
        return False
    if name2 not in familyTree.get(name1)[0]:
        return False
    return True

def isSibling(name1, name2):              #checks to see if the 2 names have common members of their parent array and therefore are siblings
    if not name1 in familyTree or not name2 in familyTree:
        return False

    if len(set(familyTree[name1][0]).intersection(familyTree.get(name2)[0])) >= 1:
        return True
    return False

def isSpouse(name1, name2):              #checks to see if name2 is in the spouse array of name1 and therefore are or have at one point been spouses
    if not name1 in familyTree or not name2 in familyTree:
        return False
    if name2 not in familyTree.get(name1)[1]:
        return False
    return True

def isAncestor(name1, name2):            #recursively checks if the 2 names have any common members in their family trees
    if not name1 in familyTree or not name2 in familyTree:
        return False
    if len(familyTree[name2][0]) != 2:
        return False
    name2Parent1 = familyTree.get(name2)[0][0]
    name2Parent2 = familyTree.get(name2)[0][1]
    if name2Parent1 == name1 or name2Parent2 == name1:
        return True
    else:
        return isAncestor(name1, name2Parent1) or isAncestor(name1, name2Parent2)

def isCousin(name1, name2):             #checks to see if name1 and name2 have common ancestors but aren't direct ancestors of each other
    if not name1 in familyTree or not name2 in familyTree:
        return False
    if (name1 == name2):
        return False
    ancList1 = getAncestor(name1)
    ancList2 = getAncestor(name2)
    if name2 in ancList1 or name1 in ancList2:
        return False
    for name in ancList1:
        if name in ancList2:
            return True
    return False

def isUnrelated(name1, name2):           #checks to see if the 2 names have no common ancestors
    if not name1 in familyTree or not name2 in familyTree:
        return True
    if (name1 == name2):
        return True
    ancList1 = getAncestor(name1)
    ancList2 = getAncestor(name2)
    if name1 in ancList2 or name2 in ancList1:
        return False
    for name in ancList1:
        if name in ancList2:
            return False
    return True

def getChild(name):                    #returns a list of all the children of a person
    childList = []
    for i in listOfNames:
        if isChild(i, name) and i != name:
            childList.append(i)
    return childList

def getSiblings(name):                  #returns a list of all the siblings of a person
    siblingList = []
    for i in listOfNames:
        if isSibling(i, name) and i != name:
            siblingList.append(i)
    return siblingList

def getSpouses(name):                 #returns a list of the spouses of a person
    spouseList = []
    for i in listOfNames:
        if isSpouse(i, name) and i != name:
            spouseList.append(i)
    return spouseList

def getAncestor(name):                #returns a list of all a person's ancestors
    ancList = []
    for i in listOfNames:
        if isAncestor(i, name) and i != name:
            ancList.append(i)
    return ancList

def getCousin(name):                  #returns a list of a person's cousins
    cousinsList = []
    for i in listOfNames:
        if isCousin(i, name) and i != name:
            cousinsList.append(i)
    return cousinsList

def getUnrelated(name):              #returns a list of all the people unrelated to the person
    unrelatedList = []
    for i in listOfNames:
        if isUnrelated(i, name):
            unrelatedList.append(i)
    return unrelatedList

if __name__ == "__main__":
    familyTree = dict()   #create dictionary to keep track of family tree
    listOfNames = []


    for line in sys.stdin:
        if line.startswith('E'):      #input lines
            y = line.split()          #splits the input line to obtain the individual names
            for i in range(1,len(y)):   #cycles through the names in the input line
                persons = []
                parents = []
                spouses = []
                persons.append(parents)
                persons.append(spouses)

                if y[i] not in listOfNames:     #process if name has not already been in a previously read line
                    listOfNames.append(y[i])    #add name to list if not already in it
                    if i == 1:
                        familyTree.update({y[i]: persons})   #adds name2 to name1's spouse list
                        spouses.append(y[2])
                    if i == 2:
                        familyTree.update({y[i]: persons})  #adds name1 to name2's spouse list
                        spouses.append(y[1])
                    try:
                        if i == 3:
                            familyTree.update({y[i]: persons})   #if a thrid name is listed it is a child of name1 & name2
                            parents.append(y[1])                 #add name1 and name2 to the parent list of name3
                            parents.append(y[2])
                    except IndexError as e:
                        pass
                else:                       #process if name has been in a previously read line
                    if i == 1:
                        if y[2] not in familyTree.get(y[i])[1]:
                            familyTree.get(y[i])[1].append(y[2])
                    if i == 2:
                        if y[1] not in familyTree.get(y[i])[1]:
                            familyTree.get(y[i])[1].append(y[1])
                    try:
                        if i == 3:
                            if y[1] not in familyTree.get(y[i])[0]:
                                familyTree.get(y[i])[0].append(y[1])
                            if y[2] not in familyTree[y[i]][0]:
                                familyTree.get(y[i])[0].append(y[2])
                    except IndexError as e:
                        pass
        elif line.startswith('X'):       #IS-A query lines
            relation = line.split()[2]   #assigns the second word in the query line, which is always the relationship in question, to relation
            name1 = line.split()[1]
            name2 = line.split()[3]
            print("X {} {} {}".format(name1, relation, name2))

            if relation == 'child':
                result = ischild(name1, name2)
            elif relation == 'sibling':
                result = isSibling(name1,name2)
            elif relation == 'spouse':
                result = isSpouse(name1, name2)
            elif relation == 'ancestor':
                result = isAncestor(name1, name2)
            elif relation == 'cousin':
                result = isCousin(name1, name2)
            elif relation == 'unrelated':
                result = isUnrelated(name1, name2)
            if result :
                print("Yes")
            else:
                print("No")
            print
        elif line.startswith('W'):    #WHO-IS-A query lines
            line = line.split()
            relation = line[1]
            name = line[2]
            printList = []

            print("W {} {}".format(relation, name))
            if name in familyTree:
                if relation == 'child':
                    printList = getChild(name)
                elif relation == 'sibling':
                    printList = getSiblings(name)
                elif relation == 'spouse':
                    printList = getSpouses(name)
                elif relation == 'ancestor':
                    printList = getAncestor(name)
                elif relation == 'cousin':
                    printList = getCousin(name)
                elif relation == 'unrelated':
                    printList = getUnrelated(name)
                printList.sort()
                for i in printList:
                    print(i)
                print("")
