import numpy as np
from scipy import stats 
from Stats import Stats

rvs1 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=42)
rvs2 = (stats.norm.rvs(loc=5, scale=10, size=500, random_state=42)
        + stats.norm.rvs(scale=0.2, size=500, random_state=42))
print(np.mean(rvs1))
print(np.mean(rvs2))
print(Stats.two_samp_ttest(rvs1,rvs2))

# pvalue=0.8762
# Since the pvalue is greater than 0.05, the null hypothesis is not rejected, hence 
# there are no difference between the averages of the samples
# (confirming the mean calculated before)


