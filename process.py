import csv, re
from pymarc import MARCReader



def getDCVariables():
    global alephIdentifier, dctitle, dctype, author, coauthor
    with open("/Users/rtillman/Documents/Projects/CurateBooks/PyMARC/alephrecords.mrc", "rb") as marcfile:
      reader = MARCReader(marcfile)
      for record in reader:
        dctype = "book"
        getAlephIdentifier(record);
        getDCTitle(record);
        getAuthor(record);
        getCoAuthor(record);
        print alephIdentifier, dctitle, author, coauthor

def getAlephIdentifier(record):
    global alephIdentifier
    alephIdentifier = str(record['001'])
    alephIdentifier = re.sub('=001\s\s', '', alephIdentifier)

def getDCTitle(record):
    global dctitle
    dctitle = re.sub(' / ?', '', record.title())
    dctitle = dctitle.rstrip('.')

def getAuthor(record):
    global author
    author = str(record.author())
    if author == "None":
        author = ''

def getCoAuthor(record):
    global coauthor
    coauthor = ''
    for person in record.get_fields('700'):
      if coauthor == '':
        coauthor += person['a']
        if person['d']:
            coauthor += " " + person['d']
        coauthor = coauthor.rstrip('.')
      else:
        coauthor += "|" + person['a']
        if person['d']:
            coauthor += " " + person['d']
        coauthor = coauthor.rstrip('.')
    for corpname in record.get_fields('710'):
      if coauthor == '':
        coauthor += corpname['a']
        if corpname['d']:
          coauthor += " " + corpname['d']
        coauthor = coauthor.rstrip('.')
      else:
        coauthor += "|" + corpname['a']
        if corpname['d']:
          coauthor += " " + corpname['d']
        coauthor = coauthor.rstrip('.')
      for meetname in record.get_fields('711'):
        if coauthor == '':
          coauthor += meetname['a']
          if meetname['d']:
            coauthor += " " + meetname['d']
          coauthor = coauthor.rstrip('.')
        else:
          coauthor += "|" + meetname['a']
          if meetname['d']:
            coauthor += " " + meetname['d']
          coauthor = coauthor.rstrip('.')


getDCVariables();
