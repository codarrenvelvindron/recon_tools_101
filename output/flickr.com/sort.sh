for line in `sed -n 's/.*@\([^,]*\).*/\1/p' resolve_flickr.com.txt|sort|uniq` ; do 
    echo "$line `grep -c $line resolve_flickr.com.txt`"
done
