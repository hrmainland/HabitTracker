import feather
import numpy as np
import pandas as pd

STORAGE_PATH = "Pixela\local_files\\"
UNIT_FILE = STORAGE_PATH + "pixel_unit.feather"


class File:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.df = self.read_file()
        self.unit_dict = self.get_unit_dict()

    @classmethod
    def create(self, filename, data):
        pd.DataFrame(data).to_feather(filename)
        print(f"{filename} successfully created")
        return self(filename)

    def read_file(self):
        df = pd.read_feather(self.filename)
        return df.set_index("id")

    def update_df(self, df: pd.DataFrame):
        self.df = df.reset_index()

    def write_file(self):
        pd.DataFrame(self.df).to_feather(self.filename)
        print(f"{self.filename} successfully updated")

    def get_index_list(self):
        return list(self.df.index)

    def get_unit(self, id):
        return self.df.loc[id]["unit"]

    def get_unit_dict(self):
        unit_dict = {}
        for id in self.get_index_list():
            unit_dict[id] = self.get_unit(id)
        return unit_dict

    def get_row(self, row_name):
        return list(self.df[row_name])


if __name__ == "__main__":
    # data = {'admin': '15', 'job': '15', 'med': '20',
    #         'read': '5', 'track': '15', 'web': '30'}
    file = File(UNIT_FILE)
    # print(file.get_unit_dict())
    print(file.read_file())
