import json
from pathlib import Path
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import cv2
import pandas as pd

count = []
BASE_DIR = Path(__file__).resolve().parent.parent
def tree_count(path: str):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    tree_count = len(contours)

    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    count.append(tree_count)
    return count

def analysis(request):
    path = os.path.join(BASE_DIR, 'Geo/images/drone_image3')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    tree_count = len(contours)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    return tree_count

def growth(request):
    temp1 = os.path.jon(BASE_DIR, 'Geo/images/drone_image3-PhotoRoom')
    temp2 = os.path.join(BASE_DIR, 'Geo/images/drone_image3-PhotoRoom (1)')
    temp3 = os.path.join(BASE_DIR, 'Geo/images/drone_image3-PhotoRoom (4)')
    path = [temp1, temp2, temp3]
    l = tree_count
    return tree_count