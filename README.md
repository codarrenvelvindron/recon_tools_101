[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Recon Tools 101
* Recon tools 101 is made up of a number of tools specifically for reconaissance

1. Recon toolbox - combines the tools together
2. Sublist3r (By Ahmed Aboul-Ela) returns a list of subdomains
3. recon_dom_cleanup (by Codarren Velvindron) returns valid urls from a list of urls.
4. recon_dom_title (by Codarren Velvindron) from each valid url return title of the page.

and more to come soon!

## Version
1. Version 0.1 - had Sublist3r and recon_dom_title and returned all titles from all urls.
2. Version 1.1 - + recon_dom_cleanup which invalidates urls so that the result is current.

## Usage
* Clone this repository
* cd recon_tools_101
* ./setup.sh for initial setup
* Run ./recon_toolbox.sh
* Enter domain to scan
* It will first call Sublist3r
* recon_dom_cleanup then checks for valid urls
* recon_dom_title will return title for valid urls.
* All results for this specific domain
are stored in an output folder

## Author
* Codarren Velvindron (codarren@hackers.mu)
* For questions and suggestions kindly send me a mail
* or open an issue

## Donations
* Code is free and donations are always welcome.
* In case this tool helped you get a huge bounty, please
consider sparing a dollar or two to support my work :)
* Paypal account: mumandcomu@gmail.com
