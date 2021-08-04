# starting with pseudocode

# Generate random number from 1-10 and assign to variable 'num'

# Create starting point total 'score' initially set to 10

# Prompt player to guess a number between 1 and 10
# Store input as 'guess'


# Sanitize input: check if guess is actually an integer, and prompt for a new guess if not

# check if 'guess' == 'num'
# If not, state incorrect and if 'guess' is higher or lower than 'num'
# Deduct one point
# output 'Too high/low, try again'
# repeat until 'guess' == 'num'

# If 'score' == 0 - game over

# When 'guess' == 'num'
# output 'You win! 'num' was the correct answer!'
# Your score is 'score' - score will be remainder after deducting one for each incorrect guess
