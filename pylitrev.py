import sys
import urllib2
import nltk
import re
import time

from gi.repository import Poppler, Gtk

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

def main_nltk():
  processLanguage()
  
def processLanguage():
  try:
    for item in exampleArray:
      tokenized = nltk.word_tokenize(item)
      tagged = nltk.pos_tag(tokenized)

      print tagged
      chunkGram = r"""Chunk:  {<RB\w?>*<VB\w?>*<NNP>}"""
      chunkParser = nltk.RegexpParser(chunkGram)
      chunked = chunkParser.parse(tagged)
      print chunked
      chunked.draw()

      time.sleep(555)

      
  except Exception, e:
    print str(e)

def main_readpdf():
  print 'fuck off'

def draw(widget, surface):
  page.render(surface)



if __name__ == '__main__':
  if sys.argv[1]=='grab_citation':
    main_grab_citation()
  if sys.argv[1]=='grab_citing':
    main_grab_citing()
  if sys.argv[1]=='nltk':
    exampleArray = ['The incredibly intimdating NLP scares people away who are sissies.']
    main_nltk()
  if sys.argv[1]=='readpdf':
#    main_readpdf()
    document = Poppler.Document.new_from_file("file:///home/jason/Downloads/larkin_thermal_2014.pdf", None)
    print(document.get_pdf_version_string())
  
    page = document.get_page(0)

    window = Gtk.Window(title="Hello World")
    window.connect("delete-event", Gtk.main_quit)
    window.connect("draw", draw)
    window.set_app_paintable(True)

    window.show_all()
    Gtk.main()


