#!/usr/bin/env python
""" 
Python script to download selected files from rda.ucar.edu.
After you save the file, don't forget to make it executable
i.e. - "chmod 755 <name_of_script>"
"""
import sys, os
from urllib.request import build_opener

opener = build_opener()

filelist = [
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.1980010100_1980013123-1984070100_1984073123.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.1990020100_1990022823-1994080100_1994083123.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.2000030100_2000033123-2004090100_2004093023.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.1984080100_1984083123-1989030100_1989033123.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.1994090100_1994093023-1999040100_1999043023.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.2004100100_2004103123-2009050100_2009053123.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.1989040100_1989043023-1990010100_1990013123.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.1999050100_1999053123-2000020100_2000022923.nc.tar',
  'https://request.rda.ucar.edu/dsrqst/WANG763595/TarFiles/763595.CAPE.e5.oper.an.sfc.128_059_cape.ll025sc.2009060100_2009063023-2009120100_2009123123.nc.tar'
]

for file in filelist:
    ofile = os.path.basename(file)
    sys.stdout.write("downloading " + ofile + " ... ")
    sys.stdout.flush()
    infile = opener.open(file)
    outfile = open(ofile, "wb")
    outfile.write(infile.read())
    outfile.close()
    sys.stdout.write("done\n")
