# Import the required Module
import tabula

# Read a PDF File
mypdf = tabula.read_pdf("[pdf directory]", pages='5')[0]

# convert PDF into CSV
tabula.convert_into("[pdf directory]", pages='all'", "output.csv", output_format="csv", pages='5')
print(df)