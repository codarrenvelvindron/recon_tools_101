echo **Making directories
mkdir -p output subdomains
echo ..done
echo **Changing permissions
chmod +x recon_toolbox.sh
echo ..done
echo **Cloning Sublist3r repository
git clone https://github.com/aboul3la/Sublist3r
echo ..done
echo **Checking os
if [ -f /etc/debian_version ]; then
    echo "Debian based distro detected"
    echo "Installing dependencies"
    echo "+Python requests"
    sudo apt-get install python-requests
    echo "+dnspython"
    sudo apt-get install python-dnspython
    echo "+argparse"
    sudo apt-get install python-argparse
elif [ -f /etc/redhat-release ]; then
    echo "Redhat based distro detected"
    echo "Installing dependencies"
    echo "+Python requests"
    sudo yum install python-requests
    echo "+dnspython"
    sudo yum install python-dns
    echo "+argparse"
    sudo pip install argparse
else
    echo "This is something else, I cannot continue, please read the manual"
fi
echo *****SETUP DONE*****
echo *****run recon_toolbox using ./recon_toolbox*****
