# image_crawler
Code to build datasets of images for ML research. Uses Google Custom Search API to run the queries. The code is generic enough 
to build datasets from other sources. The dataset is comnposed not only by the image but also by an xml generated based on the 
metadata of the image and source where it came from.

The dataset formed is stored in a folder like this:

output_folder/
  class1/
    image1.jpg
    image1.xml
    image2.png
    image2.xml
    ...
  class2/
  class3/
  ...
