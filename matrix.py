import random

class Matrix():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        for i in range(self.rows):
            self.data.append([])
            for j in range(self.cols):
                self.data[i].append(0)

    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])

        return arr
            
    @staticmethod
    def fromArray(arr):
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.data[i][0] = arr[i]
            
        return m
    
    def add(self, n): 
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n.data[i][j]
        else:          
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n

    @staticmethod
    def subtract(a, b):
        # Retorna uma nova matriz a - b
        result = Matrix(a.rows, a.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
                    
        return result
    
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.uniform(-1, 1)

    @staticmethod        
    def transpose(matrix):
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[j][i] = matrix.data[i][j]

        return result
 
    @staticmethod
    def multiply(a, b):
        # Produto da matriz
        if a.cols != b.rows:
            print("O número de colunas de A deve ser igual ao número de linhas de B.")
            return

        result = Matrix(a.rows, b.cols)
            
        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(a.cols):
                    sum += a.data[i][k] * b.data[k][j]
                        
                result.data[i][j] = sum
                    
        return result
    
    def map(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = func(val)
    @staticmethod         
    def mapIt(matrix, func):
        result = Matrix(matrix.rows, matrix.cols)
        
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                val = matrix.data[i][j]
                result.data[i][j] = func(val)
        return result
    
    def multiplyBy(self, n):
        
        if isinstance(n, Matrix):
            for i in range(n.rows):
                for j in range(n.cols):
                    self.data[i][j] *= n.data[i][j]    
            return       
        
       # Produto escalar
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n
                
    def print(self):
        for i in range(self.rows):
            print("| ", end="")
            for j in range(self.cols):
                print(self.data[i][j], " ", end="")
                
            print("|")
        print()
