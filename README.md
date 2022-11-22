Lane-level map aided tracking (LMAT)
=====

Self-generated Lane-level map aided on-road multi-object tracking with a low-channel Roadside LiDAR sensor.
Show an demo：
1. enter <working_directory>/TrackingFunctions/mapAidedTracking/yananstreet_tracker_function. 
2. Run ShowTracker.py or ShowTrackerWithBoundingBox.py
  ``` 
  $ python ShowTrackerWithBoundingBox.py
  ``` 
3. "j": last frame, "l": next frame, "i":last 10 frame, "k": next 10 frame
### Introduction

Using a low-channel roadside LiDAR to acquire complete tracks of all objects within its scanning range plays a vital role in monitoring and managing the traffic problems. Low density appearance information and frequent occlusion make the tracking task more difficulty. To tackle the issues, we proposed a multi-object tracking algorithm under the constraint of self-generated Lane-level map, which is an association approach based on track tracing and microscopic traffic models under the constraint of lane-level map. 
```
+---Detections
|   +---angangxilu
|   +---FilteredPointCloudsForVeloviewFormat
|   |   +---angangxilu
|   |   +---xincun
|   |   +---yananstreet
|   |   +---yatai
|   +---xincun
|   +---yananstreet
|   +---yatai
\---TrackingFunctions
    +---bytetrack
    +---data
    |   +---gt
    |   +---train
    +---mapAidedTracking
    |   +---angangxilu_tracker_function
    |   +---results
    |   +---xincun_tracker_function
    |   +---yananstreet_tracker_function
    |   +---yatai_tracker_function
    +---ocsort
    |   +---output_oc
    |   +---tools
    |   +---trackers
    |   +---trackeval
    +---sort
        +---output
```


**Also see:**
Here, We have published the all labled gt and the results of LMAT. Also, we public the tracking codes and results of sites yatai steet and yan'an street, and the codes for site angangxilu and site xincun will be released in futher. 


### Dependencies:

To install required dependencies:
```
$ opencv, numpy, open3d, pickle, scipy, matplotlib, skimage, glob, filterpy, lap, motmetrics

```

### Show LMAT Demo Results:

1. enter <working_directory>/mapAidedTracking/yananstreet_tracker_function. 
2. Run ShowTracker.py or ShowTrackerWithBoundingBox.py. Note, "ShowTrackerWithBoundingBox.py" will show point cloud of detections. Thus, if run, you should download detections at Site yananstreet from ScienceDB (Data DOI:10.57760/sciencedb.02891).
  ``` 
  $ python ShowTrackerWithBoundingBox.py
  ``` 


### Main Results

run ```getClearMetricResults.py --site <site_name>``` to get clear mot metric at <site_name>

The comparison results are as follows:
  ```
                                     MOTA  IDF1   IDP   IDR  Rcll  Prcn  GT  MT  PT ML   FP   FN  IDs   FM IDt  IDa IDm
yananstreet_sort_no_optimized       33.0% 48.7% 46.0% 51.7% 83.7% 74.5% 138  96  40  2 2680 1524 2081  561   1 2058   0
yananstreet_oc_sort_no_optimized    38.3% 55.4% 52.4% 58.9% 83.7% 74.5% 138  89  44  5 2683 1527 1576  485 222 1310   9
yananstreet_byte_track_no_optimized  4.4% 40.9% 38.7% 43.4% 67.6% 60.2% 138  25 109  4 4196 3040 1726  766 232 1465  13
yananstreet_our_work                97.1% 94.7% 94.3% 95.0% 99.2% 98.4% 138 136   0  2  149   74   52   24  10   32   4

                                MOTA  IDF1   IDP   IDR  Rcll  Prcn  GT  MT  PT ML   FP   FN  IDs    FM IDt  IDa IDm
yatai_sort_no_optimized        14.1% 43.0% 39.9% 46.7% 78.1% 66.7% 436 227 206  3 6296 3525 4039  1484   6 3984   2
yatai_oc_sort_no_optimized     26.9% 51.7% 47.9% 56.2% 81.9% 69.9% 436 235 175 26 5696 2925 3167  1222 408 2666  45
yatai_byte_track_no_optimized -25.6% 28.9% 26.7% 31.3% 58.3% 49.8% 436  94 333  9 9492 6721 4038  1671 363 3633  33
yatai_our_work                 92.3% 86.7% 87.1% 86.3% 96.6% 97.5% 436 385  36 15  404  550  288   178 134  156  70

                                MOTA  IDF1   IDP   IDR  Rcll  Prcn  GT MT PT ML   FP   FN  IDs   FM IDt  IDa IDm
xincun_sort_no_optimized       42.8% 38.8% 36.4% 41.6% 85.6% 74.9% 115 89 24  2 3643 1830 1801  686   6 1782   0
xincun_oc_sort_no_optimized    45.2% 50.0% 46.9% 53.6% 83.9% 73.4% 115 66 31 18 3862 2049 1054  598  64  922   7
xincun_byte_track_no_optimized 27.1% 44.1% 41.4% 47.3% 76.3% 66.8% 115 55 56  4 4827 3014 1437  825  82 1193   9
xincun_our_work                87.8% 79.3% 79.3% 79.3% 94.3% 94.4% 115 95  8 12  708  719  129  268  41   69  10

                                    MOTA  IDF1   IDP   IDR  Rcll  Prcn  GT MT PT ML   FP   FN  IDs   FM IDt  IDa IDm
angangxilu_sort_no_optimized       42.9% 38.7% 36.4% 41.3% 84.6% 74.5% 122 86 34  2 4261 2263 1896  765  24 1783   2
angangxilu_oc_sort_no_optimized    45.0% 49.0% 46.1% 52.3% 82.9% 73.0% 122 60 47 15 4520 2522 1068  627  93  818  12
angangxilu_byte_track_no_optimized 25.5% 48.2% 45.4% 51.5% 74.9% 65.9% 122 49 70  3 5699 3701 1577  943 120 1256   9
angangxilu_our_work                66.0% 66.8% 71.9% 62.4% 77.0% 88.7% 122 76 35 11 1439 3392  175  501  94   52  33
  ```


