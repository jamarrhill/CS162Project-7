# Name: Jamar Hill
# Date: 5/17/2021
# Description: CS 162 Project 7

class node:

    def __init__(self, data, next=None):  # next is BY DEFAULT none
        self.__data = data
        self.__next = next


#  cur_node = node(5)
#  node(9, cur_node) # 9 -> 5


class linkedlist:

    def __init__(self):# Initiates the linked list class as itself.
        self.__head = None #Set the value of the variable "__head to None

    def getHead(self): # returns the whats is defined as the head of a linked list.
        return self.__head

    # Iterative approach
    # add(node(7))
    # current_node = self.head
    # while (current_node.next != None):
    #     current_node = current_node.next
    # current_node.next = node(7)

    #   5 -> 6 -> 2 -> 1 -> 10 -> None
    def recursiveLink(self, a_node, val): # Adds a recurrsion step to the end of a list.
        #This step is called a_node. A_node has a value.
        if a_node.__next is None: #a_node.next calls to move to the next node in a linked list.
            #If there is not another node ("None")
            a_node.__next = node(val) #a_node next is equal to the nodes value
        else:
            self.recursiveLink(a_node.__next, val) #Else add recursively by linking to the current list.

    def add(self, val): # Creates a method for starting a list of adding to a list
        if self.__head is None:  # If there is no head node, then linked list is empty
            self.__head = node(val) #establish head of list
        else:
            self.recursiveLink(self.__head, val) #else recursivley add to list.

    def rec_display(self, a_node): #Displays Method
        if a_node is None:
            return

        print(a_node.__data, end=" ")
        self.rec_display(a_node.__next) #Returns end of list

    # remove(self.head, 2)
    #   5 -> 6 -> 2 -> 1 -> 10 -> None
    # node 2's next is 1
    # Update node 6's next to be node 2's next
    def remove(self, a_node, val): #Removes Node
        if (self.__head.__data == val):
            self.__head = self.__head.__next
            return

        if (a_node.__next == None):
            return

        # Removing of the node
        elif (a_node.__next.__data == val):
            a_node.__next = a_node.__next.__next
            return #next.next skips over the identifed value in the linked list
        #this action consequently removes the value.

        else:
            self.remove(a_node.__next, val) #Else node does not have a value
            #In this case we will be removing the last node in the linkedlist.

    # contains(self.head, 1)
    #   5 -> 6 -> 2 -> 1 -> 10 -> None
    def contains(self, a_node, val): #Chacking to see if the node contains a value
        if (a_node.__data == val):
            return True

        if a_node.__next is None:
            return False

        return self.contains(a_node.__next, val) #Will return None value

    # insert(self.head, index=8, value=4, 0)
    #   5 -> 6 -> 2 -> 1 -> 10 -> None
    #
    # Recursive function to insert a node at the respective index
    # The only difference from add(): choose the respective index to add to
    def insert(self, a_node, sort, val, pos):
        if (sort == 0):  # Insert at the head node position
            self.__head = node(val, self.head)
            return

        elif a_node.__next is None:  # If we're at the last node, then add to end of linked list
            a_node.__next = node(val)
            return

        elif (sort == pos + 1):  # When counter == the index position
            new_node = node(val)
            new_node.__next = a_node.__next
            a_node.__next = new_node
            return
        else:
            self.insert(a_node.__next, sort, val, pos + 1)

    #  start: 5 -> 6 -> 2
    #  end:   5 <- 6 <- 2

    # rev(5) -> self.head = ?
    #     rev(6) -> vaeriable_node = ?
    #         rev(2) ->
    def __rev(self, a_node):
        if (a_node == None or a_node.__next == None):
            return a_node #Return value of a_node

        variable_node = self.__rev(a_node.__next)#Create temporty node variable
        a_node.__next.__next = a_node
        a_node.__next = None
        return variable_node #Returns link form list

    def reverse(self):#Establishes the last node (.next ==None) as head.
        self.__head = self.__rev(self.__head)

    # 5 -> 6 -> 7 -> 8
    def _to_plain_list(self, a_node):
        if (a_node.__next != None):
            plainList = self._to_plain_list(a_node.__next) #Computer moves to the next value

        elif (a_node.next == None):
            return [a_node.__data] #Returns the data from the last value in the list

        x = [] #Indexes a single value
        x.append(a_node.__data) #appends to a list
        x = x.__add__(plainList) #adds two lists together
        return x #returns the next value in the list