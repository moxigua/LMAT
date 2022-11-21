import argparse
import os
import os.path as osp
import time
import cv2
import numpy as np
import glob

from loguru import logger
from trackers.ocsort_tracker.ocsort import OCSort
from trackers.tracking_utils.timer import Timer


if __name__ == "__main__":

    

    # 读取检测结果


    if not os.path.exists('output_oc'):
        os.makedirs('output_oc')

    # 跟踪并输出结果
    frame_id = 0
    results = []
    total_time = 0.0
    total_frames = 0

    pattern = os.path.join('../data', 'train' , '*', 'det', 'det.txt')

    for seq_dets_fn in glob.glob(pattern):
        tracker = OCSort(det_thresh=0.5, iou_threshold=0.01, use_byte=True, min_hits=0)
        seq_dets = np.loadtxt(seq_dets_fn, delimiter=',')
        seq = seq_dets_fn[pattern.find('*'):].split(os.path.sep)[0]
        with open(os.path.join('output_oc', '%s.txt'%(seq)),'w') as out_file:
            print("Processing %s."%(seq))
            for frame in range(int(seq_dets[:,0].max())):
                frame += 1 #detection and frame numbers begin at 1
                dets = seq_dets[seq_dets[:, 0]==frame, 2:7]
                dets[:, 2:4] += dets[:, 0:2] #convert to [x1,y1,w,h] to [x1,y1,x2,y2]
                total_frames += 1


                start_time = time.time()

                online_targets = tracker.update(dets, [2001, 2001], [2001, 2001])


                cycle_time = time.time() - start_time
                total_time += cycle_time

                for d in online_targets:
                    print('%d,%d,%.2f,%.2f,%.2f,%.2f,1,-1,-1,-1'%(frame,d[4],d[0],d[1],d[2]-d[0]+1,d[3]-d[1]+1),file=out_file)

    print("Total Tracking took: %.3f seconds for %d frames or %.1f FPS" % (total_time, total_frames, total_frames / total_time))

        


