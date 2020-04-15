import re
import csv



def processFile():
	
	with open('input.txt') as file:
		file_contents = file.read()
		getIndexes(file_contents)



def getIndexes(fileAsString):

	header_text = 'Record Information:'
	footer_text = 'To incorporate this lead into salesforce.com you can key in the data above.'

	header_indexes = [m.start() for m in re.finditer(header_text, fileAsString)];
	footer_indexes = [m.start() for m in re.finditer(footer_text, fileAsString)];

	parseFile(fileAsString, header_indexes, footer_indexes)



def parseFile(fileAsString, header_indexes, footer_indexes):

	records_as_text = []

	for i in range(len(header_indexes)):

		start = header_indexes[i] + 21 # Add 21 offset to remove "Record Information:"
		end = footer_indexes[i]

		records_as_text.append(fileAsString[start:end])

	parseRecordsAsText(records_as_text)



def parseRecordsAsText(records_as_text):

	all_records = []

	# Build arrays of the text line for each record
	for record_as_text in records_as_text:
		record_array = record_as_text.splitlines()
		record_array = [x.strip() for x in record_array] # remove the whitespace
		record_array = list(filter(None, record_array)) # remove empty entries

		# Convert to dictionary, splitting by '=' into the key-value pairs
		record_dictionary = dict(value.split(' =') for value in record_array)

		all_records.append(record_dictionary)

	buildCsvFile(all_records)



def buildCsvFile(all_records):

	headers = getHeaders(all_records)

	csv_file = 'output.csv'

	with open(csv_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=headers)
		writer.writeheader()
		for data in all_records:
			writer.writerow(data)

	print(headers)



def getHeaders(all_records):

	headers = set()

	for record in all_records:
		headers.update(record.keys())
	
	return headers	



processFile()