import glob
import os
from slugify import slugify

filenames = glob.glob("temp/*.pdf")
filenames.sort()

for filename in filenames:
    print "Converting: " + str(filename)
    input_filename = "'" + str(filename) +"'"
    output_filename =  "out/" + slugify(unicode(filename)) + ".txt"
    layoutoption = ""
    #os.system("pdftotext -layout " + input_filename + " " + output_filename)
    os.system("pdftotext " + input_filename + " " + output_filename)
