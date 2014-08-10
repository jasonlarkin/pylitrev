import sys
import urllib2

def main_grab_citation():
  url = "http://journals.aps.org/prb/export/10.1103/PhysRevB.46.6131"
  #url = sys.argv[2]
  response = urllib2.urlopen(url)
  html = response.read()
  print html

def main_grab_citing():
  url = "http://journals.aps.org/prb/cited-by/10.1103/PhysRevB.46.6131"
  #url = sys.argv[2]
  response = urllib2.urlopen(url)
  html = response.read()
  print html



if __name__ == '__main__':
  if sys.argv[1]=='grab_citation':
    main_grab_citation()
  if sys.argv[1]=='grab_citing':
    main_grab_citing()
