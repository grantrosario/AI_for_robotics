def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
for k in range(len(motion)):
    mu, sig = update(mu, sig, measurements[k], measurement_sig)
    print "update: ", [mu, sig]
    mu, sig = predict(mu, sig, motion[k], motion_sig)
    print "predict: ", [mu, sig]

# note that for the assignment you must just print the [mu, sig] tuple once, outside of the for loop


    


