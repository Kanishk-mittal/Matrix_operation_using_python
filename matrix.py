class square_matrix:
    def __init__(self):
        self.__matrix=[[]]
    
    def get_matrix_from_user(self):
        r1=list(eval(input("Enter the numbers of row 1 seprated by comma:- ")))
        self.__matrix[0]=r1
        for i in range(1,len(r1)):
            r=list(eval(input(f"Enter the numbers of row {i+1} seprated by comma:- ")))
            self.__matrix.append(r)

    def set_matrix(self,nested_list):
        self.__matrix=nested_list

    def print_matrix(self):
        for i in self.__matrix:
            print(i)

    def add(self , matrix2):
        if len(self.__matrix)==len(matrix2.__matrix):
            m3=list()
            for i in range(len(self.__matrix)):
                m3.append(list())
                for j in range(len(self.__matrix[0])):
                    m3[i].append(self.__matrix[i][j]+matrix2.__matrix[i][j])
            m4=square_matrix()
            m4.set_matrix(m3)
            return m4
        else:
            return[[]]
        
    def subtract(self , matrix2):
        if len(self.__matrix)==len(matrix2.__matrix):
            m3=list()
            for i in range(len(self.__matrix)):
                m3.append(list())
                for j in range(len(self.__matrix[0])):
                    m3[i].append(self.__matrix[i][j]-matrix2.matrix[i][j])
            m4=square_matrix()
            m4.set_matrix(m3)
            return m4
        else:
            return[[]]
        
    def multiply(self , matrix2):
        if len(self.__matrix)==len(matrix2.__matrix):
            m3=list()
            for i in range(len(self.__matrix)):
                m3.append(list())
                for j in range(len(self.__matrix[0])):
                    num=0
                    for k in range(len(self.__matrix[0])):
                        num+=self.__matrix[i][k]*matrix2.__matrix[k][j]
                    m3[i].append(num)
            m4=square_matrix()
            m4.set_matrix(m3)
            return m4
        else:
            return[[]]
        
    def __get_slice(self,array, row, col):
        result = []
        for i in range(len(array)):
            if i != row:
                new_row = []
                for j in range(len(array[i])):
                    if j != col:
                        new_row.append(array[i][j])
                if len(new_row)>0:
                    result.append(new_row)
        return result

    def __det_array(self, array):
        if len(array[0]) == 2:
            value = array[0][0] * array[1][1] - array[0][1] * array[1][0]
            return value
        else:
            value=0
            for i in range(len(array[0])):
                value += ((-1) ** i )* array[0][i] * self.__det_array(self.__get_slice(array,0, i))
            return value

    def det(self):
        return self.__det_array(self.__matrix)
    def transpose(self):
        transposed_matrix = [[0 for _ in range(len(self.__matrix))] for _ in range(len(self.__matrix))]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix)):
                transposed_matrix[i][j] = self.__matrix[j][i]
        result_matrix = square_matrix()
        result_matrix.set_matrix(transposed_matrix)
        return result_matrix
    def cofactor(self):
        cofacotr_matrix = [[0 for _ in range(len(self.__matrix))] for _ in range(len(self.__matrix))]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix)):
                if((i+j+2)%2==0):
                    cofacotr_matrix[i][j] = (self.__det_array(self.__get_slice(self.__matrix,i,j)))
                else:
                    cofacotr_matrix[i][j] = (-1)*(self.__det_array(self.__get_slice(self.__matrix,i,j)))
        result_matrix = square_matrix()
        result_matrix.set_matrix(cofacotr_matrix)
        return result_matrix
    def inverse(self):
        if (self.det()==0):
            return None
        else:
            determinant=self.det()
            cofacotr_matrix=self.cofactor()
            cofacotr_matrix=cofacotr_matrix.transpose()
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix)):
                    cofacotr_matrix.__matrix[i][j] = (cofacotr_matrix.__matrix[i][j])/determinant
            return cofacotr_matrix