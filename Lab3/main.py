from csv_reader import CsvReader
from general_results_exporter import GeneralResultsExporter
from tables_by_region_exporter import TablesByRegionExporter
from results_by_local_exporter import ResultsByLocalExporter
list2=[]
x = CsvReader('Laboratorios\Lab3\data.csv',list2)
x.read_file()
d=TablesByRegionExporter(x.read_file(),'tables.txt')
d.count_tables()
u=ResultsByLocalExporter(x.read_file(),'votos.txt')
u.count_local()
f=ResultsByLocalExporter(x.read_file(),'local.txt')
f.count_local()
f.export()
