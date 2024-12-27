import os
from scripts.convert_txt_to_csv import convert_txt_to_csv
import pandas as pd

def test_convert_txt_to_csv():
    # Create test data
    test_input = "data/test_data.txt"
    test_output = "data/test_data.csv"

    # Write a test TXT file
    with open(test_input, "w") as f:
        f.write("col1\tcol2\tcol3\n1\t2\t3\n4\t5\t6")

    # Run the conversion
    convert_txt_to_csv(test_input, test_output)

    # Validate the output
    assert os.path.exists(test_output), "CSV file was not created."
    df = pd.read_csv(test_output)
    assert df.shape == (2, 3), "CSV file content does not match expected."

    # Clean up
    os.remove(test_input)
    os.remove(test_output)
    print("Test passed successfully.")
