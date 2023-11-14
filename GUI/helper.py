import pandas as pd
import csv
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

# Load the Excel file into a DataFrame
# file_path = 'makemytrip_com-travel_sample.csv'  # Replace with your Excel file path
# df = pd.read_csv(file_path)

# # Define the two columns you want to compare
# column1 = 'property_name'  # Replace with the name of the first column
# column2 = 'city'  # Replace with the name of the second column

# # Remove rows where the entries in the two columns are the same
# mask = df.duplicated(subset=[column1, column2], keep='first')

# # Remove the rows with matching entries
# df = df[~mask]

# # Save the modified DataFrame back to an Excel file
# output_file = 'makemytrip_com-travel_sample_1.csv'  # Replace with your desired output file path
# df.to_csv(output_file, index=False)

##########################################################################
# Read the CSV file into a DataFrame
# file_path = 'makemytrip_com-travel_sample_1.csv'  # Replace with your CSV file path
# df = pd.read_csv(file_path)

# # Define the column name to filter and the list of allowed values
# filter_column = 'hotel_star_rating'  # Replace with the name of the column to filter
# allowed_values = ['1', '2', '3', '4' , '5', '1 star', '2 star', '3 star', '4 star', '5 star']  # Replace with your list of allowed values

# # Filter rows where the specified column has one of the allowed values
# filtered_df = df[df[filter_column].isin(allowed_values)]
# for index, row in filtered_df.iterrows():
#     if row[filter_column] == '1':
#         # Change the value of a specific column (e.g., 'NewValue') for this row
#         filtered_df.at[index, 'hotel_star_rating'] = '1 star'
#     elif row[filter_column] == '2':
#         filtered_df.at[index, 'hotel_star_rating'] = '2 star'
#     elif row[filter_column] == '3':
#         filtered_df.at[index, 'hotel_star_rating'] = '3 star'
#     elif row[filter_column] == '4':
#         filtered_df.at[index, 'hotel_star_rating'] = '4 star'
#     elif row[filter_column] == '5':
#         filtered_df.at[index, 'hotel_star_rating'] = '5 star'

# # Keep only the specified column and discard all other columns
# # filtered_df = filtered_df[[filter_column]]

# # Save the modified DataFrame back to a CSV file
# output_file = 'filtered_csv_file.csv'  # Replace with your desired output file path
# filtered_df.to_csv(output_file, index=False)

# print("Filtered rows saved to", output_file)
##########################################################################################
# import pandas as pd

# # Read the CSV file into a DataFrame
# file_path = 'filtered_csv_file.csv'  # Replace with your CSV file path
# df = pd.read_csv(file_path)

# # List of columns to remove
# columns_to_remove = [
#      'crawl_date',  'image_urls', 'is_value_plus',  'mmt_holidayiq_review_count', 'mmt_location_rating', 'mmt_review_count',
#     'mmt_review_rating',  'mmt_traveller_type_review_count',
#     'mmt_tripadvisor_count', 'pageurl',  'property_id',
#      'qts', 'query_time_stamp', 
#     'site_review_count', 'site_review_rating', 'sitename',
#     'uniq_id', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36',
#     'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39'
# ]

# # Remove the specified columns from the DataFrame
# df = df.drop(columns=columns_to_remove)

# # Save the modified DataFrame back to a CSV file
# output_file = 'csv_file_without_columns.csv'  # Replace with your desired output file path
# df.to_csv(output_file, index=False)

# print("Columns removed. Saved to", output_file)

file_path = 'csv_file_without_columns.csv'  # Replace with your Excel file path
df = pd.read_csv(file_path)

# Define the desired column order
new_column_order = [
    'property_name', 'property_address', 'property_type', 'room_types', 'hotel_star_rating','mmt_review_score','latitude','longitude',  'area', 'city' ,'state', 'country', 'highlight_value','hotel_overview', 'traveller_rating']# Replace with your desired column order


# Create a new DataFrame with the columns rearranged
df = df[new_column_order]

# Save the new DataFrame back to the Excel file
output_file = 'CSV_file_with_reordered_columns.CSV'  # Replace with your desired output file path
df.to_csv(output_file, index=False)

print("Columns rearranged. Saved to", output_file)



