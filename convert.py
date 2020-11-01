
from yolov3.configs import *

best_val_loss = 10
total_val = 
count = 1

print(TRAIN_SAVE_CHECKPOINT)
print(TRAIN_SAVE_BEST_ONLY)
if TRAIN_SAVE_CHECKPOINT and not TRAIN_SAVE_BEST_ONLY:
    print("+++++++++++++++++++++++++++++++++")

if not TRAIN_SAVE_BEST_ONLY and not TRAIN_SAVE_CHECKPOINT:
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")

if TRAIN_SAVE_BEST_ONLY and best_val_loss>total_val/count:
    print("====================================================")