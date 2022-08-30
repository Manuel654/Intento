from csv_reader import CsvReader

list2=[]
class TablesByRegionExporter:
    def __init__(self, data,filename):
        self.data = data
            
        self.filename=filename
    def count_tables(self):
        list_tables=[]
        list_region=[]
        list_region2=[]
        
        for i in self.data:
            list_region.append(i["Región"])
        for i in list_region:
            
            
            
            if i not in list_region2:
                list_region2.append(i)
        for i in list_region2:
            x=list_region.count(i)
            list_tables.append(x)
            list_tables.append(i)


                
        list_tables.pop(0)
        print(list_tables)
    def export(self):
    
        file = open(self.filename, "w")
        file. write("GABRIEL BORIC FONT: "+j + os.linesep)
        file. write("JOSE ANTONIO KAST RIST: "+g)
        file. close()


