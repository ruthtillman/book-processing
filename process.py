import csv, re
from pymarc import MARCReader



def getDCVariables():
    global alephIdentifier, dctitle, dctype, author, coauthor, alternative, isbn, subjects, issued
    with open("/Users/rtillman/Documents/Projects/CurateBooks/PyMARC/alephrecords.mrc", "rb") as marcfile:
      reader = MARCReader(marcfile)
      for record in reader:
        dctype = "book"
        getAlephIdentifier(record);
        getDCTitle(record);
        getAuthor(record);
        getCoAuthor(record);
        getAltTitle(record);
        getISBN(record);
        getSubjects(record);
        getIssued(record);
        print alephIdentifier, dctitle, issued

def getAlephIdentifier(record):
    global alephIdentifier
    alephIdentifier = str(record['001'])
    alephIdentifier = re.sub('=001\s\s', '', alephIdentifier)

def getDCTitle(record):
    global dctitle
    dctitle = re.sub(' / ?', '', record.title())
    dctitle = dctitle.rstrip('.')

def getAltTitle(record):
    global alternative
    alternative = ''
    for alt in record.get_fields('246'):
      if alternative == '':
        alternative = alt['a']
        if alt['b']:
          alternative += " " + alt['b']
        alternative = alternative.rstrip('.')
      else:
        alternative += "|" + alt['a']
        if alt['b']:
          alternative += " " + alt['b']
        alternative = alternative.rstrip('.')

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

def getISBN(record):
    global isbn
    isbn = ''
    if record.isbn():
      isbn = str(record.isbn())

def getIssued(record):
    global issued
    issued = ''
    if record.pubyear():
        issued = str(record.pubyear())
        issued = issued.rstrip('.')
        if "[" in issued:
            issued = issued.lstrip('[')
            issued = issued.rstrip(']')

def getSubjects(record):
    global subjects
    subjects = ''
    for subject in record.subjects():
      workingSub = ''
      for subfields in subject:
        workingSub += str(subfields[1])
        if re.search(r'[A-Za-z]$', workingSub):
          workingSub += '--'
        else:
          workingSub += ' '
      workingSub = workingSub.rstrip('--')
      workingSub = workingSub.rstrip(' ')
      workingSub = workingSub.rstrip('.')
      if subjects == '':
        subjects += workingSub
      else:
        subjects += '|' + workingSub

getDCVariables();
