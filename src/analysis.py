import numpy as np

def calculate_average_temperature(df):
    """Calculate average temperature."""
    average_temperature = np.mean(df['Temperature'])
    return average_temperature

def total_rainfall(df):
    """Calculate total rainfall."""
    total_rain = np.sum(df['Rainfall'])
    return total_rain
