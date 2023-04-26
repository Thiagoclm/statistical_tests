import numpy as np
from scipy import stats 
from Stats import Stats

rvs1 = [0.0571, 0.0813, 0.0831, 0.0976, 0.0817, 0.0859, 0.0735,
             0.0659, 0.0923, 0.0836]
rvs2 = [0.0873, 0.0662, 0.0672, 0.0819, 0.0749, 0.0649, 0.0835,
           0.0725]
rvs3 = [0.1033, 0.0915, 0.0781, 0.0685, 0.0677, 0.0697, 0.0764,
           0.0689]

print(Stats.multi_samp_anova(rvs1,rvs2,rvs3))

# pvalue=0.6121
# Since the pvalue is greater than 0.05, the null hypothesis is not rejected, hence 
# the three samples are drawn from the same distribution


