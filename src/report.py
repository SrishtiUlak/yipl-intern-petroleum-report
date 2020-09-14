from gettingdataFromAPI import fechPetroleumData
from creatingTables import createTable
from insertingProductData import insertProductData
from InsertingSaleData import insertSaleData
from reportGenerator import generatingReport


createTable()
reportData = fechPetroleumData()
insertProductData(reportData)
insertSaleData(reportData)
generatingReport()
