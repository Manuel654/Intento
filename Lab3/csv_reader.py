import csv
list2=[]
class CsvReader:
    def __init__(self, filename,list2):
        self.filename = filename    
        self.list2 = list2
    def read_file(self):
        list=[]
        list_info=[]
        
        with open(self.filename, newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                list_info.append(row)
        for i in list_info:
            x=(i[0].replace(';', ','))
            y=x.split(sep=',')
            list.append(y)
        
        
        for i in list:
            if len(i)==15:
                list2.append({"Nro. Región": i[0], 
                "Región": i[1],
                "Provincia": i[2],
                "Circunscripción senatorial": i[3],
                "Distrito": i[4],
                "Comuna": i[5],
                "Circunscripción electoral": i[6],
                "Local": i[7],
                "Nro. Mesa": i[8],
                "Tipo de mesa": i[9],
                "Mesas Fusionadas": i[10],
                "Electores": i[11],
                "Nro. en Voto": i[12],
                "Candidato": i[13],
                "Votos TRICEL": i[14]})
            
        
        return list2
