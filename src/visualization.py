import matplotlib.pyplot as plt

def plot_temperature(df):
    """Line plot for temperature over time."""
    plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='b')
    plt.title('Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout
    plt.show()

def plot_rainfall(df):
    """Bar chart for rainfall over time."""
    plt.bar(df['Date'], df['Rainfall'], color='skyblue')
    plt.title('Rainfall Over Time')
    plt.xlabel('Date')
    plt.ylabel('Rainfall (mm)')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout
    plt.show()
