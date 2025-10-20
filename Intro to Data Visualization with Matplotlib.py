# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')
climate_change = pd.read_csv('climate_change.csv')
# Map month number to 3-letter abbreviation
# month_map = {
#     1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
#     5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
#     9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
# }
# Add new column with month abbreviation
# seattle_weather['MONTH'] = seattle_weather['DATE'].map(month_map)
# print(seattle_weather['DATE'])
# seattle_weather.info()

# # 1.1 Using the matplotlib.pyplot interface
# # Create a Figure and an Axes with plt.subplots
# fig, ax = plt.subplots()

# # Call the show function to show the result
# plt.show()

# # 1.2 Adding data to an Axes object
# # Create a Figure and an Axes with plt.subplots
# fig, ax = plt.subplots()

# # Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
# ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# # Plot MLY-PRCP-NORMAL from austin_weather against MONTH
# # ax.plot(seattle_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# # Call the show function
# plt.show()

# # 1.3 Customizing data appearance
# # Plot Seattle data, setting data appearance
# ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color="b" , marker = "o" , linestyle = "--")

# # Plot Austin data, setting data appearance
# ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r" , marker = "v" , linestyle = "--")

# # Call show to display the resulting plot
# plt.show()

# # 1.4 Customizing axis labels and adding titles
# ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
# ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# # Customize the x-axis label
# ax.set_xlabel("Time (months)")

# # Customize the y-axis label
# ax.set_ylabel("Precipitation (inches)")

# # Add the title
# ax.set_title("Weather patterns in Austin and Seattle")

# # Display the figure
# plt.show()

# # 1.4 Creating small multiples with plt.subplots
# Create a Figure and an array of subplots with 2 rows and 2 columns
# fig, ax = plt.subplots(2, 2)

# # Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
# ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# # In the top right (index 0,1), plot month and Seattle temperatures
# ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# # In the bottom left (1, 0) plot month and Austin precipitations
# ax[1,0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# # In the bottom right (1, 1) plot month and Austin temperatures
# ax[1,1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
# plt.show()

# # 1.5 Small multiples with shared y axis
# # Create a figure and an array of axes: 2 rows, 1 column with shared y axis
# fig, ax = plt.subplots(2, 1, sharey=True)

# # Plot Seattle precipitation data in the top axes
# ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color = "b")
# ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color = "b", linestyle = "--")
# ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color = "b", linestyle = "--")

# # Plot Austin precipitation data in the bottom axes
# ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color = "r")
# ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color = "r", linestyle = "--")
# ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color = "r", linestyle = "--")

# plt.show()

# # 2.1 Read data with a time index
# # Read the data from file using read_csv
# climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")

# # 2.2 Plot time-series data
# fig, ax = plt.subplots()

# # Add the time-series for "relative_temp" to the plot
# ax.plot(climate_change.index, climate_change["relative_temp"])

# # Set the x-axis label
# ax.set_xlabel("Time")

# # Set the y-axis label
# ax.set_ylabel("Relative temperature (Celsius)")

# # Show the figure
# plt.show()

# # 2.3 Using a time index to zoom in
# # Use plt.subplots to create fig and ax
# fig, ax = plt.subplots()

# # Create variable seventies with data from "1970-01-01" to "1979-12-31"
# seventies = climate_change["1970-01-01":"1979-12-31"]

# # Add the time-series for "co2" data from seventies to the plot
# ax.plot(seventies.index, seventies["co2"])

# # Show the figure
# plt.show()

# # 2.4 Plotting two variables
# # Initalize a Figure and Axes
# fig, ax = plt.subplots()

# # Plot the CO2 variable in blue
# ax.plot(climate_change.index, climate_change['co2'], color='b')

# # Create a twin Axes that shares the x-axis
# ax2 = ax.twinx()

# # Plot the relative temperature in red
# ax2.plot(climate_change.index, climate_change['relative_temp'], color='r')

# plt.show()

# # 2.5 Defining a function that plots time-series data
# # Define a function called plot_timeseries
# def plot_timeseries(axes, x, y, color, xlabel, ylabel):

#   # Plot the inputs x,y in the provided color
#   axes.plot(x, y, color=color)

#   # Set the x-axis label
#   axes.set_xlabel(xlabel)

#   # Set the y-axis label
#   axes.set_ylabel(ylabel, color=color)

#   # Set the colors tick params for y-axis
#   axes.tick_params('y', colors=color)

# # 2.6 Using a plotting function
# fig, ax = plt.subplots()

# # Plot the CO2 levels time-series in blue
# plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue", 'Time (years)', 'CO2 levels')

# # Create a twin Axes object that shares the x-axis
# ax2 = ax.twinx()

# # Plot the relative temperature data in red
# plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], "red", 'Time (years)', "Relative temperature (Celsius)")

# plt.show()

# # 2.7 Annotating a plot of time-series data
# fig, ax = plt.subplots()

# # Plot the relative temperature data
# ax.plot(climate_change.index , climate_change['relative_temp'])

# # Annotate the date at which temperatures exceeded 1 degree
# ax.annotate('>1 degree', xy=(pd.Timestamp('2015-10-06'), 1))

# plt.show()

# # 2.8 Plotting time-series: putting it all together
# fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
# plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)', 'CO2 levels')

# # Create an Axes object that shares the x-axis
# ax2 = ax.twinx()

# # Plot the relative temperature data in red
# plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temp (Celsius)')

# # Annotate point with relative temperature >1 degree
# ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'),1), xytext=(pd.Timestamp('2008-10-06'),-0.2), arrowprops={"arrowstyle":"->", "color":"gray"})

# plt.show()

