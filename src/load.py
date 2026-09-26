import os


def load_data(df, file_name):
    os.makedirs("data/processed", exist_ok=True)

    output_path = f"data/processed/{file_name}"

    df.to_csv(output_path, index=False)

    print(f"Data loaded successfully: {output_path}")
