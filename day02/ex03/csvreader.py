class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.has_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.fields = 0

    def __enter__(self):
        self.file = open(self.filename, 'r')
        if self.has_header:
            self.header = self.file.readline().split(self.sep)
            self.fields = len(self.header)
        lines = self.file.readlines()
        self.data = []
        for line in lines[self.skip_top: len(lines) - self.skip_bottom]:
            line = line.replace("\n", '')
            row = [d.replace(' ', '') for d in line.split(self.sep)]
            if self.fields == 0:
                self.fields = len(row)
            if len(row) != self.fields or any(len(d) == 0 for d in row):
                return None
            self.data.append(row)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        if self.has_header:
            return self.header
        return None


if __name__ == '__main__':
    with CsvReader('good.csv') as csv:
        data = csv.getdata()
        header = csv.getheader()
        print(data, header)

    with CsvReader('bad.csv') as csv:
        if csv is None:
            print("File is corrupted")
