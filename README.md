# Weather-Temparature-Forecasting
# Chattogram (Chittagong) Weather Forecast Project

## 🌦️ Overview
This Python script provides weather information and predictions for Chattogram (Chittagong), Bangladesh using historical weather data from 2010-2022. It can:
- Display actual historical weather when available
- Estimate weather for future dates based on historical patterns
- Generate 24-hour temperature forecasts
- Provide weather condition analysis and practical advice

## 📊 Sample Output
![Sample Weather Forecast](sample_output.png) *(Example visualization would go here)*

## 🛠️ Tools & Technologies
- **Python 3** with these key libraries:
  - `pandas` - Data analysis and manipulation
  - `matplotlib` - Data visualization
  - `numpy` - Numerical operations
  - `datetime` - Date/time handling

## 📂 File Structure
```
chattogram-weather/
├── weather_forecast.py                 # Main Python script
├── Chittagong Weather Data 2010-01-01 to 2022-08-22.csv  # Historical data
├── README.md                           # This documentation
└── requirements.txt                    # Dependency list
```

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chattogram-weather.git
   cd chattogram-weather
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the script with:
```bash
python weather_forecast.py
```

When prompted, enter a date in MM-DD-YYYY format (e.g., "06-15-2018").

### Key Features:
- **Historical Data**: Shows actual weather if date is between 2010-2022
- **Predictions**: Estimates weather for other dates using historical patterns
- **Visualization**: 24-hour temperature forecast graph
- **Practical Advice**: Weather-specific recommendations

## 📝 Data Requirements
The script requires a CSV file named:
`Chittagong Weather Data 2010-01-01 to 2022-08-22.csv`

Required columns:
- `datetime` (format: MM/DD/YYYY)
- `temp` (temperature in °C)
- `humidity` (percentage)
- `conditions` (text description)

## 🔧 How It Works
1. The script loads historical weather data
2. For the input date:
   - If exact historical data exists, it uses that
   - Otherwise, it estimates using data from the same calendar date in other years
3. Generates:
   - A temperature forecast graph
   - Weather condition information
   - Practical advice based on conditions

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📜 License
MIT License

---

*For GitHub:*
- Add a screenshot named `sample_output.png` showing the visualization
- The requirements.txt should contain:
```
pandas>=1.0.0
matplotlib>=3.0.0
numpy>=1.18.0
```
