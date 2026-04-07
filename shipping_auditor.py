# The Detailed Challenge:

# "The Smart Warehouse Auditor"

# The Scenario:
# You are developing software for a global shipping warehouse. You receive a raw list of package weights (in kilograms). However, the data is messy: it contains negative weights (sensor errors) and weights exceeding 1000kg (illegal oversized loads).

# The Task:
# You must build a modular program with three distinct functions to process this data safely.
# clean_data(weights): Removes any weight 0 < and > 1000.
# apply_shipping_fee(weights): Adds a flat $10 fee to packages under 20kg and a $25 fee to packages 20kg or over. It should return a list of fee-adjusted prices (not weights).
# get_inventory_stats(weights, fees): Returns a summary string showing the total count of valid packages and the total revenue from fees.

def clean_data(weights):
    cleaned_weights = []
    for weight in weights:
        if 0 < weight < 1000:
            cleaned_weights.append(weight)

    return cleaned_weights

def apply_shipping_fee(weights):
    fees = []
    for weight in weights:
        if weight < 20:
            fees.append(10)
        else:
            fees.append(25)

    return fees

def get_inventory_stats(weights, fees):
    total_packages = len(weights)
    total_revenue = sum(fees)
    return f"Total valid packages: {total_packages}, Total revenue: ${total_revenue}"

# weights =  [-5, 10, 25, 2000, 18, 50, 1001, 5]
weights2 = [2, -23, 21, 150, 1190, 834]

cleaned_weights = clean_data(weights2)

fees = apply_shipping_fee(cleaned_weights)

stats = get_inventory_stats(cleaned_weights, fees)

print(stats)

# 1. local working directory
#  a. Initially all files will be Untracked stage (which git is not tracking any files in the directory yet)
#  b. After git add, files will be in Staging stage (ready to be committed, will be tracked by git)
#  c. After git commit, files will be in Committed stage (saved in local repository, but not yet pushed to remote repository)
#  d. After git push, files will be in Remote repository (available on GitHub or other hosting service, can be accessed by others if repository is public)