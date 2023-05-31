import pandas as pd
from datetime import datetime
import calendar
import sys

def generate_invoice(filename, description_file):
    """
    Generate an invoice based on the provided description file.

    Args:
        filename (str): The name of the invoice file to be generated.
        description_file (str): The path to the description file.

    Returns:
        None
    """
    # Read the description file
    df_description = pd.read_excel(description_file)
    
    # Filter the description data for the assigned person
    assigned_to = 'Dabwitso Mweemba'
    filtered_description = df_description[df_description['Assigned To'] == assigned_to]['Description']
    
    # Get the current month and year
    now = datetime.now()
    month = now.strftime("%m")
    year = now.strftime("%y")
    
    # Create the date range for the month
    _, num_days = calendar.monthrange(int(year), int(month))
    dates = [f"{i} {calendar.month_abbr[int(month)]} 20{year}" for i in range(1, num_days + 1) if datetime(int(year), int(month), i).weekday() != 6]
    
    # Create a list to store the invoice data
    invoice_data = []
    
    # Generate invoice data for each day
    for date in dates:
        # First entry for the day
        invoice_data.append({
            'Date': date,
            'From': '07:20',
            'To': '12:30',
            'Hours': '=TIMEVALUE("12:30")-TIMEVALUE("07:20")',
            'Category': 'Tech Support',
            'Description': filtered_description.values[0]
        })

        # Second entry for the day
        invoice_data.append({
            'Date': date,
            'From': '13:30',
            'To': '17:20',
            'Hours': '=TIMEVALUE("17:20")-TIMEVALUE("13:30")',
            'Category': 'Tech Support',
            'Description': filtered_description.values[1]
        })
    
    # Create a DataFrame from the invoice data
    invoice_df = pd.DataFrame(invoice_data)

    # Update the Description column to include line breaks
    invoice_df['Description'] = invoice_df['Description'].apply(lambda x: x.replace('\n', '\n\n'))
    
    # Save the invoice to an Excel file using xlsxwriter engine
    invoice_df.to_excel(filename, index=False, engine='xlsxwriter')
    
    # Display success message
    print(f"\033[92mThe {filename} has been created successfully.\033[0m")

def main():
    """
    Main function to handle command-line arguments and generate the invoice.
    """
    if len(sys.argv) < 2:
        print("Please provide the description file as a command-line argument.")
        return
    
    # Extract the description file path from the command-line arguments
    description_file = sys.argv[1]
    
    # Set the invoice filename
    invoice_filename = f"DM029_EZL_Invoice{datetime.now().strftime('%m%y')}.xlsx"
    
    # Generate the invoice
    generate_invoice(invoice_filename, description_file)

if __name__ == "__main__":
    main()
