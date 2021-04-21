import pandas as pd

def get_tables(path):
    tables = pd.read_csv(path, sep=":")
    return tables["table"][tables["to_be_loaded"]=="yes"]