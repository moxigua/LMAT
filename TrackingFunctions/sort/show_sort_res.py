
import numpy as np
import cv2


file_name = 'C:/Users/moxigua/Documents/paper_test/AssociationAndTrack/sort-master/output/angangxilu.txt'


max_R = 100
Voxel_Size = 0.1


def xToGrid_c(x):
  c = int((x + 100) * 10)
  return c


def yToGrid_r(y):
  r = int((y + 100) * 10)
  return r


res_list = np.loadtxt(file_name, delimiter=',')

frame_list = res_list[:, 0]
object_id_list = res_list[:, 1]

for frame in np.unique(frame_list):
  objects = res_list[frame_list == frame, :]
  count = 0

  track_image = np.zeros((int(2 * max_R / Voxel_Size) + 1,
                            int(2 * max_R / Voxel_Size) + 1, 3), dtype=np.uint8)

  for _ in range(objects.shape[0]):

    d = objects[count]
    # row = int(yToGrid_r(d[3]))
    # column = int(xToGrid_c(d[2]))

    row = int(d[3])
    column = int(d[2])

    cv2.circle(track_image, (row, column), 10, (255, 255, 0), -1)

    cv2.putText(track_image, '{}'.format(d[1]),
                (row, column - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 255, 0),
                thickness=4)

    #
    count += 1

  cv2.imshow('track_image', cv2.resize(track_image, (0, 0), fx=0.5, fy=0.5))
  cv2.waitKey(100)
