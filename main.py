from src.data_preprocessing import load_data, preprocess_data
from src.analysis import calculate_average_temperature, total_rainfall
from src.visualization import plot_temperature, plot_rainfall

def main():
    # Load data
    df = load_data('data/weather_data.csv')
    
    # Preprocess data
    df = preprocess_data(df)
    
    # Calculate statistics
    average_temperature = calculate_average_temperature(df)
    print(f'Average Temperature: {average_temperature} °C')
    
    total_rain = total_rainfall(df)
    print(f'Total Rainfall: {total_rain} mm')
    
    # Visualize results
    plot_temperature(df)
    plot_rainfall(df)

if __name__ == '__main__':
    main()
