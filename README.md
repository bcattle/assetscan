assetscan
================

Recursively scans directories looking for HTML and CSS files

Usage: `scan.py [dir or file to scan]`

Sample output: 

```
Found /home/bryan/src/assetscan/splash/about.html
Found /home/bryan/src/assetscan/splash/home.html

Local assets:

<css> files
      css/jquery.modal.css
      css/skin.css
      css/splashstyle1.css
      css/video-js.css

<ico> files
      favicon.ico

<jpg> files
      images/poster2.jpg

<js> files
     js/jquery-1.9.1.min.js
     js/jquery.cycle.all.js
     js/jquery.modal.min.js
     js/jquery.videoBG.js
     js/script.js
     js/video.js
     js/wufoo.js

<png> files
      images/Favicon_large.png
      images/facebook_red.png
      images/logo_blue.png
      images/logo_blue1.png
      images/logo_blue_small.png
      images/twitter_red.png

External assets linked by url:
[u'http://fonts.googleapis.com/css?family=Titillium+Web:600',
 u'http://fonts.googleapis.com/css?family=Titillium+Web:600']
```

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
- Output coloring



