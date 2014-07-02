import glob
import os
from slugify import slugify

filenames =  glob.glob("temp/*.pdf") + glob.glob("temp/*.PDF")
filenames.sort()

for filename in filenames:
    print "Converting: " + str(filename)
    input_filename = "'" + str(filename) +"'"
    input_filename_no_extension = filename[4:-4]
    
    # Convert file to txt
    output_filename =  "out/" + slugify(unicode(input_filename_no_extension)) + ".txt"
    os.system("pdftotext " + input_filename + " " + output_filename)
    
    # Convert file to slugified filename
    new_input_name = 'temp/' + slugify(unicode(input_filename_no_extension)) + ".pdf"
    command = "mv " +input_filename + " " + new_input_name
    #print command
    os.system(command)
    

