######## Multi-GPU training example #######
python train.py --name gray2color_512p --label_nc 0 --no_instance --resize_or_crop none --batchSize 8 --gpu_ids 0,1,2,3,4,5,6,7