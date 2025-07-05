class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        # Use 'r' as the mode
        # Use a raw string (r'...') or double backslashes for Windows path
        self.file = open(self.filepath, 'r')  

    def read_data(self):
        return self.file.read()

    def __del__(self):
        if hasattr(self, 'file') and not self.file.closed:
            self.file.close()

# Correct way to pass the file path
file_obj = FileHandler(r'C:\Users\SOOQ ELASER\OneDrive\Desktop\SE_ALX\Backend\alx_be_python\sample.txt')
print(file_obj.read_data())
