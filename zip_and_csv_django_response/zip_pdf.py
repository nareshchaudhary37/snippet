# coding=utf-8
from django.http import HttpResponse

from StringIO import StringIO
from zipfile import ZipFile


class ZipResponseWithPDF(object):
    """
    Zip Response: for return zip file response with multiple PDFs.
    """

    def __init__(self, filename="invoices"):
        self.filename = filename
        self.response = self.__get_response_object()
        self.__create()

    def __create(self):
        self.in_memory = StringIO()
        self.zip = ZipFile(self.in_memory, "a")

    def add_pdf_file(self, filename, pdf_content):
        self.zip.writestr(filename + '.pdf', pdf_content)
        # fix for Linux zip files read in Windows
        for file in self.zip.filelist:
            file.create_system = 0

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