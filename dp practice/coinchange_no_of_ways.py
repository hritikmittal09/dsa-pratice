def coinChangeWays(coins: list[int], n: int) -> int:
    # Number of coins
    m = len(coins)
    
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: There's 1 way to make sum 0 (use no coins)
    for i in range(m + 1):
        dp[i][0] = 1

    # Fill the DP table
    for i in range(1, m + 1):  # Iterate through coins
        for j in range(1, n + 1):  # Iterate through sums
            if coins[i - 1] <= j:  # If the coin can contribute
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:  # If the coin cannot contribute
                dp[i][j] = dp[i - 1][j]
    
    # The answer is in dp[m][n], i.e., using all coins to make sum `n`
    return dp[m][n]

# Example Usage
coins = [1, 2, 3]
n = 5
result = coinChangeWays(coins, n)
print(f"Number of ways to make sum {n}:", result)
