# Python script: having a DEM and wetlands as polygons. It calculate volume for each wetland
#                based on DEM information, considering max value for each polygon as top value.
#                volumes are stored at a new field from polygon shapefile
# How to use:
# Input: 1) DEM path and filename
#        2) polygon file (vector) that represents wetlands
#        3) path for Scratch folder "line 53"
# Output:
# ----------------------------------------------------------------------------------------
import arcpy, sys, os, numpy, re, arcgisscripting
from arcpy import env  # import env from arcpy module

#import files
import vol # import "vol" python codefile
import add_field_way2 as af2 # import "add_field_way2" python codefile
import box1

print "starting ... "
# Set up input files
# ------------------------
# Setup current address
current_filepath = sys.argv[0] ## It gets current full filename, where ever it is located
main_folder = os.path.abspath(os.path.join(current_filepath, os.pardir)) # PARENT
#main_folder = os.path.abspath(os.path.join(os.path.abspath(os.path.join(current_filepath, os.pardir)), os.pardir)) # GRAND-PARENT
###print main_folder

# setup Dem input file
# OPTION 1: by external box
name_box = "Setup DEM file"
initial_path = main_folder
full_demfilename = box1.setup_window_box(initial_path, name_box)  # <------------------- Function

# OPTION 2: by internal input                   # CHANGE THIS ADDRESS WHENEVER YOU NEED
'''full_demfilename = "D:\\hidro\\Z_JMA\\CCHHCCHH\\curva_alt_vol\\data\\dem_pj.tif" # "X:\\noayarae\\project\\dem\\dem_pj.tif" #"E:\\LowerWabash\\Indiana\\Z_indiana\\DEM"   # CHANGE
'''
# ------------------------------
# setup polygon input file
# OPTION 1: by external box
name_box = "Setup SHAPE file"
initial_path = main_folder
full_polyg_filename = box1.setup_window_box(initial_path, name_box) # <------------------- Function

# OPTION 2: by internal input                   # CHANGE THIS ADDRESS WHENEVER YOU NEED
'''full_polyg_filename = "D:\\hidro\\Z_JMA\\CCHHCCHH\\curva_alt_vol\\data\\espejo_agua2_pj.shp" #"E:\\LowerWabash\\Indna_wtlnd\\existing_wet" # CHANGE
'''

# -----------------------------------------
# make a list of attributes from a shape file
# get number of attributes
gp = arcgisscripting.create(9.3)
gp.OverWriteOutput = 1
# read rows of a shape file (Lee las lineas del shapefile para determinar cuantos poligonos (lagunas) presenta el archivo)
# SHAPEFILE MUST HAVE A FIELD NAMED "code_t" WITH POLYGON ID's (see Line 41)
rows = gp.searchcursor(full_polyg_filename)
print "line 35: ", rows 
row = rows.next()

attributes = []
while row:
    attributes.append(row.code_t) #<-- CHANGE code_t #(my_attribute) to the name of your attribute
    #print "line 41: ", attribute_types
    row = rows.next()
print "Number of polygons: ",len(attributes) #number of attributes can be obtained also by: c = arcpy.GetCount_management(full_polyg_filename)
###print "attributes: ",attributes

# iteration for each attribute (row) (ITERACION POR CADA POLIGONO) 
list_volume = []
for each_att in attributes:
    # extract ID number from the attribute
    int_val = int(re.search(r'\d+',each_att).group()) #it gets integer value from a string (string variable is each_at)
    print int_val    

    # Check if "...\\Scratch" folder does exist
    if not os.path.exists(main_folder+"\\scratch"):
        os.makedirs(main_folder + "\\scratch") # it creates a ordinary directory
    else:
        print "Line 179: The given name for the NEW directory does already exist"

    # set up output filename
    out = "out" + str(int_val).zfill(3) + ".shp" 
    out_path = main_folder + "\\scratch" #"X:\\noayarae\\project\\scratch2" #"E:\\LowerWabash\\Indna_wtlnd\\existing_wet\\scratch"
    out_fullname = os.path.join(out_path,out)
    print "out_fullname: ", out_fullname
    # extract a feature from attribute table
    att_polyg = gp.Select_analysis (full_polyg_filename, out_fullname, "\"code_t\" = '" + each_att + "'") #<-- CHANGE my_attribute to the name of your attribute
    #att_polyg = gp.Select_analysis (full_polyg_filename, out_fullname, "\"FID\" = '" + each_att + "'") #<-- CHANGE my_attribute to the name of your attribute        

    # describe extension for DEM and polygon SHP files
    descrip_dem = arcpy.Describe(full_demfilename)
    print "DEM file extension: ",descrip_dem.extent.XMin,descrip_dem.extent.YMin,descrip_dem.extent.XMax,descrip_dem.extent.YMax

    descrip_polyg = arcpy.Describe(att_polyg)
    print "SHP file extension: ",descrip_polyg.extent.XMin,descrip_polyg.extent.YMin,descrip_polyg.extent.XMax,descrip_polyg.extent.YMax

    ## Set up variables to clip
    # set up rectangle coordinates to clip
    rectangle = str(descrip_polyg.extent.XMin) + " " + str(descrip_polyg.extent.YMin) + " " + str(descrip_polyg.extent.XMax) + " " + str(descrip_polyg.extent.YMax)
    # set up the output file to save after clipping
    #>> int_val = int(re.search(r'\d+',polyg_file).group()) #it gets integer value from a string (string variable is each_at)
    out_path = main_folder + "\\scratch" #"X:\\noayarae\\project\\scratch2"#"E:\\LowerWabash\\Indna_wtlnd\\existing_wet\\Scratch" # CHANGE path
    out = "dem_p" + str(int_val).zfill(3)+".tif"; print "Line 75: ", out
    out_clipfile = os.path.join(out_path,out); print "out_clipfile: ",out_clipfile
    
    # clip polygon from the DEM (EL RASTER ES CLIPPEADO AL AREA COORESPONDIENTE A LOS POLIGONOS)
    att_raster = arcpy.Clip_management(full_demfilename,rectangle,out_clipfile,att_polyg,"#",clipping_geometry="ClippingGeometry",maintain_clipping_extent="NO_MAINTAIN_EXTENT")

    #att_raster = "E:\\LowerWabash\\Indna_wtlnd\\existing_wet\\Scratch\\dem_p002"

    # call volume function to calculate DEM's volume
    volume_value = vol.volume(att_raster)  # <-----------------  function to calculate volume
    print "volume_value: ", round(volume_value,2)
    list_volume.append(volume_value)

# call "add_and_populate_field" function
# set up input file. Polygon input file
inputfile= full_polyg_filename
# set up characteristics of new field
field_chr = ["vol1","DOUBLE","","","","","NULLABLE", "REQUIRED",""]
# set up list of volume values to populate the new field
list_values = list_volume

# call function
volume_value = af2.add_and_populate_field(inputfile,field_chr,list_values)  #  <------------ Function
