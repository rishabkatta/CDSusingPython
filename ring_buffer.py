'''
@author-name: Rishab Katta
'''


class Node:

    __slots__ = "value", "link"

    def __init__( self, value, link = None ):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link

    def __str__( self ):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str( self.value )

    def __repr__( self ):
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "Node(" + repr( self.value ) + "," + \
               repr( self.link ) + ")"


class RingBuffer:

    __slots__ = "maxsize", "sizer", "head", "tail"

    def __init__(self,msize):
        '''
        Initialize all the instance variables of Ring Buffer
        :param msize: Max Size of the Ring buffer
        '''
        self.sizer = 0
        self.maxsize = msize
        self.head=None
        self.tail=None

    def insert_keep_new(self,data):
        '''
        Insert elements in such a way to preserve the newest added elements
        :param data: Value to be added
        :return:
        '''
        tmp = Node(data)
        if self.head==None:
            self.head=tmp
            self.tail=tmp
            self.tail.link = self.head
            self.sizer +=1
        else:
            if not self.is_full():
                self.tail.link=tmp
                self.tail=self.tail.link
                self.tail.link=self.head
                self.sizer += 1
            else:
                self.head=self.head.link
                self.tail.link=tmp
                self.tail=self.tail.link
                self.tail.link=self.head
                # self.size += 1

    def insert_keep_old(self,data):
        '''
        Insert elements in such a way that oldest elements are to be preserved
        :param data: Value to be added to the Ring Buffer
        :return:
        '''
        tmp = Node(data)
        if self.head == None:
            self.head = tmp
            self.tail = tmp
            self.tail.link = self.head
            self.sizer += 1
        else:
            if not self.is_full():
                self.tail.link = tmp
                self.tail = self.tail.link
                self.tail.link = self.head
                self.sizer += 1
            else:
                pass #asked and confirmed with Prof Passino.


                # cur = self.head
                # while (True):
                #     if cur.link is self.tail:
                #         break
                #     cur=cur.link
                # cur.link = tmp
                # self.tail=tmp
                # self.tail.link=self.head


    def __str__(self):
        '''
        Return a String Representation of all the elements in the Ring Buffer
        :return: String of all the elements in the Ring buffer
        '''
        str_ring = ""
        if self.head is None:
            return str_ring + ""
        else:
            cur = self.head
            while cur.link is not self.head:
                str_ring +=str(cur.value) + " "
                cur = cur.link
            return str_ring + str(cur.value)

    def find(self,value):
        '''
        Find if the value is present in the Ring Buffer or not
        :param value: Value to be searched for
        :return: Cursor at which the Value is present.
        '''
        cur = self.head
        if cur is None:
            return -1
        if cur.link == self.head:
            if cur.value == value:
                return cur
            else:
                return -1
        while True:
            if cur.value == value:
                return cur
            elif(cur.link is self.head):
                break
            cur = cur.link
        return -1

    def get(self, index):
        '''
        I wrote this function to get the element at the specified position in the Ring Buffer
        :param index: Index position of the element
        :return: element at the index specified
        '''
        cur =self.head
        if(index>self.size()):
            return -1
        if self.size()>0:
            for i in range(0,index):
                cur = cur.link
            return cur.value

    def capacity(self):
        '''
        return max size of the Ring Buffer
        :return: max size of ring buffer
        '''
        return self.maxsize

    def size(self):
        '''
        function returns current size of the ring buffer
        :return: current size of the ring buffer
        '''
        return self.sizer

    def is_full(self):
        '''
        checks to see if the buffer is filled upto capacity or not
        :return:
        '''
        if self.sizer == self.maxsize:
            return True
        return False

    def replace(self, cursor, val):
        '''
        replace the value in the ring buffer with the value in the cursor
        :param cursor: Cursor containing the value to be replaced with
        :param val: value in the Ring buffer
        :return:
        '''
        cur = self.find(val)
        if cur ==-1:
            print("cursor with that value not found")
            return
        cur.value = cursor.value

    def remove_oldest(self):
        '''
        Remove oldest value in the ring buffer
        :return:
        '''
        if self.size() >1:
            self.head = self.head.link
            self.tail.link = self.head
            self.sizer =self.sizer-1
            return
        if self.size() ==1:
            self.head = None
            self.tail =None
            self.sizer=0
            return

    def remove_newest(self):
        '''
        remove newest value in the ring Buffer
        :return:
        '''
        if self.size()>1:
            cur =self.head
            while True:
                if cur.link is self.tail:
                    break
                cur = cur.link
            self.tail =cur
            self.tail.link = self.head
            self.sizer = self.sizer - 1
            return
        if self.size()==1:
            self.head = None
            self.tail = None
            self.sizer=0
            return


def test():
    '''
    Test various functionalities of the Ring Buffer like Insert_keep_new, Insert_keep_old,
    Remove_oldest, Remove_newest, find, Is_full etc.
    :return:
    '''
    rb = RingBuffer(3)

    rb.insert_keep_new(1)
    rb.insert_keep_new(2)
    rb.insert_keep_old(3)
    print(rb)
    rb.remove_newest()
    rb.remove_oldest()
    print(rb)
    print(rb.is_full())
    rb.insert_keep_new(4)
    rb.insert_keep_new(5)
    rb.insert_keep_old(6)
    print(rb)
    rb.remove_newest()
    rb.remove_oldest()
    print(rb)
    rb.insert_keep_new(7)
    rb.insert_keep_new(8)
    rb.insert_keep_old(9)
    rb.insert_keep_new(10)
    rb.insert_keep_new(11)
    rb.insert_keep_old(12)
    print(rb)
    rb.remove_newest()
    rb.remove_oldest()
    print(rb)
    rb.insert_keep_new(20)
    rb.insert_keep_new(25)
    print(rb.is_full())
    print("Searching for 5")
    rb.replace(Node(5),2)
    print(rb)


if __name__ == '__main__':
    test()




