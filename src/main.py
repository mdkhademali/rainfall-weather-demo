
import pandas as pd
from models.rainfall_model import train_model
from visualization.plot_rainfall import plot_rainfall

def main():
    df = pd.read_csv("data/sample_rainfall_data.csv")

    print("Dataset Loaded")
    print(df.head())

    model, score = train_model(df)

    print(f"Model R2 Score: {score}")

    plot_rainfall(df)

if __name__ == "__main__":
    main()
