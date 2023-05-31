# my-scripts
personal scripts to make my work easier and faster

# Invoice Generator

This script generates an invoice based on the provided description file. It extracts the necessary information from the description file and creates an invoice in Excel format.

## Requirements
- Python 3.x
- pandas library
- xlsxwriter library

## Usage
```
python invoice_generator.py <description_file>
```

Replace `<description_file>` with the path to the description file.

## Functionality
1. Read the description file provided as a command-line argument.
2. Filter the description data for the assigned person.
3. Retrieve the current month and year.
4. Create a date range for the month excluding Sundays.
5. Generate invoice data for each day, including two entries per day.
6. Create a DataFrame from the invoice data.
7. Update the Description column to include line breaks.
8. Save the invoice to an Excel file with the filename "Name_Company_Invoice<month><year>.xlsx".
9. Display a success message.

## Example
```
python invoice_generator.py "description_file.xlsx"
```

The script will generate an invoice file named "Name_Company_InvoiceMMYY.xlsx" based on the provided description file.

**Note:** Ensure that the description file is in Excel format (xlsx).

## Contact
For any issues or inquiries, please contact me at mweembadabwitso@gmail.com.
