import arcpy

workSpace = r"C:\Users\bjholli1\Documents\Exercise3"
featureList = ["CapitalCities", "Landmarks", "HistoricPlaces", "StateNames", "Nationalities", "Rivers"]

arcpy.env.workspace = workSpace
arcpy.CreateFileGDB_management(workSpace, "exercise3_Q5")

geodataBase = r"C:\Users\bjholli1\Documents\Exercise3\exercise3_Q5.gdb"

def createFeatures(featureList):
    for feature in featureList:
        arcpy.CreateFeatureclass_management(geodataBase, str(feature))
    print("SUCCESS")

createFeatures(featureList)
