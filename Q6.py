#Set workspace and environment
import arcpy

workspace = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb"

arcpy.env.overwriteOutput = True
arcpy.env.workspace = workspace

#Set variables
gdb = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb"
fc = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\CallsforService"
field_name = "Crime_Explanation"
fields_edit = ["CFSType", "Crime_Explanation"]

#Add field to feature class
arcpy.ListFields(fc)

arcpy.AddField_management(fc, field_name, "TEXT")

with arcpy.da.UpdateCursor(fc, fields_edit) as cursor:
    for row in cursor:
        if (row[0] == "Burglary Call"):
            row[1] == "This is a Burglary Call"
        else:
            row[1] == "This is NOT a Burglary Call"
        
            cursor.updateRow(row)

print("SUCCESS")