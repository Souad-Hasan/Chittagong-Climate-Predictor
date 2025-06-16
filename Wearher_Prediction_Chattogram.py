import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np

# Load the historical weather data
df = pd.read_csv("Chittagong Weather Data 2010-01-01 to 2022-08-22.csv")
df['datetime'] = pd.to_datetime(df['datetime'], format="%m/%d/%Y")

def predict_weather(date_str):
    try:
        input_date = datetime.strptime(date_str, "%m-%d-%Y")
        exact_match = df[df['datetime'] == input_date]

        if not exact_match.empty:
            # Use actual historical data
            row = exact_match.iloc[0]
            temp = row['temp']
            humidity = row['humidity']
            condition = row['conditions'].lower()
            is_future = False
        else:
            # Estimate based on historical data from same MM-DD
            same_day_data = df[(df['datetime'].dt.month == input_date.month) &
                               (df['datetime'].dt.day == input_date.day)]

            if same_day_data.empty:
                print("No historical data to estimate this future date.")
                return

            temp = same_day_data['temp'].mean()
            humidity = same_day_data['humidity'].mean()
            condition = same_day_data['conditions'].mode()[0].lower()
            is_future = True

        # Simulate hourly temperatures
        hours = list(range(24))
        temperatures = [temp + np.random.uniform(-2, 2) for _ in hours]

        # Plotting the graph
        plt.figure(figsize=(10, 5))
        plt.plot(hours, temperatures, marker='o', color='orange')
        title_prefix = "Predicted" if is_future else "Observed"
        plt.title(f"{title_prefix} Weather on {date_str} - {condition.capitalize()}")
        plt.xlabel("Hour of Day")
        plt.ylabel("Temperature (\u00b0C)")
        plt.grid(True)
        plt.xticks(hours)
        plt.tight_layout()

        # Output text
        print(f"\n{title_prefix} Weather on {date_str}:")
        print(f"Condition: {condition.capitalize()}")
        print(f"Estimated Temperature: {temp:.1f} \u00b0C")
        print(f"Estimated Humidity: {humidity:.0f}%")

        if "rain" in condition:
            print("Advice: Carry an umbrella!")
        elif "cloud" in condition and humidity > 75:
            print("Advice: It might be muddy, wear waterproof shoes.")
        else:
            print("Advice: Perfect day to go outside!")

        plt.show()

    except ValueError:
        print("Invalid date format. Please use MM-DD-YYYY format.")

# Run it
print("Chattogram Weather Forecast (Historical-based Prediction)")
date_input = input("Enter a date (MM-DD-YYYY): ")
predict_weather(date_input)
