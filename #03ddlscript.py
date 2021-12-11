# -*- coding: utf-8 -*-
import sys

# Hauptprogramm / Main  / DNL in Githup
def main():
    print("hallo")
    if len(sys.argv) < 2:
        in_dsn = 'daten\STBPE\script\INSTALL_DB.TXT'
    else: 
        # irgendwie muss ein \ am Ende eines Strings doppelt gemacht werden
        in_dsn = 'daten\STBPE\script\\' + sys.argv[1]
    # fobj_in   = open("daten\script.txt")
    fobj_in   = open(in_dsn)
    fobj_out  = open("output.txt","w")
    directory = "daten\\"
    i = 1
    rc = init()
    for line in fobj_in:
        if line[0:2] != '--' and line.strip() != '':
            dsn = directory + line.replace("/", "\\")
            dsn = dsn.rstrip()
            print("Datei:" + dsn)
            fddl_in = open(dsn)
            for line2 in fddl_in:
                temp_changes = changes.copy()
                while temp_changes != []:
                    change = temp_changes.pop() 
                    line2 = line2.replace( change[0], change[1]) 
                if line2.strip() != '':
                    fobj_out.write("%5d" % i + ": " + line2)
                i = i + 1
            fddl_in.close()
    fobj_in.close()
    
    fobj_out.close()

def init():
    global changes
    changes = [[ '&$TCREAT' , 'T00' ] \
              ,[ '&$ICREAT' , 'I00' ] \
              ,[ '$SCHEMA$' , 'FINREP_2801' ] \
              ,[ '$VSCHEMA$' , 'FINREP_2801' ] \
              ,[ '$SCHEMAALL$' , 'FINREP_UEG' ] \
              ,[ '$TOPTION$' , ' ' ] \
              ,[ '$TABLESPACED08$' , ' ' ] \
              ,[ '$TABLESPACEI08$' , ' ' ] \
              ,[ '$TECUSER$' , 'PUBLIC' ] \
              ]

if __name__ == '__main__':
    main()    
