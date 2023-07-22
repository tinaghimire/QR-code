# QR Code Generator for CSV Data

This code is a Python script that uses the `pandas` library to read data from a CSV file, generates QR codes for each row of data, and then saves the generated QR codes back to a new CSV file.

Here's a step-by-step description of the code:

1. Importing required libraries:
   - `pandas`: This library is used for data manipulation and analysis.
   - `qrcode`: This library is used to generate QR codes.

2. Reading the CSV file:
   The script reads data from the CSV file named "file.csv" using the `pd.read_csv()` function and stores it in a DataFrame called `file`.

3. Iterating through the DataFrame:
   The script then iterates through each row of the DataFrame using a `for` loop and the `file.iterrows()` function. For each row, it extracts the values of the "Name," "Username," and "Email" columns.

4. Creating the data for the QR code:
   The script formats the data as a string that includes the name, username, and email for each row.

5. Generating the QR code:
   The `qrcode.make()` function is used to create a QR code image from the data string generated in the previous step.

6. Saving the QR code:
   The QR code image is saved to a file with a name based on the index of the current row. The file names will be in the format "num_{index}.png".

7. Building a list of QR code file names:
   For each row, the script creates a file name in the format "num_{index}" (without the ".png" extension) and appends it to the list called `lst`.

8. Updating the DataFrame with QR code file names:
   The list of QR code file names is then added as a new column named "QR" at the 2nd position (index 2) in the DataFrame `file` using the `file.insert()` method.

9. Printing the DataFrame head:
   The script prints the first few rows of the DataFrame using the `file.head()` method to display the updated DataFrame with the QR code file names added as a new column.

10. Saving the updated DataFrame to a new CSV file:
    Finally, the script saves the updated DataFrame with the QR code file names to a new CSV file named "newfile.csv" using the `file.to_csv()` method. The `index=False` argument ensures that the index column is not saved in the CSV file, and `header=True` keeps the header in the output file.

Note: The script assumes that the input CSV file ("file.csv") has columns named "Name," "Username," and "Email," which is necessary for the code to work correctly. Additionally, it also assumes that the `qrcode` library is installed in the Python environment. If not, you can install it using `pip install qrcode`.
