import string

class ModuleGenerator:
    def __init__(self, author, date, name, company):
        self.author = author
        self.date = date
        self.moduleName = name
        self.company = company

    def Make(self):
        self.WriteHeader()
        self.WriteSource()

    def WriteHeader(self):
        # Read in the .h template file
        with open("templates/header.htf") as inputFile:
            headerTemplate = string.Template(inputFile.read())
        inputFile.close()

        # Substitute the new strings with the template tags, also remove last carriage return from final paramString
        headerFile = headerTemplate.substitute( module=self.moduleName,
                                                author=self.author,
                                                date=self.date,
                                                company=self.company,
                                                fileMacro=self.moduleName.upper())

        # Write out to parameters.h
        with open(self.moduleName.lower() + ".h", "w") as outputFile:
            outputFile.write(headerFile)
        outputFile.close()

    def WriteSource(self):
        # Read in the .c template file
        with open("templates/source.ctf") as inputFile:
            sourceTemplate = string.Template(inputFile.read())
        inputFile.close()

        # Substitute the new strings with the template tags, also remove last carriage return from final paramString
        sourceFile = sourceTemplate.substitute(module=self.moduleName,
                                               author=self.author,
                                               date=self.date,
                                               company=self.company,
                                               moduleInclude=self.moduleName.lower())

        # Write out to parameters.h
        with open(self.moduleName.lower() + ".c", "w") as outputFile:
            outputFile.write(sourceFile)
        outputFile.close()