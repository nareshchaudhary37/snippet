**Being Human**

I am a full stack developer and I fully understand a matter when comes to export things through a Django. For some of the application have most of features are like exports pdf, csv and multiple CSVs and PDFs in zip. Lets complete this task in 15 min.


**Export CSV**


	from .zip_csv import CSVResponse
	csv_res = CSVResponse()
	csv_list = [ ["AAAA", "Naresh Chaudhary"],
                 ["AAAB", "Jay"]]
	csv_header = ["Number", "Name"]
	csv_res.add_row(csv_header)
	csv_res.add_rows(csv_list)
	return csv_res.get_response()`


**Zip with CSVs**



	from .zip_csv import ZipResponseWithCSV
	is_empty = True
	response = ZipResponseWithCSV()
    for csv_list in csv_data_list:
		if csv_list:
			is_empty = False
		 	response.create_csv_writer()
		 	response.add_row(csv_list[0].keys())
		 	response.add_rows(csv_list)
		 	response.add_csv_file("filename")
	if is_empty:
		response.close()
		return self.add_empty_response()
	return response.get_response()`

**Zip with PDFs**


	from .zip_pdf import ZipResponseWithPDF
	ip = ZipResponseWithPDF(filename="default")
	filename = "pdf"
	pdf_content = "PDF file <open a file and read>".read()
	zip.add_pdf_file(filename, pdf_content)
	zip.get_response() # just RETURN THIS`


It closes  memory object genetly. :)