def upload_csv():
    global data_list
    global supplier_consolidated,specific_column_data
    
    # Open file dialog to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    count = 0 
    if file_path:
        # Initialize data structures
        supplier_consolidated = []
        column_data = []
        
        # Read the CSV file
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Read the header row
            supplier_consolidated = next(csv_reader)
            
            # Read the data row by row
            for row in csv_reader:
                count += 1
                column_data.append(row)
        
        # Create a list of tuples with column headings and data
        data_list = list(zip(supplier_consolidated, column_data))
        
        # Notify the user
        messagebox.showinfo("Data uploaded", "Upload Successful!\n\nPlease press Next")

        # Extract data from a specific column by name
        specific_column_name = "property_name"  # Replace with the actual column name
        specific_column_index = supplier_consolidated.index(specific_column_name)
        specific_column_data = [row[specific_column_index] for row in column_data]
        
        # Now, specific_column_data contains the data from the column with the specified name
        # print(specific_column_data)
        print(count)
# Call the function
def find_duplicates_in_csv(file_path, column1, column2):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Create a boolean mask for rows with matching entries in the two columns
    mask = df.duplicated(subset=[column1, column2], keep='first')

    # Get the duplicate rows
    duplicate_rows = df[mask]

    return duplicate_rows

# Specify the CSV file path and the columns to check for duplicates
file_path = 'makemytrip_com-travel_sample.csv'  # Replace with your CSV file path
column1 = 'property_name'  # Replace with the name of the first column
column2 = 'city'  # Replace with the name of the second column

# Find and retrieve duplicate rows
duplicate_rows = find_duplicates_in_csv(file_path, column1, column2)

# Display the duplicate rows
print("Duplicate rows based on columns", column1, "and", column2, ":")
print(duplicate_rows)


# upload_csv()

# # Open and read the CSV file
# with open('hotel_data.csv', mode='r', newline='', encoding='utf-8') as file:
#     csv_reader = csv.DictReader(file)

#     for row in csv_reader:
#         hotel = {
#             'property_name': row['property_name'],
#             'property_address': row['property_address'],
#             'property_type': row['property_type'],
#             'hotel_star_rating': row['hotel_star_rating'],
#             'mmt_review_score': row['mmt_review_score'],
#             'latitude': row['latitude'],
#             'longitude': row['longitude'],
#             'area': row['area'],
#             'city': row['city'],
#             'state': row['state'],
#             'country': row['country'],
#             'highlight_value': row['highlight_value'],
#             'hotel_overview': row['hotel_overview'],
#             'traveller_rating': row['traveller_rating']
#         }
#         hotel_data.append(hotel)

# # Specify the name of the Markdown file where you want to write the data
# markdown_file_name = 'hotel_data.md'



# print ((hotel_data))
# Open the Markdown file for writing
# with open(markdown_file_name, 'w', encoding='utf-8') as markdown_file:
#     # Write a header or introduction to your Markdown file
#     markdown_file.write("# Hotel Data\n\n")
    
#     # Iterate through the 'hotel_data' list and write the information for each hotel
#     for hotel in hotel_data:
#         markdown_file.write(f"## {hotel['property_name']}\n")
#         markdown_file.write(f"- **Property Type**: {hotel['property_type']}\n")
#         markdown_file.write(f"- **City**: {hotel['city']}\n")
#         markdown_file.write(f"- **Rating**: {hotel['hotel_star_rating']}\n")
#         markdown_file.write(f"- **Review Score**: {hotel['mmt_review_score']}\n")
#         markdown_file.write(f"- **Location**: {hotel['latitude']}, {hotel['longitude']}\n")
#         markdown_file.write(f"- **Area**: {hotel['area']}\n")
#         markdown_file.write(f"- **Country**: {hotel['country']}\n")
#         markdown_file.write(f"- **Highlight Value**: {hotel['highlight_value']}\n")
#         markdown_file.write(f"### Overview\n")
#         markdown_file.write(f"{hotel['hotel_overview']}\n")
#         markdown_file.write(f"### Traveller Rating\n")
#         markdown_file.write(f"{hotel['traveller_rating']}\n")

#         # Add any additional formatting or content as desired

#         markdown_file.write("\n")  # Add a newline between hotels

# The 'hotel_data' is now written to 'hotel_data.md'

        
# print (len(hotel_data))

# Now, you have the data in the 'hotel_data' list of dictionaries
# You can access and manipulate the data as needed
