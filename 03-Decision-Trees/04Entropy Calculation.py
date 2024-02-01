import math 

p_slow = 2/3
p_fast = 1/3

entropy = -p_slow * math.log2(p_slow) - p_fast * math.log2(p_fast)
print("entropy is: ", entropy)



import scipy.stats
print(scipy.stats.entropy([2,1],base=2))


information_gain = 1 - (3/4 * 0.9184) + (1/4*0)
print("information gain grade is: ", information_gain)




# entropy of bumpy
p_slow = 1/2
p_fast = 1/2

entropy_bumpy = -p_slow * math.log2(p_slow) - p_fast * math.log2(p_fast)
print("entropy of bumpy: ", entropy_bumpy)



# entropy of smooth
p_slow = 1/2
p_fast = 1/2

entropy_smooth = -p_slow * math.log2(p_slow) - p_fast * math.log2(p_fast)
print("entropy of smooth: ", entropy_smooth)


# information gain of bumpiness
weight_average_bumpy = 2/4
entropy_bumpy = 1
wight_average_smooth = 2/4
entropy_smooth = 1

information_gain_bumpiness = 1 - ((weight_average_bumpy * entropy_bumpy) + (wight_average_smooth * entropy_smooth))
print("information gain bumpiness is: ", information_gain_bumpiness)




# information gain of speed limit
weight_average_speed_limit = 2/4
entropy_yes = 0
wight_average_no_speed_limit = 2/4
entropy_no = 0

information_gain_speed_limit = 1 - ((weight_average_speed_limit * entropy_yes) + (wight_average_no_speed_limit * entropy_no))
print("information gain speed limit is: ", information_gain_speed_limit)