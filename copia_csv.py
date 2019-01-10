import csv

# TODO: Darle una pequeña interfaz para hacerlo más chachi

#Mensaje de bienvenida y comienza la ronda de preguntas:
archivo = input("File to read (relative path): ")
input_del = input("Read file delimiter: ")
output = input("Name of the output file: ")
out_del = input("Output file delimiter: ")
start = input("Column to start copying: ")
end = input("Last Column to copy: ")

with open(archivo) as csv_file:
    reader = csv.reader(csv_file, delimiter=input_del)
    writer = csv.writer(open(output, 'w+'), delimiter=out_del)
    for row in reader:
        writer.writerow(row[int(start):int(end)])
