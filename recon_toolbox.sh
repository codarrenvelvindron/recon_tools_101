#!/usr/bin/env bash
echo "Check which domain?(e.g: example.com)"
read domain
./Sublist3r/sublist3r.py -d $domain -o ./subdomains/input_$domain.txt
./recon_dom_cleanup/recon_dom_cleanup.py -d $domain
./recon_dom_title/recon_dom_title.py -d $domain
./recon_dom_server/recon_dom_server.py -d $domain
./recon_dom_resolve/recon_dom_resolve.py -d $domain
