import pandas as pd
import os


def saveData(dataset):
    dataset = [dataset]
    # save data to xlsx using pandas with column names
    fieldnames = ["Column 1", "Column 2"]
    if os.path.exists('data.xlsx'):
        if os.stat('data.xlsx').st_size == 0:
            df = pd.DataFrame(dataset, columns=fieldnames)
            df.to_excel('data.xlsx', index=False)
        else:
            old_df = pd.read_excel('data.xlsx')
            new_df = pd.DataFrame(dataset, columns=fieldnames)
            df = pd.concat([old_df, new_df])
            df.to_excel('data.xlsx', index=False)
    else:
        df = pd.DataFrame(dataset, columns=fieldnames)
        df.to_excel('data.xlsx', index=False)
        
if __name__ == "__main__":
    saveData([1,2])
    
