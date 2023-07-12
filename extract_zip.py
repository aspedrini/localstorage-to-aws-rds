import os
from zipfile import ZipFile


params = {"local_folder": r"C:\Users\pedri\OneDrive\Área de Trabalho\Stuff\Python\Aulas\29-06-23-basic-data\dataset",
          "dataset_zip": "archive.zip"}

def extract_zip():
    try:
        with ZipFile(os.path.join(params["local_folder"], params["dataset_zip"]), "r") as zf:
            zf.extractall(params["local_folder"])
        return "'Archive.zip' extracted succesfully"
    except:
        return "Extract proccess error"
    

if __name__ == "__main__":
    
    extract_zip()