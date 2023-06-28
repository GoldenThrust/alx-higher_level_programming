#!/usr/bin/python3
""" classes for a singly-linked list(Node) """


class Node:
    """Node for a singly linked list"""

    def __init__(self, data, next_node=None):
        """ Initialize Node
        Args:
            data (int): Node data
            next_node (Node): next node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Node getter """
        return self.__data

    @data.setter
    def data(self, value):
        """ Node Setter """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ next_node getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node setter """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly Linked list """

    def __init__(self):
        """ Initalize SinglyLinkedList """
        self.__head = None

    def sorted_insert(self, value):
        """ insert Node in sorted order """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

    def __str__(self):
        """ string representation of a SinglyLinkedList """
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)
