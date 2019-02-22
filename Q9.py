import arcpy

#Variables
workSpace = r"C:\Users\bjholli1\Documents\Exercise3\exercise3_Q5.gdb"
fc = "Banana_Feature"
fieldName = "Amount_of_Bananas"
domainValues = {"1":"One Banana", "2":"Two Bananas", "3":"3 Bananas", "4":"4 Bananas", "5":"5 Bananas"}

#Environment Settings
arcpy.env.workspace = workSpace
arcpy.env.overwriteOutput = True

geodataBase = r"C:\Users\bjholli1\Documents\Exercise3\exercise3_Q5.gdb"

arcpy.CreateFeatureclass_management(geodataBase, fc, "POINT")

arcpy.AddField_management(fc, fieldName, "TEXT")

arcpy.CreateDomain_management(geodataBase, "BananaInput", "amount of bananas I want to eat", "TEXT", "CODED")

#All domain codes.
arcpy.AddCodedValueToDomain_management(geodataBase, "BananaInput", "1", "One Banana")
arcpy.AddCodedValueToDomain_management(geodataBase, "BananaInput", "2", "Two Bananas")
arcpy.AddCodedValueToDomain_management(geodataBase, "BananaInput", "3", "Three Bananas")
arcpy.AddCodedValueToDomain_management(geodataBase, "BananaInput", "4", "Four Bananas")
arcpy.AddCodedValueToDomain_management(geodataBase, "BananaInput", "5", "Five Bananas")

arcpy.AssignDomainToField_management(fc, fieldName, "BananaInput")
print("SUCCESS")