# Scripts
This section contains auxiliary scripts to be used in preparation for a image recognition task.
## Scraper
Contains various scripts to enable image collection from Google images as well as perform preprocessing steps on said images.
* `scrape_images.py`: The following scripts allow the user to download images of their choice by using `scrape_images.py --search <search term> --thumbnail`. The `--search <search term>` is used to define the search term. If one wish to create a model for detecting bananas, an advice would be to enter a search term for _bananas_. `--thumbail` is an optional argument. When applied, the images will be fetched with the set thumbnail sizes seen immediately when checking imagery on Google images. When this argument is not added, it will perform an extra step and open the source picture, thus fetching the image with its intended size. Depending on the purpose of the project, either of these alternatives could be desirable.
* `rename_images.py`: Renames every file in the directory to conform to the name standard _imageXX.jpg_ where XX is a number within the range of the total amount of files in the directory. Hence every name will be unique and given a number that corresponds to the actual amount of data available.
* `resize_images.py`: Resizes all images in the directory to a user specified size. As many CNN related tasks require identical sized objects, this is one way of ensuring this criteria is resolved prior to data processing. Also a requirement before label assignment when performing image classification tasks.

## Preprocessing
* `generate_tfrecord.py`: Converts the label XML files to a more usable .record file
* `partition_dataset.py`: Partitions the total amount of images and label data to a train and test folder according to a user set ratio.