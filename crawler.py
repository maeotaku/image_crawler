import json
import os
import uuid
import six
from six.moves.urllib.request import Request
import urllib

#pip install --upgrade google-api-python-client
from googleapiclient.discovery import build

import config as Config
from DataLayer.ClassDataSet import *
from DataLayer.Base import *
from Crawler.DataSetDumper import *

#uses custom search API
SEARCH_TYPE='image'
HEADERS={'User-Agent': 'Mozilla/5.0'}

#controls how many searches can be done
def maxim_iter(value):
    if(value>9):
        return 100
    else:
        return ((value)//1)*10

def get_new_uuid_filename():
    return str(uuid.uuid4())

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_images(all_images, total_pages, destination, folder, query_term):
    dataset = ClassDataSet(destination, all_images, folder, query_term)
    crawler = DataSetDumper(dataset)
    crawler.generate()

#find urls from google given several search page results
def retrieve_imgs_urls(query_term, total_pages):
    all_images = []
    service = build("customsearch", "v1", developerKey=Config.APIKEY)
    for page in range(1, total_pages, 10):
        print("Looking for page: "+str(page//10+1))
        res = service.cse().list(
            q=query_term,
            cx=Config.SEID,
            searchType=SEARCH_TYPE,
            fields='items,items(link)',
            start=page
        ).execute()
        if(len(res.keys())==0):
            print("*No results found*")
            break
        images=res['items']
        all_images= all_images + images
    print("All pages retrieved")
    return all_images

#recives the query_term to look for and the number of pages no_pages (from 1 to 10 as per limits of free google api access)
def crawl(query_term, folder, no_pages=1, limit=False):
    if limit:
        for i in range(len(Config.WEBSITES)-1):
            query_term=query_term+" site:"+Config.WEBSITES[i]+" OR "
        query_term=query_term+" site:"+Config.WEBSITES[len(Config.WEBSITES)-1]

    total_pages=maxim_iter(no_pages)
    all_images = retrieve_imgs_urls(query_term, total_pages)

    #dest_folder = os.path.join(, folder)
    #create_folder(dest_folder)
    download_images(all_images, total_pages, Config.DESTINATION, folder, query_term)

def crawl_queries(queries):
    for query in queries:

        #query has the format [query_term, folder, pages]
        crawl(query[0], query[1], query[2], limit=False)

crawl_queries(Config.class_queries)
