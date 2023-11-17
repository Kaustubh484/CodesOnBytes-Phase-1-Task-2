import pandas as pd

def import_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset imported successfully.")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Empty dataset found in file: {file_path}")
        return None

def clean_dataset(df):
    # Display count of missing values before cleaning
    print("\nCount of missing values before cleaning:")
    print(df.isnull().sum())

    # Replace missing values with the mean of the respective columns
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Identify and remove outliers using z-score
    z_scores = (df.select_dtypes(include=['number']) - df.select_dtypes(include=['number']).mean()) / df.select_dtypes(include=['number']).std()

    # Display z-scores
    print("\nZ-Scores:")
    print(z_scores)

    # Display count of rows before and after removing outliers
    print("\nCount of rows before removing outliers:", len(df))
    df_cleaned = df[(z_scores.abs() < 3).all(axis=1)]
    print("Count of rows after removing outliers:", len(df_cleaned))

    return df_cleaned

def main():
    # Update file path
    file_path = r"C:\Users\Kaustubh Shah\Downloads\dataset - netflix1.csv"

    # Import dataset from CSV file
    dataset = import_dataset(file_path)

    if dataset is not None:
        # Display summary statistics before cleaning
        print("\nSummary statistics before cleaning:")
        print(dataset.describe())

        # Clean the dataset
        cleaned_dataset = clean_dataset(dataset)

        # Display summary statistics after cleaning
        print("\nSummary statistics after cleaning:")
        print(cleaned_dataset.describe())

        # Save cleaned dataset as CSV
        cleaned_dataset.to_csv("cleaned_dataset.csv", index=False)
        print("Cleaned dataset saved as cleaned_dataset.csv")

if __name__ == "__main__":
    main()
