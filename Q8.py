rgeaimport arcpy
import os

arcpy.env.workspace = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb"
arcpy.env.overwriteOutput = True

recordCount = arcpy.GetCount_management("CallsforService")
print("There are " + str(recordCount) + " records in the feature class 'CallsforService'.")