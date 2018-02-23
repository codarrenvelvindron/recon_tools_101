#!/usr/bin/env python2
# -*- coding: utf8 -*-
#recon_dom_cleanup
#sole purpose is to do sort out urls from
#a list of subdomains and
#returns those that are currently active
#i.e. that exist and resolve

#Usage:Make it executable first chmod +x
# ./recon_dom_cleanup.py -d example.com
#it will then look for the list of urls from
#input_example.com.txt so all your urls must be
#in that file

#libs
import os
import sys
import os.path
import requests
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
def invalid(t):
    text = t
    print (R + "[-]" + text)
    #fh.write(text + "\n")

def valid(t):
    text = t
    print (G + "[+]" + text)
    fh.write(text + "\n")

def info(t):
    text = t
    print (W + "[!]" + text)
    #fh.write(text + "\n")


def outtro():
    print (G)
    print "** Successfully scanned **"
    print "** Please see %s for full log in output folder**" % (output_filename)
    #fh.write("** Successfully scanned **")
    fh.close()

#2-Basis for filename/checking if file exists
def input_filename_check(n):
    if os.path.join("./subdomains", n):
        info("Input file: " + n + " was found")
        return 1
    else:
        info("Input file: " + n + " was NOT found")
        return 0

#3-Output file creator
def output_file_init(n, m):
    print("""%s
  ^   ^   ^   ^   ^       ^   ^   ^       ^   ^   ^   ^   ^   ^   ^  
 /r\ /e\ /c\ /o\ /n\     /d\ /o\ /m\     /c\ /l\ /e\ /a\ /n\ /u\ /p\ 
<___X___X___X___X___>   <___X___X___>   <___X___X___X___X___X___X___>%s%s

                ==Codarren Velvindron== | codarren@hackers.mu
    """ % (G,Y,W))
    info ("Let me check, and invalidate urls!")
    info ("Website Tested: " + m)
    info ("Your output filename was created  !")

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

def return_valid(i, o):
    filepath = os.path.join("./subdomains", i)
    num_lines = sum(1 for line in open(filepath))
    info('Scanning validity for: ' + str(num_lines) + ' urls')
    valid_counter = 0
    invalid_counter = 0
    with open(filepath) as fp:
        line = fp.readlines()
        lines = [line.rstrip('\n') for line in open(filepath)]
        #urls
        for x in lines:
            try:
                y = "http://" + x
                info (y)
                r = requests_retry_session().get(y, timeout = 1)
                if (r.status_code == 200):
                    valid(x)
                    valid_counter += 1
                else:
                    valid(x)
                    valid_counter += 1

            except Exception as y:
                invalid(x)
                invalid_counter += 1

        info ("Valid urls: " + str(valid_counter))
        info ("Invalid urls: " + str(invalid_counter))
#Main function
def main():
    #Start reading file if exists or stop if not exists
    if (input_filename_check(input_filename)) == 1:
        info("Reading input file")
        #03-Create output file to store results
        output_file_init(output_filename, mainurl)

        #4-Read input file and urls
        return_valid(input_filename, output_filename)
        outtro()
    else:
        info ("No file with name input_%domain%.txt")
        info ("I cannot continue")

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
    output_filename = "clean_" + mainurl + ".txt"
    fn = os.path.join("./subdomains/",output_filename)
    fh = open(fn, "w")


    main()
