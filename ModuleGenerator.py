import string
import os, os.path
import errno

class ModuleGenerator:
    def __init__(self, author, date, name, company, path=""):
        self.author = author
        self.date = date
        self.moduleName = name
        self.company = company
        self.outputPath = path

    def Make(self):
        self.WriteHeader()
        self.WriteSource()

    # Taken from https://stackoverflow.com/a/600612/119527
    def mkdir_p(self, path):
        if path == '':
            pass
        else:
            try:
                os.makedirs(path)
            except OSError as exc: # Python >2.5
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else: raise

    def WriteHeader(self):
        # Read in the .h template file
        with open("templates/header.htf") as inputFile:
            headerTemplate = string.Template(inputFile.read())
        inputFile.close()

        # Substitute the new strings with the template tags
        headerFile = headerTemplate.substitute( module=self.moduleName,
                                                author=self.author,
                                                date=self.date,
                                                company=self.company,
                                                fileMacro=self.moduleName.upper())

        # Write out to header file
        self.mkdir_p(self.outputPath)
        with open(self.outputPath + self.moduleName.lower() + ".h", "w") as outputFile:
            outputFile.write(headerFile)
        outputFile.close()

    def WriteSource(self):
        # Read in the .c template file
        with open("templates/source.ctf") as inputFile:
            sourceTemplate = string.Template(inputFile.read())
        inputFile.close()

        # Substitute the new strings with the template tags
        sourceFile = sourceTemplate.substitute(module=self.moduleName,
                                               author=self.author,
                                               date=self.date,
                                               company=self.company,
                                               moduleInclude=self.moduleName.lower())

        # Write out to source file
        self.mkdir_p(self.outputPath)
        with open(self.outputPath + self.moduleName.lower() + ".c", "w") as outputFile:
            outputFile.write(sourceFile)
        outputFile.close()