### Run LMAT Demo:

To run the tracker with the provided detections:

0. Download the original detection dataset and put it under the folder: <working_directory>/Detections/
1. Enter <working_directory>/TrackingFunctions/. Unzip file "mapAidedTracking.rar" to the current folder.
2. Enter the working directory,  <working_directory>/TrackingFunctions/mapAidedTracking/<site_name>_tracker_function. , for example:<working_directory>/mapAidedTracking/yananstreet_tracker_function
3. Run AssociateByRemovingNoises.py, get the results in: <working_directory>/TrackingFunctions/mapAidedTracking/results/yananstreet/WithoutNoisesTracks/. 
  ```
  $ python AssociateByRemovingNoises.py
  ```
4. We can convert it to MOT formate by running  
  ``` 
  $ python ConvertToMotFormat_optimized_predict.py
  ```
5. the results is saved in: <working_directory>/TrackingFunctions/mapAidedTracking/results/yananstreet/MOTFormate/<site_name>_predict_optimized.csv 
6. In addition, the gt data is in: <working_directory>/TrackingFunctions/data/gt/<site_name>_gt.csv 



### Run SORT

The comparison results are as follows:

0. copy the detections (<site_name>_no_optimized.csv) to <working_directory>/TrackingFunctions/data/train/<site_name>/
1. rename it as det.txt
2. run sort.py in sort dirctory.
  ```
  $ python sort.py
  ```
3. get results in ocsort/output/


### Run oc-SORT

The comparison results are as follows:

0. copy the detections (<site_name>_no_optimized.csv) to <working_directory>/TrackingFunctions/data/train/<site_name>/
1. rename it as det.txt
2. run sort.py in ocsort dirctory.
  ```
  $ python track_roadside.py
  ```
3. get results in ocsort/output_oc/

### Run byteTrack

The comparison results are as follows:

0. copy the detections (<site_name>_no_optimized.csv) to <working_directory>/TrackingFunctions/data/train/<site_name>/
1. rename it as det.txt
2. run sort.py in bytetrack dirctory.
  ```
  $ python track_roadside_byte_tracker.py
  ```
3. get results in bytetrack/output_byte/ 


### About Data:

The raw detection data can be downloaded from ScienceDB (Data DOI:10.57760/sciencedb.02891)

Here, the data used for tracking is converted to MOT formate. If you want to convert it yourself, you can:  

0. Download or prepare your data, move it to <working_directory>/Detections/
1. enter corresponding working directory，for example: <working_directory>/mapAidedTracking/yananstreet_tracker_function/
2. Runenter GetCenterPoints.py can get center point information of each object, you can find it in  <working_directory>/TrackingFunctions/mapAidedTracking/results/<site_name>/lable(ori)/
  ``` 
  $ python GetCenterPoints.py  --f <total frame number>
  ```
3. SORT, oc-SORT, byteTrack is used with MOT formate data, you can convert it by:
  ``` 
  $ python GetCenterPoints_NoOptimizedSORTData.py  --f <total frame number>
  ```
4. you can find it in <working_directory>/TrackingFunctions/mapAidedTracking/results/<site_name>/SORT/<site_name>_no_optimized.csv 



### License

LMAT is released under the CC BY-SA 4.0 License (refer to the LICENSE file for details) to promote the open use of the tracker and future improvements. 
