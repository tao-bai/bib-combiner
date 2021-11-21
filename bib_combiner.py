import os
import sys
import bibtexparser

from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

if __name__ == "__main__":
    bibtex_list = sys.argv[1:]
    print(bibtex_list)

    db_final = BibDatabase()
    db_final.entries = []

    bib_ids = []
    bib_total = 0
    bib_sum = 0
    duplicate_num = 0

    for bibtex in bibtex_list:
        with open(bibtex, 'r') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            for bib_dict in bib_database.entries:
                bib_total += 1
                if bib_dict['ID'] not in bib_ids:
                    bib_sum += 1
                    bib_ids.append(bib_dict['ID'])
                    db_final.entries.append(bib_dict)
                else:
                    duplicate_num += 1

    print(f'Total: {bib_total}, Duplicate:{duplicate_num}, Final:{bib_sum}')

    with open('final.bib', 'w') as bibtex_file:
        bibtexparser.dump(db_final, bibtex_file)