# # 3.1 Bar chart
# fig, ax = plt.subplots()

# # Plot a bar-chart of gold medals as a function of country
# ax.bar(medals.index, medals['Gold'])

# # Set the x-axis tick labels to the country names
# ax.set_xticklabels(medals.index, rotation=90)

# # Set the y-axis label
# ax.set_ylabel('Number of medals')

# plt.show()

# # 3.2 Stacked bar chart
# # Add bars for "Gold" with the label "Gold"
# ax.bar(medals.index, medals['Gold'], label='Gold')

# # Stack bars for "Silver" on top with label "Silver"
# ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')

# # Stack bars for "Bronze" on top of that with label "Bronze"
# ax.bar(medals.index, medals['Bronze'], bottom=medals['Gold'] + medals['Silver'], label='Bronze')

# # Display the legend
# ax.legend()

# plt.show()

# # 3.3 Creating histograms
# fig, ax = plt.subplots()
# # Plot a histogram of "Weight" for mens_rowing
# ax.hist(mens_rowing['Weight'])

# # Compare to histogram of "Weight" for mens_gymnastics
# ax.hist(mens_gymnastics['Weight'])

# # Set the x-axis label to "Weight (kg)"
# ax.set_xlabel('Weight (kg)')

# # Set the y-axis label to "# of observations"
# ax.set_ylabel('# of observations')

# plt.show()

# # 3.4 "Step" histogram
# fig, ax = plt.subplots()

# # Plot a histogram of "Weight" for mens_rowing
# ax.hist(mens_rowing['Weight'], label='Rowing', bins=5, histtype="step")

# # Compare to histogram of "Weight" for mens_gymnastics
# ax.hist(mens_gymnastics['Weight'], label='Gymnastics', bins=5, histtype="step")

# ax.set_xlabel("Weight (kg)")
# ax.set_ylabel("# of observations")

# # Add the legend and show the Figure
# ax.legend()
# plt.show()

# # 3.5 Adding error-bars to a bar chart
# fig, ax = plt.subplots()

# # Add a bar for the rowing "Height" column mean/std
# ax.bar("Rowing", mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())

# # Add a bar for the gymnastics "Height" column mean/std
# ax.bar("Gymnastics", mens_gymnastics['Height'].mean(), yerr=mens_gymnastics['Height'].std())

# # Label the y-axis
# ax.set_ylabel('Height (cm)')

# plt.show()

# # 3.6 Adding error-bars to a plot
# fig, ax = plt.subplots()

# # Add Seattle temperature data in each month with error bars
# ax.errorbar(seattle_weather['MONTH'], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# # Add Austin temperature data in each month with error bars
# ax.errorbar(austin_weather['MONTH'], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# # Set the y-axis label
# ax.set_ylabel('Temperature (Fahrenheit)')

# plt.show()

# # 3.7 Creating boxplots
# fig, ax = plt.subplots()

# # Add a boxplot for the "Height" column in the DataFrames
# ax.boxplot([mens_rowing['Height'],mens_gymnastics['Height']])

# # Add x-axis tick labels:
# ax.set_xticklabels(['Rowing', 'Gymnastics'])

# # Add a y-axis label
# ax.set_ylabel('Height (cm)')

# plt.show()

# # 3.8 Simple scatter plot
# fig, ax = plt.subplots()

# # Add data: "co2" on x-axis, "relative_temp" on y-axis
# ax.scatter(climate_change['co2'], climate_change['relative_temp'])

# # Set the x-axis label to "CO2 (ppm)"
# ax.set_xlabel('CO2 (ppm)')

# # Set the y-axis label to "Relative temperature (C)"
# ax.set_ylabel('Relative temperature (C)')

# plt.show()

# # 3.9 Encoding time by color
# fig, ax = plt.subplots()

# # Add data: "co2", "relative_temp" as x-y, index as color
# ax.scatter(climate_change['co2'], climate_change['relative_temp'], c=climate_change.index)

# # Set the x-axis label to "CO2 (ppm)"
# ax.set_xlabel('CO2 (ppm)')

# # Set the y-axis label to "Relative temperature (C)"
# ax.set_ylabel('Relative temperature (C)')

# plt.show()

# # 4.1 Switching between styles
# # Use the "ggplot" style and create new Figure/Axes
# plt.style.use('ggplot')
# fig, ax = plt.subplots()
# ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
# plt.show()

# # Use the "Solarize_Light2" style and create new Figure/Axes
# plt.style.use('Solarize_Light2')
# fig, ax = plt.subplots()
# ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
# plt.show()

# # 4.2 Saving a file several times
# # Save as a PNG file with 300 dpi
# fig.savefig('my_figure_300dpi.png', dpi=300)

# # # 4.3 Save a figure with different sizes
# # Set figure dimensions and save as a PNG width 5 height 3
# fig.set_size_inches([5,3])
# fig.savefig('figure_5_3.png')

# # 4.4 Unique values of a column
# # Extract the "Sport" column
# sports_column = summer_2016_medals['Sport']

# # Find the unique values of the "Sport" column
# sports = sports_column.unique()

# # Print out the unique sports values
# print(sports)

# # 4.5 Automate your visualization
# fig, ax = plt.subplots()

# # Loop over the different sports branches
# for sport in sports:
#   # Extract the rows only for this sport
#   sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
#   # Add a bar for the "Weight" mean with std y error bar
#   ax.bar(sport, sport_df["Weight"].mean(),  
# yerr=sport_df["Weight"].std()) 
# ax.set_ylabel("Weight")
# ax.set_xticklabels(sports, rotation=90)

# # Save the figure to file
# fig.savefig('sports_weights.png')