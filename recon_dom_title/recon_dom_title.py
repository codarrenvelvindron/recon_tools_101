#!/usr/bin/env python2
# -*- coding: utf8 -*-
#recon_dom_title is a quick
#tool thats sole purpose is to do reconaissance
#for a list of subdomains and then to
#returns the title out of the subdomains
#of a particular domain

#Usage:Make it executable first chmod +x
# ./recon_dom_title.py -d example.com
#it will then look for the list of urls from
#input_example.com.txt so all your urls must be
#in that file

#libs
import os
import sys
import os.path
import requests
import re
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import argparse

#0 Arguments
def parse_args():
    """ Script arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help='Enter domain to check')
    return parser.parse_args()

#1-Console colours
Y = '\033[93m'  # Yellow
R = '\033[91m'  # red
G = '\033[92m'  # green
W = '\033[0m'   # white

#l-LOGGING all text is written to the output file using
#keyword(text)
def info(t):
    text = t
    print (W + "[!]" + text)
    fh.write("[!]" + text + "\n")

def result(t):
    text = t
    print (R + "-->" + text)
    fh.write("-->" + text + "\n")
    
def negative(t):
    text = t
    print (R + "[-]" + text)
    fh.write("[-]" + text + "\n")

def positive(t):
    text = t
    print (G + "[+]" + text)
    fh.write("[+]" + text + "\n")

def silent(t):
    text = t
    print (Y + ">>Skipping")
    fh.write("[-]" + text + "\n")

def outtro():
    print "** Successfully scanned **"
    print "** Please see %s for full log**" % (output_filename,)
    fh.write("** Successfully scanned **")
    fh.close()    

#2-Basis for filename/checking if file exists
def input_filename_check(n):
    if os.path.isfile(n):
        positive("Input file: " + n + " was found")
        return 1
    else:
        negative("Input file: " + n + " was NOT found")
        return 0

#3-Output file creator
def output_file_init(n, m):
    info("Your output filename was created !")
    positive ("Recon_dom_title by Codarren Velvindron")
    positive ("Version 0.5")
    info ("Give me urls and I give titles!")	
    info ("Website Tested: " + m)
    #f.close()
	
#5-Url checker
def requests_retry_session(
    retries=1,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def return_titles(i, o):
    filepath = i
    num_lines = sum(1 for line in open(filepath))
    info('Scanning titles for: ' + str(num_lines) + ' urls')

    with open(filepath) as fp:
        line = fp.readlines()
        lines = [line.rstrip('\n') for line in open(filepath)]
        #urls
        cnt = 0
        for x in lines:
            t0 = time.time()
            try:
                x = "http://" + x
                info (x)
                r = requests_retry_session().get(x, timeout = 2)
                al = r.text
                try:
                    d = re.search('(?<=<title>).+?(?=</title>)', al, re.DOTALL).group().strip()
                except:
                    d = "nothing found, you should check!"
                #if d contains part of the url, it should be tagged as normal
                d = str(d)
                if name in d.lower():
                    result(d)
                else:
                    positive(d)
            except Exception as x:
                output = 'exception found, non-existant domain'
                negative(output)
            else:
                poststatus = 'It worked eventually' + str(r.status_code)
                #positive(poststatus)
            finally:
                t1 = time.time()
                timediff = t1 - t0
                #info('Took' + str(timediff) + 'seconds')


#Main function
def main():
    #Start reading file if exists or stop if not exists
    if (input_filename_check(input_filename)) == 1:
        positive("Reading input file")
		#3-Create output file to store results
        output_file_init(output_filename, mainurl)

		#4-Read input file and urls
        return_titles(input_filename, output_filename)
        
        outtro()
    else:
        negative("No file with name input_%domain%.txt")
        negative("I cannot continue")

if __name__ == "__main__":
    #0-Globals
    args = parse_args()
    if not args.domain:
        sys.exit('[!] Enter domain to check please: ./recon_dom_title.py -d "test.org"')
    if "http" in args.domain: 
        sys.exit('[!] Must be in the format: -d "example.com"')

    mainurl = args.domain
    z = mainurl.split('.')
    name = z[0]
    input_filename = "input_" + mainurl + ".txt"
    output_filename = "output_title_" + mainurl + ".txt"	
    fh = open(output_filename, "a")


    main()
