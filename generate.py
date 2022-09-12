import yaml
import string
import argparse
from ModuleGenerator import ModuleGenerator
from datetime import date

def getDate():
    today = date.today()
    return today.strftime("%m/%d/%Y")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new C module from templates')

    # Required positional argument
    parser.add_argument('Name', type=str,
                        help='Module name to create')

    # Optional positional argument
    parser.add_argument('opt_outputPath', type=str, nargs='?',
                        help='An optional output path argument')

    args = parser.parse_args()

    if args.opt_outputPath is None:
        outputPath = ""
    else:
        outputPath = args.opt_outputPath + "/"

    # Get the configuration for the author and company information
    stream = open("config/config.yaml", 'r')
    config = yaml.safe_load(stream)
    author = config.get("author") 
    company = config.get("company")

    # Generate the output modules
    Module = ModuleGenerator(author, getDate(), args.Name, company, outputPath)
    Module.Make()