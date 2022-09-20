import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        if not os.path.isfile(self.path):
            with open(self.path, 'w') as f:
                f.write('')

    def __add__(self, other):
        content = ''
        with open(self.path) as f:
            content += f.read()
        with open(other.path) as f:
            content += f.read()
        print(tempfile.gettempdir())
        new_file = File(os.path.join(tempfile.gettempdir(),
                                     os.path.splitext(os.path.basename(self.path))[0] + '_' +
                                     os.path.splitext(os.path.basename(other.path))[0] +
                                     os.path.splitext(os.path.basename(other.path))[1]))
        with open(new_file.path, 'w') as f:
            f.write(content)
        return new_file

    def __str__(self):
        return self.path

    def __getitem__(self, index):
        with open(self.path) as f:
            lines = f.readlines()
            return lines[index]

    def read(self):
        with open(self.path) as f:
            return f.read()

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
        return len(text)
