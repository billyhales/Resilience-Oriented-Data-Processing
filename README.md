# <div align='center'>  Resilience-Oriented Data: </div>
## <div align='center'>A GIS Data Production Framework for Interdependent Infrastructures </div>
#### <div align='center'> Lynn Abdouni<sup>1</sup>, Billy Hales<sup>1</sup>, Alysha Helmrich<sup>1</sup>, Mohammad Zaher Serdar<sup>2</sup>, Sajib Saha<sup>2</sup>, Eyad Masad<sup>2</sup>, Bjorn Birgisson<sup>3</sup> </div>
#### <sup>1. College of Engineering, University of Georgia, USA</sup>
#### <sup>2. College of Engineering, Hamid bin Khalifa University, Qatar</sup>
#### <sup>3. Office of Vice Provost, Nazarbayev University, Khazakhstan

## Abstract
Local and regional governments rely on Geographic Information System (GIS) datasets for asset maintenance, land-use planning, and infrastructure coordination. These datasets are produced as static geospatial layers for visualization and administration, and not always with the intention of modeling infrastructure performance under climate hazards. Increasingly frequent climate hazards are pushing public agencies toward anticipatory resilience planning, exposing limitations in how administrative geospatial datasets support modeling efforts. Resilience modeling requires attributes such as functional interdependencies, disruption thresholds, temporal updates, and elevation compatibility. Yet, these attributes are rarely encoded in conventional GIS infrastructure datasets. This paper addresses this mismatch by developing a resilience-oriented data (ROD) production framework for interdependent urban infrastructure. A synthesis of practitioner and academic transportation flood-resilience tools shows that infrastructure data frequently require specific preparation steps before analysis is possible, including hazard-to-asset linkage, topology reconstruction, directionality encoding, elevation processing, and threshold definition. Building on Rinaldi’s four infrastructure interdependency types (physical, cyber-informational, geographic, and logical), the framework translates these requirements into four operational data-production standards: semantic linkage, informational interoperability, geographic consistency, and threshold awareness. The framework is applied to a case study of preparing a national road dataset in Doha, Qatar for flood resilience modeling. The case illustrates how administrative road centerlines can become graph-ready, interoperable, and stress-responsive data for transportation resilience towards flood events. The paper contributes to resilience research and infrastructure data administration by shifting attention from downstream model preparation to upstream data production standards.  It alsooffers a transferable basis for preparing infrastructure datasets across sectors, hazards, and urban contexts.

## Contents
This GitHub repository contains code featured in the above paper, which is consistent of four scripts that were utilized during data processing, where we adapted a managed urban infrastructure datasets into a format that is conductive to study connectivity through the lens of graph theory.

Directionality Checker:
The geometry checker is a software tool that allows the user to evaluate multiple aspects of a road dataset to evaluate if the dataset is complete and is suitable for graph-theoretical operations with NetworkX (Python).
1)	Types of Geometries present in the dataset (MultiLineString, LineString).
2)	Number of records in each geometry type.
3)	Average Number of Parts for Each Geometry Type (typically 1 if LineString)
4)	Validity of All Geometries (Valid/Invalid).
5)	List of field columns and percent completeness of each field column (e.g. Figure 4.1).
<br/>
<br/>
[Geometry Checker](Scripts/geom_check.py)<br/>

One/Two Way Road Segment Processor:
[Description]<br/>
[Usage]<br/>
[link]<br/>

Anomaly Flagging/Screening:
[Description]<br/>
[Usage]<br/>
[link]<br/>

Script 4:
[Description]<br/>
[Usage]<br/>
[link]<br/>
