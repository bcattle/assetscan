assetscan
================

Recursively scans directories looking for HTML and CSS files

Usage: `scan.py [dir or file to scan]`

Output: `index.html 33: images/img/header_image.jpeg`


Dependencies
==============
[beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)


TODO 
========

Lots. 
- Understand ways to reference files from javascript
- Validate that files actually exist given a supplied static path
and url prefix
- Command line option to limit file extensions scanned
- Turn into a webapp where you can drop a file and see its output
- Plugins for common template languages
- Command line option to delete files that aren't referenced 



