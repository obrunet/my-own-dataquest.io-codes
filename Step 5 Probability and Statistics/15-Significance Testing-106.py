## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)
plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)
# Null hypothesis -> mean_difference = 0 # Alternative hypothesis -> mean_difference > 0

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

mean_differences = []
for i in range(1000):
    group_a, group_b = [], []
    for val in all_values:
        weight_loss = np.random.rand() 
        if weight_loss >= .5:
            group_a.append(val)
        else:
            group_b.append(val)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {} # keys will be the test statistics and whose values are the frequencies of the test statistics
for each in mean_differences:
    if each not in sampling_distribution:
        sampling_distribution[each] = 1
    else:
        sampling_distribution[each] += 1
    
    """
    if sampling_distribution.get(each, False):
        # If in the dictionary, grab the value, increment by 1, reassign.
        val = sampling_distribution.get(each)
        inc = val + 1
        sampling_distribution[each] = inc
    else:
        # If not in the dictionary, assign `1` as the value to that key.
        sampling_distribution[each] = 1 
        """

## 8. P value ##

frequencies = []
for sd in sampling_distribution:
    if sd >= 2.52:
        frequencies.append(sampling_distribution[sd])
p_value = np.sum(frequencies) / 1000
# Since the p value of 0 is less than the threshold we set of 0.05, we conclude that 
# the difference in weight lost can't be attributed to random chance alone. 
# We therefore reject the null hypothesis and accept the alternative hypothesis.