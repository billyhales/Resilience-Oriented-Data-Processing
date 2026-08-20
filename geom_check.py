import os, argparse, re
import numpy as np, networkx as nx, pandas as pd, geopandas as gpd, matplotlib.pyplot as plt, osmnx as ox
from shapely.ops import transform
from shapely.geometry import LineString
import xml.etree.ElementTree as ET
import copy
import matplotlib.ticker as ticker
from argparse import RawDescriptionHelpFormatter

def multi2single(gpdf):
    singlepoly = [gpdf.loc[gpdf.geometry.type == 'LineString']]
    gpdf_multipoly = gpdf.loc[gpdf.geometry.type == 'MultiLineString']
    df_list = []

    for i, row in gpdf_multipoly.iterrows():
        if i % 10000 == 0:
            print(f'\r{i:d}/{len(gpdf):d}',end='')
        Series_geometries = pd.Series(row.geometry.geoms)
        df = pd.concat([gpd.GeoDataFrame(row).T]*len(Series_geometries), ignore_index=True)
        df['geometry']  = Series_geometries
        df_list.append(df)
    return singlepoly+df_list

parser = argparse.ArgumentParser(prog='geom_check',description=
'''
The geometry checker is a software tool that allows the user to evaluate multiple aspects of a road dataset to evaluate if the dataset is complete and is suitable for graph-theoretical operations with NetworkX (Python).
1. Types of Geometries present in the dataset (MultiLineString, LineString).
2. Number of records in each geometry type.
3. Average Number of Parts for Each Geometry Type (typically 1 if LineString)
4. Validity of All Geometries (Valid/Invalid).
List of field columns and percent completeness of each field column (e.g. Figure 4.1).
''', formatter_class=RawDescriptionHelpFormatter)

parser.add_argument('filename', help="Input filename. If GeoDataBase or geopackage, please indicate name of layer after end of colon (:).")
parser.add_argument('-r','--repair', help="Attempt to repair issues such as automatically converting geomtries that are not conductive to graph-theoretical operations to ones that are. on the data, do not fix anything. Output file will be original with the word 'edited' at the end.", action="store_true")
parser.add_argument('-o','--output', help="Output file name for report (MS Excel). If omitted, will only output summary results on-screen")
args = parser.parse_args()

input_path = args.filename

input_filedesc = os.path.split(input_path)[-1]

if input_filedesc.count(':') > 0:
    input_file, input_desc = input_filedesc.split(":")
    input_handle = gpd.read_file(input_file,layer=input_desc)
    print(len(input_handle))
else:
    input_file = input_filedesc
    input_handle = gpd.read_file(input_file)

total_len = len(input_handle)
print(f'Total Records in Dataset:\t{total_len}')
print()
geom_types = np.unique(input_handle['geometry'].geom_type).tolist()
print("Types of Geometries Present:")
print("  Geometry Type\t\tNumber of Records\tPercent of Dataset\tAverage # of Parts\tPercent Valid Parts")
for geom in geom_types:
    numparts = 0
    numrecords = 0
    for idx,feat in input_handle.loc[input_handle['geometry'].geom_type==geom].iterrows():
        if feat['geometry'].geom_type.lower().count('multi') > 0:
            numparts += len(feat['geometry'].geoms)
        else:
            numparts += 1
        numrecords+=1
    total_valid = input_handle.loc[input_handle.geom_type==geom].is_valid.astype(int).sum()
    print(f"  {geom}\t{len(input_handle.loc[input_handle['geometry'].geom_type==geom])}\t\t\t{100*len(input_handle.loc[input_handle['geometry'].geom_type==geom])/total_len:.4f}%\t\t{numparts/numrecords:.4f}\t\t\t{100*total_valid/numrecords:.4f}%")