# pepe-analyse
analyzing @pepecoineth (pepe.com) using python
A DATA-DRIVEN APPROACH TO CRYPTOCURRENCY SPECULATION
How do PEPE coin behave? What are the causes of the sudden spikes and dips in cryptocurrency values? Are the markets for different altcoins inseparably linked or largely independent? How can we predict what will happen next?

The goal of this article is to provide an easy introduction to cryptocurrency analysis using Python. We will walk through a simple Python script to retrieve, analyze, and visualize data on #PEPE (pepe.com). In the process, we will uncover an interesting trend in how these volatile markets behave, and how they are evolving.


![Figure_1 1](https://github.com/user-attachments/assets/acf9fa93-dd41-4df6-bcd7-0437c7a26688)

1 : Fetch PEPE cryptocurrency data using the CoinGecko API.
2 : Process the data to make it ready for visualization.
3 : Visualize the data using libraries like matplotlib and pandas.

1. Install Required Packages :
pip install requests pandas matplotlib

Explanation:
Fetching PEPE Data: The function get_pepe_data() sends an HTTP request to CoinGecko’s API to fetch market data for PEPE in USD over the last 30 days.

Processing the Data: In process_data(), we convert the timestamp data (in milliseconds) to readable datetime format and prepare a pandas DataFrame containing the date and price information.

Visualization: The function plot_pepe_data() uses matplotlib to plot PEPE’s price trend over the last 30 days.

Running the Script:
python3 pepe.py
