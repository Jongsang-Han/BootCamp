import numpy as np

xy = np.array([[1.,2.,3.,4.,5.,6.],
               [3.,6.,9.,12.,15.,18.]])

x_train = xy[0,]
y_train = xy[1,]

beta_gd = np.random.uniform(low=-1.0, high=1.0, size=(1))
bias = np.random.uniform(low=-1.0, high=1.0, size=(1))

learning_rate = 0.01

for i in range(1000):
    y_hat = x_train * beta_gd + bias

    error = ((y_hat - y_train)**2).mean()

    beta_gd = beta_gd - learning_rate * ((y_hat - y_train) * x_train).mean()
    bias = bias - learning_rate * (y_hat - y_train).mean()

    if i % 100 == 0:
        print('Epoch ({:10d}/1000) error: {:10f}, beta_gd: {:10f}, bias:{:10f}'.format(i, error, beta_gd.item(), bias.item()))
