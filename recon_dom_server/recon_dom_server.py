#!/usr/bin/env python2
# -*- coding: utf8 -*-
#recon_dom_server is a quick
#tool thats sole purpose is to do reconaissance
#for a list of subdomains and then to
#returns the server header out of the subdomains
#of a particular domain

#Usage:Make it executable first chmod +x
# ./recon_dom_server.py -d example.com
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
    fh.write(text + "\n")

def negative(t):
    text = t
    print (R + "[-]" + text)
    fh.write(text + "\n")

def positive(t):
    text = t
    print (G + "[+]" + text)
    fh.write(text + "\n")

def outtro():
    print (G)
    print "** Successfully scanned **"
    print "** Please see %s for full log in output folder**" % (output_filename)
    fh.close()

#2-Basis for filename/checking if file exists
def input_filename_check(n):
    if os.path.join("./subdomains", n):
        positive("Input file: " + n + " was found")
        return 1
    else:
        negative("Input file: " + n + " was NOT found")
        return 0

#3-Output file creator
def output_file_init(n, m):
    print("""%s
  ^   ^   ^   ^   ^       ^   ^   ^       ^   ^   ^   ^   ^   ^  
 /r\ /e\ /c\ /o\ /n\     /d\ /o\ /m\     /s\ /e\ /r\ /v\ /e\ /r\ 
<___X___X___X___X___>   <___X___X___>   <___X___X___X___X___X___>%s%s
         ==Codarren Velvindron== | codarren@hackers.mu
    """ % (G,Y,W))

    positive ("Version 1.0")
    info ("Give me urls and I'll check the server headers!")
    info ("Website Tested: " + m)
    info ("Your output filename was created !")
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
    filepath = os.path.join("./subdomains", i)
    num_lines = sum(1 for line in open(filepath))
    info('Scanning server headers for: ' + str(num_lines) + ' urls')

    with open(filepath) as fp:
        line = fp.readlines()
        lines = [line.rstrip('\n') for line in open(filepath)]
        #urls
        for x in lines:
            try:
                x = "http://" + x
                info (x)
                r = requests_retry_session().get(x, timeout = 2)
                al = r.headers['server']
                try:
                    d = str(al)
                    if (d is "None"):
                        negative("None")
                    else:
                        positive(d)
                except:
                    d = "None"
            except Exception as x:
                output = 'None'
                negative(output)

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
        sys.exit('[!] Enter domain to check please: ./recon_dom_server.py -d "test.org"')
    if "http" in args.domain: 
        sys.exit('[!] Must be in the format: -d "example.com"')

    mainurl = args.domain
    z = mainurl.split('.')
    name = z[0]
    input_filename = "clean_" + mainurl + ".txt"
    output_filename = "server_" + mainurl + ".txt"
    fn = os.path.join("./output/",output_filename)
    fh = open(fn, "w")


    main()
