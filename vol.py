# Python script to calculate volume from a DEM file, considering maximum cellvalue as top
# How to use:
# Input: 
# Output:
# ----------------------------------------------------------------------------------------
import arcpy, sys, os, numpy, re
from arcpy import env  # import env from arcpy module

def setup_inputs():
    # Set up input files
    # set up Dem input file
    dem_path = "E:\\LowerWabash\\Indna_wtlnd\\existing_wet\\Scratch"   # CHANGE
    dem_file = "dem_p002"                                     # CHANGE
    full_demfilename = os.path.join(dem_path, dem_file)

    volume_value = volume(full_demfilename) # <---  call "volume" function
    
def volume(dem):
    print 
    print "starting volume calculation..."
    # get maximum value of raster file
    elevMAXResult = arcpy.GetRasterProperties_management(dem, "MAXIMUM")  
    elevMax = float(elevMAXResult.getOutput(0)); print "DEM max value: ",elevMax

    # Get input Raster properties
    inRas = arcpy.Raster(dem)
    lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
    cellSize = inRas.meanCellWidth
    print "lower left coordinate: ",lowerLeft
    print "DEM cell size: ",cellSize

    # Convert Raster to numpy array
    #arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0); #print arr
    arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=elevMax)
    print "Line35, arr: ", repr(arr)
    print "array size: ",arr.shape # Tamano del Raster clipeado (X,Y)
    x_ext = arr.shape[0]
    y_ext = arr.shape[1]

    # ---- Volume calculation
    # set up a list of lists having the maximum value of DEM
    list1 = []; list2 = []
    for i in range(y_ext):
        list1.append(elevMax); ###print list1
    for i in range(x_ext):
        list2.append(list1); ### print list2
    cell_area = cellSize * cellSize
    cell_volume = cell_area * (list2 - arr) # get volume for cells
    #cell_volume = cell_area * (arr - arr+1) # 
    ######print res

    # Sum of rows from "cell_volume"
    ###row_sum = [ sum(x) for x in cell_volume ] #Another way to get sum: arrSum_r = res.sum(1)
    ###print "Sum by rows: ",row_sum
    # Sum total. First rows, after columns
    sum_total = sum([ sum(x) for x in cell_volume ]) # it provides volume total
    print ("volume total: " + str(round(sum_total,2)) + " m2")
    print "end"
    return sum_total

if __name__ == "__main__":
    print "This code calculates volume of a raster file, considering max value as top value"
    list_shpfiles = setup_inputs()
    
