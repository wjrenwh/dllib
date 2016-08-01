import theano
import theano.tensor as T


def relu(x):
    y = T.maximum(0.0, x)
    return(y)

def sigmoid(x):
    y = T.nnet.sigmoid(x)
    return(y)

def tanh(x):
    y = T.tanh(x)
    return(y)d

def iden(x):
    y = x
    return(y)