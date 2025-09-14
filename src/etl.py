import pandas as pd

def run_etl():
    """Performs a basic ETL process on the raw healthcare data."""
    try:
        # Load raw data
        df = pd.read_csv('data/raw/healthcare_raw_data.csv')
        
        # Data Cleaning and Transformation
        df['date'] = pd.to_datetime(df['date'])
        
        # Remove any potential duplicates
        df.drop_duplicates(inplace=True)
        
        # Save processed data
        df.to_csv('data/processed/healthcare_processed_data.csv', index=False)
        print("ETL process completed. Data saved to data/processed/healthcare_processed_data.csv")
        
        return df
    except FileNotFoundError:
        print("Error: Raw data file not found. Please run data_generator.py first.")
        return None

if __name__ == '__main__':
    run_etl()