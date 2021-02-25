from heybrochecklog.printer import Printer
import codecs
from pathlib import Path

class PrinterFile(Printer):

    def __init__(self, file_path):
        super().__init__()

        self.file_path = Path(file_path)
        self.create_file()
        self.target_resource = open(self.file_path, 'at', encoding='utf-16-le')

    def create_file(self):
        f = open(self.file_path, 'wb')
        f.write(codecs.BOM_UTF16_LE)
        f.close()

    def __del__(self):
        self.target_resource.close()