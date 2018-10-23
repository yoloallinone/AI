from Exception import*
class block(object):
    ''' block model'''
    def __init__(self, on=True):
        '''on refers to the object the block is on. None=Table'''
        self.clear=True
        self.on=on
        print("in block")

    def getOn(self):
        '''returns the obect it's on'''
        return self.on

    def getClear(self):
        '''return wheather it's clear or not'''
        return self.clear

class agent(object):
    '''AI agent'''
    def __init__(self):
        self.empty=True

    def pickUp(self,x):
        '''picks up block x if self.empty'''
        if not self.empty == True:raise NotEmptyException
        self.empty =x
    def drop(self):
        '''drops the block in hand'''
        if not self.empty: raise NotBlockInHandException
        self.empty=True

class blockWorld:
    def __init__(self,blocks=None,agent=agent()):
        self.blocks= blocks
        self.agent=agent
    def isClear(self,X):
        '''return true if X is clear and false if otherwise'''
        if X not in self.blocks: raise BlockNotFoundException
        return X.getClear()
    def addNewBlock(self,X):
        '''appens block to world'''
        if X in self.blocks:return X
        self.blocks.append(X)
        return X
    def newBlock(self,X=None):
        '''creates a new block in world'''
    def on(self,X,Y):
        '''moves X on Y'''
        if not Y in self.blocks:
            self.blocks.append(Y)
        if not X in self.blocks:
            self.blocks.append(X)
#if isClear(Y):
if __name__=="__main__":
    block1=block()
    block2=block(block1)

	
	
	
#################################################### Exception.py#########################################
# copy below code in a new file Exception.py 
class NotEmptyException(Exception):
    def __str__(self):
        "Agent not empty"
class NotBlockInHandException(Exception):
    def __str__(self):
        "Agent empty"
class BlockNotFoundException(Exception):
    def __str__(self):
        "Block not found in world"
