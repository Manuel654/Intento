from csv_reader import CsvReader

class ResultsByLocalExporter:
    def __init__(self, data,filename):
        self.data=data
        self.filename=filename
    def count_local(self):
    
        list_local=[]
        list_local2=[]
        list_count_local=[]
    
        for i in self.data:
            list_local.append(i["Local"])
        for i in list_region:
            
            
            
            if i not in list_region2:
                list_local2.append(i)
        for i in list_region2:
            x=list_region.count(i)
            list_tables.append(x)
            list_count_local.append(i)
        return list_count_local
    def export(self):
    
        file = open(self.filename, "w")
        file. write("GABRIEL BORIC FONT: "+j + os.linesep)
        file. write("JOSE ANTONIO KAST RIST: "+g)
        file. close()
