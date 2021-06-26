# learned from https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/

from csv import reader, writer
import os  

# open file in read mode
with open('list.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:

            # produce the one-row csv
            with open('list_part.csv', 'w', newline='') as write_obj:
                writer2 = writer(write_obj)
                writer2.writerow(header)
                writer2.writerow(row)

            # execute template.tex
            os.system("pdflatex template.tex")
            os.remove("list_part.csv")

            # rename
            filename = "output/cover_" + row[0] + "_" + row[1] + "_" + row[2] + ".pdf"
            os.rename(r'template.pdf',filename)
