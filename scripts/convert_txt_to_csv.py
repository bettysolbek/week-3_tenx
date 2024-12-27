import pandas as pd

def convert_txt_to_csv(input_file, output_file, delimiter="\t"):
    """
    Converts a TXT file to CSV format.

    Args:
        input_file (str): Path to the input .txt file.
        output_file (str): Path to save the output .csv file.
        delimiter (str): Delimiter used in the TXT file. Default is tab ("\t").

    Returns:
        None
    """
    try:
        # Load the TXT file into a DataFrame
        df = pd.read_csv(input_file, delimiter=delimiter, engine='python')

        # Save as CSV
        df.to_csv(output_file, index=False)
        print(f"File converted successfully and saved to {output_file}")
    except Exception as e:
        print(f"Error converting file: {e}")
