from csv_reader import CsvReader

list2=[]
class GeneralResultsExporter:
    def __init__(self, data,filename):
        self.data=data
        self.list2=list2
        self.filename = filename
    def count_votes(self):
        list_candidates=[]
        j=0
        g=0
        for i in self.data:
            list_candidates.append(i["Candidato"])
        j=list_candidates.count('GABRIEL BORIC FONT')
        g=list_candidates.count('JOSE ANTONIO KAST RIST')
        print('GABRIEL BORIC FONT: ',j,' \ JOSE ANTONIO KAST RIST: ',g)
        return j,g
    def export(self):

        file = open(self.filename, "w")
        file. write("GABRIEL BORIC FONT: "+j + os.linesep)
        file. write("JOSE ANTONIO KAST RIST: "+g)
        file. close()
        



            