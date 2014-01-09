## Convert csv file to Wiki page format
try:
    import tkinter as tk

except ImportError as ie:
    print('Import tkinter failed:',ie,'GUI read file won\'t work.',
          'Use open function instead' + '\n')
    filename = input('Please input filename include its path')
    file_to_read = open(filename,'r')
    savename = input('Please input the filename that you want to save, include its path')
    file_to_save = open(savename,'w')
else:
    file_to_read = tk.filedialog.askopenfile('r')
    file_to_save = tk.filedialog.asksaveasfile('w')
    

class ConvertFile:
    """ Convert csv file to Wiki page table format."""
    def __init__(self, file_to_read, file_to_save):
        """ (self, file, file) -> Nonetype
        
        """
        self.file_to_read = file_to_read
        self.file_to_write = file_to_save
        self.head = '{|class="wikitable sortable" style="color:navy;" cellpadding="10" cellspacing="0" border="1"' + '\n' * 2
        self.newcontent = ''
    def change(self):
        """ (ConvertFile) -> Nonetype
        Convert csv format to wiki table format
        """
        content = self.file_to_read
        for line in content:
##            s = content.readline()
            s = line.rstrip('\n')

            # First add '!' at the begining of every English term
            beginchar = '!'
            
            for char in s:
                if char != ",":
                    beginchar += char
                else:
                    beginchar += '\n' + '|'
            beginchar += '\n' + '|-' + '\n'
            self.newcontent = self.newcontent + beginchar
        self.newcontent = self.head + '|-' + '\n' + self.newcontent[:-2] + '}' + \
                          '\n' + '\n' + '[[category:zh]]' + '\n'

    def save(self):
        """ (ConvertFile) -> Nonetype
        Save converted string to new file file_to_save
        """
        self.file_to_write.write(self.newcontent)

    def close(self):
        self.file_to_read.close()
        self.file_to_write.close()

##    def __str__(self):
##        """ (ConvertFile) -> str
##        Return file file_to_save in string.
##        """
##        print("Do you really want to do this? Output may be very much.",end='')
##        answer = input('Yes/No?')
##        #below behavior is not right
##        if answer == 'Yes' or 'Y' or 'y':
##            return self.newcontent
##        elif answer == 'No' or 'N' or 'n':
##            return "Cancelled"

if __name__ == '__main__':
    

    newfile = ConvertFile(file_to_read, file_to_save)
    newfile.change()
    newfile.save()
    newfile.close()
