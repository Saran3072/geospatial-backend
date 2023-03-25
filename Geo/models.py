from django.db import models
import cv2
import pandas as pd
from PIL import Image
from numpy import asarray
# Create your models here.

class geo(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=10, blank=True)
    # masked = models.ImageField(upload_to='results')
    updated = models. DateTimeField(auto_now=True)
    created = models. DateTimeField(auto_now_add=True)

    def str(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        img = Image.open(self.image)
        numpydata = asarray(img) 
        print(type(numpydata))
        print(numpydata.shape)
        # image = cv2.imread(img)
        gray = cv2.cvtColor(numpydata, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        tree_count = len(contours)

        cv2.drawContours(numpydata, contours, -1, (0, 255, 0), 2)
        # cv2_imshow(img)
        # im = Image.open(self.image)
        # im = Image.fromarray(numpydata)
        # # masked = im.open(im)
        # self.masked = im
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        print(f'Total Trees: {tree_count}')
        self.result = str(tree_count)
        print("The Trees are: ", tree_count)
        return super().save(*args, **kwargs)