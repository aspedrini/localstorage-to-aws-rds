import os

params = {"local_folder": r"C:\Users\pedri\OneDrive\Área de Trabalho\Stuff\Python\Aulas\29-06-23-basic-data\dataset"}

def rename_files(folder):

    renamed_files = []
    non_renamed_files = []

    for file in os.listdir(folder):
        if "_dataset.csv" in file:
            renamed_files.append(file)
            old_filepath = os.path.join(folder, file)
            new_name = file.split("_", 1)[1].replace("_dataset", "")
            #new_name = left_split[1].replace("_dataset", "")
            new_filepath = os.path.join(folder, new_name)
            os.rename(old_filepath, new_filepath)
        else:
            non_renamed_files.append(file)
            
    return {"Renamed files": renamed_files, "Not renamed": non_renamed_files}


if __name__ == "__main__":
    
    rename_files(folder=params["local_folder"])