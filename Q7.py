#Set workspace and environment
import arcpy

workspace = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb"

arcpy.env.overwriteOutput = True
arcpy.env.workspace = workspace

#Set variables
gdb = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb"
fc = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\General_Offense"
fc_layer = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\Offense_Layer"
fc_export = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\Assault_Offenses"
where_clause = "'OffenseCustom' = " + "'ASSAULT'"

arcpy.MakeFeatureLayer_management(fc, fc_layer)

#Select Layer by Attribute and Export
arcpy.SelectLayerByAttribute_management(fc_layer, "NEW_SELECTION", where_clause)

arcpy.CopyFeatures_management(fc_layer, fc_export)

print("SUCCESS")