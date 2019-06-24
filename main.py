import bibtexparser


name_arquive = input('Insert name of archive:')

origin_name = ''.join([name_arquive, '.bib'])
destiny_name = ''.join([name_arquive, '_new.bib'])

with open(origin_name) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for entrie in bib_database.entries:
    if 'title' in entrie.keys():
        entrie['title'] = str(entrie['title']).replace('{','')
        entrie['title'] = str(entrie['title']).replace('}','')

    if 'booktitle' in entrie.keys():
        entrie['booktitle'] = str(entrie['booktitle']).replace('}','')
        entrie['booktitle'] = str(entrie['booktitle']).replace('}','')

with open(destiny_name, 'w') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)
