from Pixela.api import *
from Pixela.file_io import *
from Pixela.pixela_wrapper import *


def initialise_unit_file():
    ids = get_all_attribute("id")
    units = get_all_attribute("unit")
    account = [False] * len(units)
    data = {"id": ids, "unit": units, "account": account}
    file = File.create(UNIT_FILE, data)
    print("Created file looks like this:")
    print(file.read_file())
    return file


def update_account_graphs():
    file = File(UNIT_FILE)
    print(
        "Enter the names (space-seperated) of each graph to be held accountable for.\nThey are:")
    for id in list(file.df.index):
        print(id)
    graph_id_inputs = input("\n").split(" ")
    df = file.read_file()
    for id in graph_id_inputs:
        if id in list(df.index):
            print("yo")
            df.at[id, "account"] = True
    file.update_df(df)
    file.write_file()
    print("File updated, it now looks like this:\n")
    print(file.read_file())


if __name__ == "__main__":
    # update_account_graphs()
    # initialise_unit_file()
    update_account_graphs()
