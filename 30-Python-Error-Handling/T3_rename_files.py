import os
import sys

def rename_txt_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            base, ext = os.path.splitext(filename)
            new_name = base + "_backup" + ext
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
            print(f"Renamed {filename} -> {new_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python T3_rename_files.py <folder_path>")
    else:
        try:
            rename_txt_files(sys.argv[1])
        except Exception as e:
            print(f"An error occurred: {e}")