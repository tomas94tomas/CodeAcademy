def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

if __name__ == "__main__":
    count_lines("sample.txt")
