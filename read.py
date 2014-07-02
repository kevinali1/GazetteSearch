import glob
import os
from slugify import slugify
import sys

def color_string_green(input_str):
    """
    Return the input sting formatted in green for TTY
    """
    # Validate input
    assert(type(input_str) == str)
    
    # Check that stdout is a tty
    if sys.stdout.isatty():
        attr = []
        attr.append('32')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), input_str)
    else:
        return input_str


def color_string_red(input_str):
    """
    Return the input sting formatted in red for TTY
    """
    # Validate input
    assert(type(input_str) == str)
    
    # Check that stdout is a tty
    if sys.stdout.isatty():
        attr = []
        attr.append('31')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), input_str)
    else:
        return input_str



def weight_string_bold(input_str):
    """
    Return the input sting formatted in bold for TTY
    """
    # Validate input
    assert(type(input_str) == str)
    
    # Check that stdout is a tty
    if sys.stdout.isatty():
        attr = []
        attr.append('1')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), input_str)
    else:
        return input_str
    
    
    

filenames = glob.glob("out/*.txt")
filenames.sort()



keywords = ['liquidiation',
            'receivership',
            'liquidate',
            'judicial management',
            'bankrupt',
            'bankruptcy',
            'liquidator',
            'winding up']



for filename in filenames:
    textfile = open(filename, "r")
    textdata = textfile.read()
    print filename
    num_hits = 0
    for keyword in keywords:
        #print keyword
        searchposition = 0
        keyword_startpoint = textdata.lower().find(keyword, searchposition)
        while keyword_startpoint != -1:
            snippetbuffer = 300
            snippet = textdata[keyword_startpoint - snippetbuffer: keyword_startpoint + snippetbuffer]
            
            print color_string_green("START SNIPPET")
            print  snippet.replace(keyword, color_string_red(keyword))
            #print keyword
            searchposition = keyword_startpoint  + 1
            keyword_startpoint = textdata.lower().find(keyword, searchposition)
            num_hits += 1
            print color_string_green("END SNIPPET")
            print "\n\n\n\n\n\n\n\n\n\n\n"
    
    print "    " + "Number of hits: " + str(num_hits)
    
        
    #print str(filename) + "    " + str(len(textdata))
    textfile.close





