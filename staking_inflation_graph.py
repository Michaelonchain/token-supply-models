import matplotlib.pyplot as plt

# Staking Inflation Model (Dynamic)
initial_supply = 1_000_000
inflation_rate = 0.08  # 8% staking reward model
years = 10

supply = [initial_supply]

for year in range(1, years + 1):
    new_supply = supply[-1] * (1 + inflation_rate)
    supply.append(new_supply)

# Plotting the inflation growth
plt.plot(range(0, years + 1), supply, marker='o')
plt.title("Staking Reward Inflation Growth Over Time")
plt.xlabel("Years")
plt.ylabel("Total Token Supply")
plt.grid(True)
plt.show()
