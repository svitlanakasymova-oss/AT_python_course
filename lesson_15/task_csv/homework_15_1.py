import csv

with open('result_csv_Kasymova.csv', 'w') as result_file:
    unique_rows = []
    with open('random.csv', 'r', encoding = 'utf-8') as file_1:
        reader = csv.DictReader(file_1)
        for row in reader:
            if row not in unique_rows:
                unique_rows.append(row)
    with open('random-michaels.csv', 'r', encoding = 'utf-8') as file_2:
        reader = csv.DictReader(file_2)
        for row in reader:
            if row not in unique_rows:
                unique_rows.append(row)
    writer = csv.DictWriter(result_file, fieldnames = unique_rows[0].keys(), extrasaction='ignore')
    writer.writeheader()
    writer.writerows(unique_rows)