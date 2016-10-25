import csv, re
from pymarc import MARCReader



def getDCVariables():
    with open("/Users/rtillman/Documents/Projects/CurateBooks/PyMARC/alephrecords.mrc", "rb") as marcfile:
      reader = MARCReader(marcfile)
      for record in reader:
        dctitle = re.sub(' / ?', '', record.title())
        dctitle = dctitle.rstrip('.')
        print dctitle



getDCVariables();
