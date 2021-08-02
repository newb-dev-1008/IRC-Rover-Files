from imutils import paths
# import argparse
import requests
import cv2
import os

input_path = 'C:\\Users\\Yash Umale\\Documents\\7th Sem\\IRC\\Datasets\\Creating Datasets\\urls-uturn.txt'
output_path = 'C:\\Users\\Yash Umale\\Documents\\7th Sem\\IRC\\Datasets\\Creating Datasets\\Downloaded Datasets\\U-Turn'
rows = open(input_path).read().strip().split("\n")
total = 0

# loop the URLs
for url in rows:
	try:
		# try to download the image
		r = requests.get(url, timeout=60)
		# save the image to disk
		p = os.path.sep.join([output_path, "{}.jpg".format(
			str(total).zfill(8))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()
		# update the counter
		print("[INFO] Downloaded: {}".format(p))
		total += 1
	
    # handle if any exceptions are thrown during the download process
	except:
		print("[INFO] Error downloading {}...skipping".format(p))

# loop over the image paths we just downloaded
for imagePath in paths.list_images(output_path):
	# initialize if the image should be deleted or not
	delete = False
	# try to load the image
	try:
		image = cv2.imread(imagePath)
		# if the image is `None` then we could not properly load it
		# from disk, so delete it
		if image is None:
			delete = True
	# if OpenCV cannot load the image then the image is likely
	# corrupt so we should delete it
	except:
		print("Except")
		delete = True
	# check to see if the image should be deleted
	if delete:
		print("[INFO] Deleting {}".format(imagePath))
		os.remove(imagePath)