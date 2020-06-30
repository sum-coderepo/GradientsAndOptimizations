# dataset
y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
x = [10.0, 8.00, 13.0, 9.00, 11.0, 14.0, 6.00, 4.00, 12.00, 7.00, 5.00]

def computeError(m, b):
    # initialize total error
    error_m_b = 0.0

    # loop within the dataset
    for i in range(len(x)):
        x_i = x[i]
        y_i = y[i]

        # compute the error for a single point
        # and add it to the total error
        error_m_b += (y_i - (m * x_i + b)) ** 2
    # end of for loop

    # compute the mean of the error for all dataset
    error_m_b = error_m_b / float(len(x))
    return error_m_b
# end of def computeError

# compute error for the line corresponded by given m and b values
print("total error:", computeError(0.9, 0.1))


# definition of the function to compute the gradient of m.
def gradientM(m, b):
    # setting default value of gradient
    gradient_m = 0.0

    # loop within the dataset
    for i in range(len(x)):
        x_i = x[i]
        y_i = y[i]

        # compute the first derivative of the error funtion
        # with respect to m
        gradient_m += -x_i * (y_i - (m * x_i + b))
    # end of for loop

    # mean of total error
    gradient_m = 2 * gradient_m / float(len(x))
    return gradient_m
# end of def gradientM


# definition of the function to compute the gradient of b.
def gradientB(m, b):
    # setting default value of gradient
    gradient_b = 0.0

    # loop within the dataset
    for i in range(len(x)):
        x_i = x[i]
        y_i = y[i]

        # compute the first derivative of the error funtion
        # with respect to b
        gradient_b += -(y_i - (m * x_i + b))
    # end of for loop

    # mean of total error
    gradient_b = 2 * gradient_b / float(len(x))
    return gradient_b
# end of def gradientB

print("gradient_m: ", gradientM(1, 0))
print("gradient_b: ", gradientB(1, 0))



def gradientStep(eta, m, b):
    # compute the derivate with respect to m and b
    dM = gradientM(m, b)
    dB = gradientB(m, b)

    # compute new value of m and b
    m = m - eta * dM
    b = b - eta * dB

    return m, b
# end of def gradientStep

# iteration count
N = 101

# learning rate
eta = 0.01

# initial values
m = b = 0

# Let's start iterating
for i in range(N):
    if i % 10 == 0:
        print(i, "\t error:", computeError(m, b))
    m, b = gradientStep(eta, m, b)
# end of for loop


#   # python library for plotting
#   import matplotlib.pylab as plt
#
#   # iteration count
#   N = 100
#
#   # learning rate
#   eta = 0.01
#
#   # initial values
#   m = b = 0
#
#   # lists to keep y-values of line
#   line = []
#
#   # Let's start iterating
#   for i in range(N):
#       m, b = gradientStep(eta, m, b)
#   # end of for loop
#
#   for i in range(len(x)):
#       line.append(m * x[i] + b)
#   # end of for loop
#
#   print("Parameters of the fittest line:")
#   print("m:", m)
#   print("b:", b)
#
#   # drawing of graph.
#   plt.title("Fittest Line")
#   plt.plot(x, y, "go")
#   plt.plot(x, line)
#   plt.show()
#
#
#   # python library for plotting
#   import matplotlib.pylab as plt
#
#   # iteration count
#   N = 30
#
#   # learning rate
#   eta = 0.01
#
#   # initial values
#   m = b = 0
#
#   # lists to keep the error and the iteration values.
#   errors = []
#   Ns = []
#
#   # Let's start iterating
#   for i in range(N):
#       errors.append(computeError(m, b))
#       Ns.append(i)
#       m, b = gradientStep(eta, m, b)
#   # end of for loop
#
#   # drawing of graph.
#   plt.title("Error distribution for %s iteration" % N)
#   plt.ylabel("Error")
#   plt.xlabel("Iteration")
#   plt.plot(Ns, errors)
#   plt.show()


import matplotlib.pylab as plt
def momentumM(m, b, p_m, beta):
    gradient_m = gradientM(m, b)
    momentum_m = gradient_m + beta * p_m
    return momentum_m
# end of def momentumM

def momentumB(m, b, p_b, beta):
    gradient_b = gradientB(m, b)
    momentum_b = gradient_b + beta * p_b
    return momentum_b
# end of def momentumB

def gradientStepWithMomentum(alpha, m, b, p_m0, p_b0, beta):
    # compute the momentum values of m and b
    p_m = momentumM(m, b, p_m0, beta)
    p_b = momentumB(m, b, p_b0, beta)

    # compute new values of m and b
    m = m - alpha * p_m
    b = b - alpha * p_b

    return m, b, p_m, p_b
# end of def gradientStepWithMomentum

# iteration count
N = 101

# learning rate
alpha = 0.01

# momentum coefficient
beta = 0.9

# initial values
m = b = 0
p_m = p_b = 1

# lists to keep the error and the iteration values.
errors = []
Ns = []

# Let's start iterating
for i in range(N):
    # append these value for plotting grapghic
    errors.append(computeError(m, b))
    Ns.append(i)

    if i % 10 == 0:
        print(i, "\t error:", computeError(m, b))

    m, b, p_m, p_b = gradientStepWithMomentum(alpha, m, b, p_m, p_b, beta)
# end of for loop

# drawing of graph.
plt.title("Error distribution for %s iteration" % N)
plt.ylabel("Error")
plt.xlabel("Iteration")
plt.plot(Ns, errors)
plt.show()