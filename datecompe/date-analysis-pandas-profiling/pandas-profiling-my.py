import pandas as pd
import pandas_profiling as pdp
import os

ROOT_PATH='../date/'


def main():
    process_all(ROOT_PATH)


def process(file_path):
    if file_path.endswith('.csv'):
        pddf=pd.read_csv(file_path)
        profile=pdp.ProfileReport(pddf)
        word=file_path.strip(ROOT_PATH)+".html"
        #print("/date/"+word)
        profile.to_file("./date/"+word)
    if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        pddf=pd.read_excel(file_path)
        profile =pdp.PrpfileReport(pddf)
        word=file_path.strip(ROOT_PATH)+".html"
        profile.to_file("./date/"+word)

def process_all(path):
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
             if filename.endswith('.xls') or filename.endswith('.xlsx') or filename.endswith('.csv'):
                    process(os.path.join(pathname,filename))


if __name__=="__main__":
    main()
