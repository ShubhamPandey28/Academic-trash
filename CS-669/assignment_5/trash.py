import numpy as np

def predict(x, w, b):
    f = np.dot(w, x)
    if f >= b:
        return 1
    else:
        return 0

def train_perceptron(X, Y, epochs, lr):
    b = 0
    n_features = X.shape[1]
    w = np.zeros((n_features))

    for epoch in range(epochs):
        print(f'iteration: {(epoch+1)}')
        for i in range(len(X)):                      
            y_pred = predict(X[i], w, b)

            for k in range(len(w)):             
                w[k] = w[k] + lr * (Y[i]-y_pred) * X[i][k]
                b = b + lr * (Y[i]-y_pred)
    return (w, b)


def plot_model(weights, bias, start, end):
    y1 = -(weights[0]*start+bias)/weights[1]
    y2 = -(weights[0]*end + bias)/weights[1]
    plt.plot([start, end], [y1, y2], color='black')
