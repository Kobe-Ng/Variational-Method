
# A lot of thinking still needs to be done on how exactly this is going to work. Right now I believe there are two functions.
# One is a cost function. This will take in some array of cn & n, create the exponential series and calculate the expectation 
# Value of energy. The goal is to minimize the final expecation value calculated. There will be some other equation
# That will be a function of weights and biases. The goal of this function is to generate the cn and n going
# into the cost function. Adjusting weights and biases will generate different cn. I'm not sure if this plan will
# work when I try and implement it, but that's the thinking for now.
# TODO: read a lot more about machine learning

def cost():