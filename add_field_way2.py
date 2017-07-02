# Created by Efrain Noa
# Description: This code add a new field into a existing shapefile and populate it with
#              values from a given list
# How to use:
# Input: 1) provide the folder address "path"
#        2) provide the filename "filename"
#        3) provide a list of values. This list must have same length as number of attributes (rows)
# Output: The same input file having a new field populated
# ----------------------------------------------------------------------------------------
import arcpy, sys, os, re
from arcpy import env  # import env from arcpy module

def setup_inputs():
    # Set up path and filename
    path = "E:\\thesis\\GAP_mobile3\\GAP_Copy\\GAP_analysis\\Output" # CHANGE path
    filename = "huc_1.shp" # CHANGE filename
    inputfile = os.path.join(path,filename)
    print "shapefile: ",inputfile
    
    # field name characteristics
    # field_chr = [field_name,field_type,field_precision,field_scale,field_legth,field_alias,field_is_nullable,field_is_required, field_domain]
    field_chr = ["name","TEXT","","","","","NULLABLE", "REQUIRED",""]

    # set up list of values to populate the new field (EXAMPLE 1)
    ####### list_values = [2,2,2,2,2,3,3,3,3,3]
    
    # set up list of values to populate the new field (EXAMPLE 2)
    list_values = []
    for x in xrange(1,102): #it goes from 1 to 101 (one value less than 102)
        val = "s"+str(x).zfill(3) # 'Zfill' add zeros up to reach 3 as string length
        list_values.append(val)
    #print list_values
        
    # Call function
    add_and_populate_field(inputfile,field_chr,list_values) # <---  call function

def add_and_populate_field(inputfile,field_chr,list_values):
    print "input file: ", inputfile
    print field_chr[0]
    ### Example 1: Add a blank field and populated by a list
    
    # New field called "field_chr[0]", is created
    arcpy.AddField_management(inputfile, field_chr[0],field_chr[1],field_chr[2],field_chr[3],field_chr[4],field_chr[5],field_chr[6],field_chr[7],field_chr[8])
    
    # Create a cursor on a feature class
    cursor = arcpy.UpdateCursor(inputfile)
    print "cursor: ", cursor

    # Loop through the rows in the attribute table
    counter = 0
    for row in cursor:
        print "assigning value to attribute (row) No: ", counter+1

        # Assign the values from a list to a column named 'field_chr[0]'
        row.setValue(field_chr[0], list_values[counter])
        counter += 1; ###print counter
        # Apply the change
        cursor.updateRow(row)
        # The loop will then move on to the next row/feature

    print "End assigning values to a new field function"
    
    
if __name__ == "__main__":
    print "This code add a new field into a existing shapefile"
    setup_inputs()

'''
### original
# Create a cursor on a feature class
cur = arcpy.UpdateCursor(myFeatureClass)

# Loop through the rows in the attribute table
for row in cur:
    # The variable sqMiles will get the value from the column
    # named 'Area_Miles'
    sqMiles = row.getValue('Area_Miles')
    # Calculate how many acres
    acres = (sqMiles * 640)
    # Assign the acres to a column named 'Area_Acres'
    row.setValue('Area_Acres', acres)
    # Apply the change
    cur.updateRow(row)
'''
