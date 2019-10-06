import math
import random
from matrix import Matrix


def sigmoid(x):                     # Função sigmoid
    return 1 / (1 + math.exp(-x))   #            1
                                    # f(x) = ----------
                                    #        1 + e^(-x)
# Derivada da função sigmoid
def dsigmoid(y):
    return y * (1 - y)

class NeuralNetwork:  
    
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = 0.1
        
        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)        
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    
    def predict(self, input_array):
        # Gerando as saídas intermediárias 
        inputs = Matrix.fromArray(input_array)
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)

        # Função de ativação
        hidden.map(sigmoid)

        # Gerando as saídas de facto
        output = Matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(sigmoid)

        return output.toArray()
    
    def feedfoward(self, input_array):
        # GERANDO OS HIDDEN OUTPUTS (SAIDAS DOS NÓS INTERMEDIÁRIOS)
        
        # Transforma a lista de entrada em um objeto vetor (ou matriz unidimensional, como quiser)
        input = Matrix.fromArray(input_array)
        # Multiplica as entradas pelos respectivos pesos
        hidden = Matrix.multiply(self.weights_ih, input)
        # Adiciona o bias
        hidden.add(self.bias_h)
        # Função de ativação!
        hidden.map(sigmoid)
        
        # GERANDO A SAÍDA
        
        # Multiplica as saidas dos nós intermediários pelos respectivos pesos
        output = Matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(sigmoid)
        
        # Transforma o objeto vetor em uma lista
        return output.toArray() # E manda de volta! hehe ;)

    def train(self, input_array, target_array): # Backpropagation
        # GERANDO OS HIDDEN OUTPUTS (SAIDAS DOS NÓS INTERMEDIÁRIOS)
        
        # Transforma a lista de entrada em um objeto vetor (ou matriz unidimensional, como quiser)
        inputs = Matrix.fromArray(input_array)
        # Multiplica as entradas pelos respectivos pesos
        hidden = Matrix.multiply(self.weights_ih, inputs)
        # Adiciona o bias
        hidden.add(self.bias_h)
        # Função de ativação!
        hidden.map(sigmoid)
        
        # GERANDO A SAÍDA
        
        # Multiplica as saidas dos nós intermediários pelos respectivos pesos
        outputs = Matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)
        
        # Coverte para uma matriz objeto
        targets = Matrix.fromArray(target_array)
        
        
        # Calcula o erro
        # ERRO = ALVOS - SAIDAS
    
        output_errors = Matrix.subtract(targets, outputs)

        # Calcula o gradiente  
        gradients = Matrix.mapIt(outputs, dsigmoid)
        gradients.multiplyBy(output_errors)
        gradients.multiplyBy(self.learning_rate)
        
        # Calcula deltas
        hidden_T = Matrix.transpose(hidden)
        weight_ho_deltas = Matrix.multiply(gradients, hidden_T)

        # Ajusta os pesos pelos deltas
        self.weights_ho.add(weight_ho_deltas)
        # Ajusta os bias pelos seus deltas
        self.bias_o.add(gradients)
        
        # Calcula os erros da camada intermediária        
        who_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.multiply(who_t, output_errors)

        # Calcula o gradiente intermediário
        hidden_gradient = Matrix.mapIt(hidden, dsigmoid)
        hidden_gradient.multiplyBy(hidden_errors)
        hidden_gradient.multiplyBy(self.learning_rate)

        # Calcula o delta intermediário
        inputs_T = Matrix.transpose(inputs)
        weight_ih_deltas = Matrix.multiply(hidden_gradient, inputs_T)
        
        self.weights_ih.add(weight_ih_deltas)
        # Ajusta os bias pelos seus deltas
        self.bias_h.add(hidden_gradient)

    
    def copy(self):
        return self
    
    def mutate(self, rate):
        
        def mutateIt(val):
            if random.random() < rate:
                return val + random.gauss(0, 0.1)
            else:
                return val


        self.weights_ih.map(mutateIt)
        self.weights_ho.map(mutateIt)
        self.bias_h.map(mutateIt)
        self.bias_o.map(mutateIt)







