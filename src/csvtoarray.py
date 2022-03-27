import csv

# raceline data obtained from https://github.com/TUMFTM/racetrack-database

if __name__ == '__main__':
    with open('racelines/Austin.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        array = []

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                array.append([float(row[0]), float(row[1])])
                line_count += 1
        print(array)