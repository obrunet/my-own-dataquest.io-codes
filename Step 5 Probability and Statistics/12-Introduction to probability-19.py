## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
bars_sorted = flags.sort_values(by = ["bars"], ascending = False)
most_bars_country = bars_sorted["name"].iloc[0]
population_sorted = flags.sort_values(by = ["population"], ascending = False)
highest_population_country = population_sorted["name"].iloc[0]

## 2. Calculating probability ##

total_countries = flags.shape[0]
# We could compute the probability of a country flag having a certain characteristic by dividing how many flags have that characteristic by the total number of flags
orange_probability = flags[flags["orange"] == 1].shape[0] / total_countries
stripe_probability = flags[flags["stripes"] > 1].shape[0] / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
# probability that 10 & 100 flips in a row will all turn out heads
ten_heads = 0.5 ** 10
hundred_heads = 0.5 ** 100

## 4. Dependent probabilities ##

# odds of picking three countries with red in their flags in a row:
total_count = flags.shape[0]
red_count = flags[flags['red'] == 1].shape[0]
three_red = (red_count / total_count) * \
    ((red_count-1) / (total_count-1)) * \
    ((red_count-2) / (total_count-2))


## 5. Disjunctive probability ##

# we actually can just add the probabilities, because both events are independent
start = 1
end = 18000

def count_evenly_divisible(start, end, div):
    nb_div = 0
    for i in range(start, end+1):
        if (i % div) ==0:
            nb_div += 1
    return nb_div
            
# odds of getting a number evenly divisible by 100 / 70, with no remainder
hundred_prob = count_evenly_divisible(start, end, 100) / end
seventy_prob = count_evenly_divisible(start, end, 70) / end

## 6. Disjunctive dependent probabilities ##

flags_nb = flags.shape[0]

# probability of a flag having red or orange as a color
orange = flags[flags['orange'] == 1].shape[0]
red = flags[flags['red'] == 1].shape[0]
red_and_orange = flags[(flags['orange'] == 1) & (flags['red'] == 1)].shape[0]
red_or_orange = (orange + red - red_and_orange) / flags_nb

# probability of a flag having at least one stripe or at least one bar
stripes = flags[flags['stripes'] > 0].shape[0]
bars = flags[flags['bars'] > 0].shape[0]
stripes_and_bars = flags[(flags['stripes'] > 0) & (flags['bars'] > 0)].shape[0]
stripes_or_bars = (stripes + bars - stripes_and_bars) / flags_nb

## 7. Disjunctive probabilities with multiple conditions ##

# Let's say we have a coin that we're flipping. Find the probability that at least one of the first three flips comes up heads
heads_or = 1 - (.5*.5*.5) # 1 minus the probability of all tails