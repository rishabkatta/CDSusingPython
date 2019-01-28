'''
@author-name: Rishab Katta
@author-name: Akhil Karrothu
'''
import copy
import turtle

originaldict={}
overlapdividend=0
class Weight:
    '''
    This class is used to get the weight objects
    '''

    __slots__ = 'weight', 'totalweight'

    def __init__(self,value):
        self.weight = value

    def get_weight(self):
        '''
        returns weights
        :return: weight objects
        '''
        return self.weight



class Beam:

    __slots__ = 'totalweight', 'fulcdist', 'hangers', 'name', 'weightfulccombo'

    def __init__(self, name, weightfulccombo):
        self.totalweight=0
        self.hangers = []
        self.fulcdist = None
        self.name = name
        self.weightfulccombo = weightfulccombo


    def total_weight(self):
        '''
        calculates total weight of a beam
        :return:
        '''
        # totalweight=sum(self.weightfulccombo[i])
        totalweight=0
        for i in range(0,len(self.weightfulccombo)):
            if int(self.weightfulccombo[i][1])>0:
                totalweight+=int(self.weightfulccombo[i][1])
            # else:
            #     return
        return totalweight

    def getname(self):
        '''
        returns name of the beam
        :return:
        '''
        return self.name

    def getweightfulccombo(self):
        '''
        returns a combination of weights an positions related
        :return:
        '''
        return self.weightfulccombo

    def draw(self, factor):
        '''
        :pre: (0,0), facing east, down
        :pre: (0,-50), facing east, down
        :param factor: factor by which beam have to be reduced
        :return:
        '''
        turtle.right(90)
        turtle.down()
        turtle.forward(50)
        turtle.left(90)
        for i in range(0,len(self.weightfulccombo)):
            turtle.forward(int(self.weightfulccombo[i][0])*100*factor)
            turtle.right(90)
            turtle.forward(50)
            if(isinstance(self.weightfulccombo[i][1], int)):
                turtle.up()
                turtle.forward(25)
                turtle.down()
                turtle.write(self.weightfulccombo[i][1])
                turtle.up()
                turtle.backward(25)
                turtle.down()
                turtle.backward(50)
                turtle.left(90)
                turtle.backward(int(self.weightfulccombo[i][0]) * 100*factor)
            else:
                turtle.left(90)
                Beam('B1',originaldict.get( self.weightfulccombo[i][1])).draw(factor/overlapdividend)
                turtle.right(90)
                turtle.backward(100)
                turtle.left(90)
                turtle.backward(int(self.weightfulccombo[i][0])*100*factor)


                #self.draw()

def compute_factor_div():
    '''
    Computes the scale by which the beam lengths have to separated by based on number of beams and number of weights hanging
    from each beam
    :return:
    '''
    l= len(originaldict.keys())
    maxim=0
    minvalue=3
    for key, value in originaldict.items():
        if(len(value)>maxim):
            maxim=len(value)

    overlapdiv= minvalue + (l*maxim)/20
    global overlapdividend
    overlapdividend = overlapdiv





def calculate_missing_weights(Dict1):
    '''
    Calculates missing weights
    :param Dict1: dictionary containing beam numbers and weights and positions related
    :return: modified dictionary after missing weights have been added
    '''
    Dict2 = copy.deepcopy(Dict1)

    for key, value in Dict2.items():
        for i in range(0, len(value)):
            if value[i][1] == '-1':
                value[i][1] = 'x'

    for key, value in Dict2.items():
        for i in range(0, len(value)):
            if (value[i][1] == 'x'):
                value[i] = value[i][0] + value[i][1]
            else:
                value[i] = int(value[i][0]) * int(value[i][1])

    sumofweights = 0
    tempweight = 0
    for key, value in Dict2.items():
        sumofweights = 0
        tempweight = 0
        for i in range(0, len(value)):
            if isinstance(value[i], int):
                sumofweights += value[i]
            if (isinstance(value[i], str)):
                tmp = value[i].index('x')
                tempweight = int(value[i][:tmp])
        value.clear()
        if (tempweight != 0):
            xweight = abs(int(sumofweights / tempweight))
            Dict2[key] = int(xweight)
        else:
            Dict2[key] = 0


    for key, value in Dict1.items():
        for i in range(0, len(value)):
            if (value[i][1] == '-1'):
                value[i][1] = Dict2.get(key)

    return Dict1

def check_balanced(Dict1):
    '''
    check if a beam is balanced or not
    :param Dict1: dictionary containing beam numbers and weights and positions related
    :return:
    '''
    Dict2 = copy.deepcopy(Dict1)

    for key,value in Dict2.items():
        sumofweights=0
        for i in range(0,len(value)):
            sumofweights += int(value[i][0])*int(value[i][1])
        if sumofweights==0:
            print(key + " is balanced")

def turtle_init():
    '''
    initializing the turtle screen
    :return:
    '''
    turtle.Screen().setworldcoordinates(-5000, -500, 5000, 500)

def main():
    '''
    used to read files and call beam objects
    :return:
    '''

    file= str(input("Enter a file name"))
    Dict1 ={}
    with open(file, "r") as f:
        for line in f:
            line=line.strip()
            list1 = line.split(" ")
            Dict1[list1[0]] = [[list1[index], list1[index+1]]for index in range(len(list1)) if index%2 !=0 and index <= len(list1) /2 + 3 ]


    global originaldict
    originaldict = copy.deepcopy(Dict1)

    Dict2={}
    for key,value in Dict1.items():
        for i in range(0,len(value)):
            if(value[i][1]=='-1'):
                Dict2[key]=value

    listofbeams = []
    for key, value in Dict1.items():
        beam = Beam(key, value)
        listofbeams.append(beam)

    lobtobecalc = []
    outerloopbreak = False
    for key, value in Dict1.items():
        for i in range(0, len(value)):
            if not isinstance(value[i][1], int):
                if (value[i][1].isdigit()):
                    continue
                else:
                    outerloopbreak = True
        if outerloopbreak:
            break
        else:
            lobtobecalc.append(key)
    lobaftercalc = []
    for beam in listofbeams:
        if beam.getname() in lobtobecalc:
            tw = beam.total_weight()
            lobaftercalc.append(tw)

    for key, value in Dict1.items():
        if key not in lobtobecalc:
            for i in range(0, len(value)):
                if value[i][1] in lobtobecalc:
                    index = lobtobecalc.index(value[i][1])
                    value[i][1] = lobaftercalc[index]
            lobtobecalc.append(key)
            beam = Beam(key, value)
            tw = beam.total_weight()
            lobaftercalc.append(tw)

    check_balanced(Dict1)
    listofbeams.clear()

    Dict3 = calculate_missing_weights(Dict2)

    for key,value in Dict1.items():
        if key in Dict3.keys():
            Dict1[key] = Dict3[key]



    for key,value in originaldict.items():
        for i in range(0,len(value)):
            if(value[i][1]=='-1'):
                originaldict[key]=Dict2[key]

    for key,value in originaldict.items():
        for i in range(0,len(value)):
            value[i][0] = int(value[i][0])
            if not isinstance(value[i][1], int):
                if not (value[i][1].startswith("B")):
                    value[i][0] = int(value[i][0])
                    value[i][1] = int(value[i][1])
    print(originaldict)
    for key,value in originaldict.items():
        beam = Beam(key, value)
        listofbeams.append(beam)

    turtle_init()
    compute_factor_div()
    for beam in listofbeams:
        if(beam.getname()=="B"):
            beam.draw(10)

    turtle.Screen().exitonclick()




if __name__ == '__main__':
    main()
