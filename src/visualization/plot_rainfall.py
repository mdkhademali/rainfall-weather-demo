
import matplotlib.pyplot as plt

def plot_rainfall(df):

    plt.figure()
    plt.plot(df['rainfall_mm'])
    plt.title("Daily Rainfall")
    plt.xlabel("Day")
    plt.ylabel("Rainfall (mm)")
    plt.show()
