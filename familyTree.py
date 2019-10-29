#!/usr/bin/python
#Annie Kirklin

import sys

def isChild(name1, name2):
    if not name1 in familyTree or not name2 in familyTree:
        return False
    if name2 not in familyTree.get(name1)[0]:
        return False
    return True

def isSibling(name1, name2):
    if not name1 in familyTree or not name2 in familyTree:
        return False

    if len(set(familyTree[name1][0]).intersection(familyTree.get(name2)[0])) >= 1:
        return True
    return False

def isSpouse(name1, name2):
    if not name1 in familyTree or not name2 in familyTree:
        return False
    if name2 not in familyTree.get(name1)[1]:
        return False
    return True

def isAncestor(name1, name2):
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

def isCousin(name1, name2):
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

def isUnrelated(name1, name2):
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

def getChild(name):
    childList = []
    for i in listOfNames:
        if isChild(i, name) and i != name:
            childList.append(i)
    return childList

def getSiblings(name):
    siblingList = []
    for i in listOfNames:
        if isSibling(i, name) and i != name:
            siblingList.append(i)
    return siblingList

def getSpouses(name):
    spouseList = []
    for i in listOfNames:
        if isSpouse(i, name) and i != name:
            spouseList.append(i)
    return spouseList

def getAncestor(name):
    ancList = []
    for i in listOfNames:
        if isAncestor(i, name) and i != name:
            ancList.append(i)
    return ancList

def getCousin(name):
    cousinsList = []
    for i in listOfNames:
        if isCousin(i, name) and i != name:
            cousinsList.append(i)
    return cousinsList

def getUnrelated(name):
    unrelatedList = []
    for i in listOfNames:
        if isUnrelated(i, name):
            unrelatedList.append(i)
    return unrelatedList

if __name__ == "__main__":
    familyTree = dict()
    listOfNames = []


    for line in sys.stdin:
        if line.startswith('E'):
            y = line.split()
            for i in range(1,len(y)):
                persons = []
                parents = []
                spouses = []
                persons.append(parents)
                persons.append(spouses)

                if y[i] not in listOfNames:
                    listOfNames.append(y[i])
                    if i == 1:
                        familyTree.update({y[i]: persons})
                        spouses.append(y[2])
                    if i == 2:
                        familyTree.update({y[i]: persons})
                        spouses.append(y[1])
                    try:
                        if i == 3:
                            familyTree.update({y[i]: persons})
                            parents.append(y[1])
                            parents.append(y[2])
                    except IndexError as e:
                        pass
                else:
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
        elif line.startswith('X'):
            relation = line.split()[2]
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
        elif line.startswith('W'):
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
