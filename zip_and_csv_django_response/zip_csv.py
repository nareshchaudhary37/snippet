# coding=utf-8
import csv
from StringIO import StringIO
from zipfile import ZipFile

from django.http import HttpResponse
from django.core.exceptions import ValidationError


class CSV(object):
    """
    CSV class helps to write content into csv
     and make alone csv in memory.  
    """

    def add_row(self, row):
        self.writer.writerow(row)

    def add_rows(self, rows):
        for row in rows:
            self.writer.writerow(row)

    def allocate_memory(self):
        return StringIO()

    def init_csv_writer(self, response_in):
        self.writer = csv.writer(response_in)
        return self.writer


class CSVResponse(CSV):
    """
    CSVResponse returns one csv file in http response.
    """

    def __init__(self, filename="default"):
        self.__get_csv_response_object(filename)
        self.init_csv_writer(self.response)

    def __get_csv_response_object(self, filename):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = "attachment; filename={filename}.csv".format(
            filename=filename
        )
        self.response = response
        return response

    def get_response(self):
        return self.response


class ZipResponseWithCSV(CSV):
    """
    Zip Response With CSV class for return zip file response with multiple CSVs.
    NOTE: Multi threading doesn't work on with csv writer 
    (you have to change code for this. doesn't handled yet.)
    """
    filename = "default"

    def __init__(self):
        self.response = self.__get_response_object()
        self.__create()
        self.has_created_csv = False

    def __create(self):
        self.in_memory = StringIO()
        self.zip = ZipFile(self.in_memory, "a")

    def create_csv_writer(self):
        self.csv_memory = self.allocate_memory()
        self.writer = csv.writer(self.csv_memory)
        self.has_created_csv = True

    def add_csv_file(self, filename):
        if self.has_created_csv:
            self.zip.writestr(filename + '.csv', self.csv_memory.getvalue())
            # fix for Linux zip files read in Windows
            for file in self.zip.filelist:
                file.create_system = 0
            # self.csv_memory.close()
            self.has_created_csv = False
        else:
            raise ValidationError("First, You can't write before file made. \n"
                                  "You have to create writer to call create_csv_writer")

    def close(self):
        self.zip.close()

    def __memory_to_response(self):
        self.in_memory.seek(0)
        self.response.write(self.in_memory.read())

    def __get_response_object(self):
        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = "attachment; filename={filename}.zip".format(
            filename=self.filename
        )
        return response

    def get_response(self):
        self.close()
        self.__memory_to_response()
        return self.response
