import os
os.system("python ./new/train.py --data ./new/data/my_data.yaml --cfg ./new/models/yolov5s.yaml --weights ./new/pretrained/yolov5s.pt --epoch 100 --batch-size 32 --device 0,1")
# os.system("python train.py --data my_data.yaml --cfg yolov5m.yaml --weights pretrained/yolov5m.pt --epoch 100 --batch-size 4")
# os.system("python train.py --data my_data.yaml --cfg yolov5l.yaml --weights pretrained/yolov5l.pt --epoch 100 --batch-size 4")

