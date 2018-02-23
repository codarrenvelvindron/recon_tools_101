#!/bin/bash
# recon_toolbox
# version 1.1
echo "Check which domain?(e.g: example.com)"
read domain
./Sublist3r/sublist3r.py -d $domain -o ./subdomains/input_$domain.txt
./recon_dom_cleanup/recon_dom_cleanup.py -d $domain
./recon_dom_title/recon_dom_title.py -d $domain
