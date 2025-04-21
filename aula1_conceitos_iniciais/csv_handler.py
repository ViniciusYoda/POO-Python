class CsvHandler:
    def __init__(self, directory) -> None:
        self.dir = directory

    def insert_data_in_csv(self, data):
        print(f'Inserindo {data} em {self.dir}')

    def read_data(self):
        print(f'read data in {self.dir}')

csv_handler = CsvHandler('caminho/para/o/arquivo.csv')
response = csv_handler.insert_data_in_csv('dados')
print(response)