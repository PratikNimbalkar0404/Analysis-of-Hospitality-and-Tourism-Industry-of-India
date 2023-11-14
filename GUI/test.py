def find_duplicates(data_list, column1, column2):
    duplicates = []
    seen_items = set()

    for item in data_list:
        if item[column1] == item[column2]:
            if item in seen_items:
                duplicates.append(item)
            else:
                seen_items.add(item)

    return duplicates

# Example usage with a list of dictionaries
data_list = [
    {"Column1": "A", "Column2": "B"},
    {"Column1": "C", "Column2": "D"},
    {"Column1": "A", "Column2": "A"},
    {"Column1": "E", "Column2": "F"},
]

column1 = "Column1"
column2 = "Column2"

duplicates = find_duplicates(data_list, column1, column2)

print("Duplicate entries based on columns", column1, "and", column2, ":", duplicates)
