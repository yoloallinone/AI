# The n queen puzzle

class NQueens:
    """Generate all valid solutions for the n queen puzzle"""
    def  __init__(self, size) :
        #Store the puzzle(problem) size and the number of valid solutions
        self.size = size
        self.solutions = 0
        self.solve( )
        
    def  solve(self) :
        """Solve the n queen puzzle and print the number of solutions"""
        positions=[-1]*self.size
        self.put_queen(positions,0)
        print("Found ",self.solutions," Solutions.")
        
    def  put_queen(self,positions,target_row):
        """"Try to place a queen on the target_row by checking all the N possible cases.
               If a valid place is found the function calls itself trying to place a queen
               on the next row until all N queens are placed on the NxN board"""
     #Base(stop) case-all N rows are occupied
        if (target_row==self.size):
            self.show_full_board(positions)
            self.solutions+=1
        else:
            #For all N colums try to place a queen
            for column in range (self.size):
                #reject all invalid positions
                if (self.check_place(positions,target_row,column)):
                    positions[target_row]=column
                    self.put_queen(positions,target_row+1)
                    
    def check_place(self,positions,occupied_rows,column):
        """Check if a given position is under attack from any of
              the previously placed queens(check column and diagonal postions)"""
        for i in range (occupied_rows):
            if  positions[i] == column or\
                positions[i] - i == column - occupied_rows or\
                positions[i] + i == column + occupied_rows :
               return False
        return True
    def show_full_board(self,positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line=" "
            for column in range(self.size):
                if positions[row]==column:
                    line+="Q "
                else:
                    line+=". "
            print(line)
        print("\n")
def main():
    """Initialise and solve the NQueen puzzle"""
    NQueens(8)
if __name__=="__main__":
    #execute only if run as script
    main()
    
                    
                
