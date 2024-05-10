
import pandas as pd
import numpy as np

# Loading the CSV file
trades_df = pd.read_csv('C:/Users/shaik/Downloads/task/task/task1/tradelog.csv')

entry_prices = trades_df['Entry Price']
exit_prices = trades_df['Exit Price']

# Calculate the necessary parameters
initial_portfolio_value = 6500
risk_free_rate = 0.05

# 1. Total Trades
total_trades = len(trades_df)

# 2. Profitable Trades
profitable_trades = len(trades_df[entry_prices < exit_prices])

# 3. Loss-Making Trades
loss_making_trades = total_trades - profitable_trades

# 4. Win Rate
win_rate = profitable_trades / total_trades

# 5. Average Profit per trade
average_profit_per_trade = np.mean(exit_prices - entry_prices)

# 6. Average Loss per trade
average_loss_per_trade = np.mean(entry_prices - exit_prices)

# 7. Risk Reward ratio
risk_reward_ratio = average_profit_per_trade / average_loss_per_trade

# 8. Expectancy
loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit_per_trade) - (loss_rate * average_loss_per_trade)

# 9. Average ROR per trade (Assuming Volatility is the standard deviation of trade returns)
volatility = np.std((exit_prices - entry_prices) / entry_prices)
average_ror_per_trade = (expectancy / volatility)

# 10. Sharpe Ratio
rate_of_return = ((initial_portfolio_value + np.sum(exit_prices - entry_prices)) / initial_portfolio_value) - 1
sharpe_ratio = (rate_of_return - risk_free_rate) / volatility

# 11. Max Drawdown
cumulative_returns = np.cumsum(exit_prices - entry_prices)
max_drawdown = np.max(np.maximum.accumulate(cumulative_returns) - cumulative_returns)

# 12. Max Drawdown Percentage
max_drawdown_percentage = (max_drawdown / initial_portfolio_value) * 100

# 13. CAGR
ending_value = initial_portfolio_value + np.sum(exit_prices - entry_prices)
cagr = (ending_value / initial_portfolio_value) ** (1 / (total_trades / 2)) - 1

# 14. Calmar Ratio
calmar_ratio = cagr / max_drawdown_percentage

# Display the results
results = {
    "Total Trades": total_trades,
    "Profitable Trades": profitable_trades,
    "Loss-Making Trades": loss_making_trades,
    "Win Rate": win_rate,
    "Average Profit per trade": average_profit_per_trade,
    "Average Loss per trade": average_loss_per_trade,
    "Risk Reward ratio": risk_reward_ratio,
    "Expectancy": expectancy,
    "Average ROR per trade": average_ror_per_trade,
    "Sharpe Ratio": sharpe_ratio,
    "Max Drawdown": max_drawdown,
    "Max Drawdown Percentage": max_drawdown_percentage,
    "CAGR": cagr,
    "Calmar Ratio": calmar_ratio
}

results_df = pd.DataFrame(results, index=[0])
results_df.to_csv('tradelog_results.csv', index=False)

print(results_df)
