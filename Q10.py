#Set workspace and environment
import arcpy

workspace = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb"

arcpy.env.overwriteOutput = True
arcpy.env.workspace = workspace

#Set Variables
target_features = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\Tracts"
join_features = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\General_Offense"
out_feature_class = r"C:\Users\bjholli1\Documents\Exercise3\Downloaded_Data\Exercise_3.gdb\Exercise_3.gdb\Tracts_Offense_Join"

#Perform spatial join
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)

#Verify
print("Success")