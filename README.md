# ModuleGenerator
Used to generate a module outline from a template file

This is a quick and dirty script that uses Python 3's string substitute method to automatically generate C header and source modules from templates. The script could be dramatically improved, but it is an example of how embedded software developers can leverage Python to automate common activities like creating a new header/source module. 

Using Python 3, you can create a Gpio module in the calling directory using the following command:

python Gpio

If you want the module to be placed into a directory named output then use:

python Gpio output


