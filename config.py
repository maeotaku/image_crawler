#Google Custom Search
APIKEY = "XXXXX"
SEID = 'XXXX'
DESTINATION = r"/somepath/"

#allowed sites (if any)
WEBSITES=["eol.org","species.wikimedia.org","wikipedia.org"]

#query has [search term, class folder name, number of pages]
#1 pag = 10 imgs
#the 10 means 10 pages, # of no_pages
class_queries = [
    [r'Acnistus arborescens', "Acnistus arborescens", 10],
    [r'Aegiphila valerioi', "Aegiphila valerioi", 10],
    [r'Anacardium excelsum', "Anacardium excelsum", 10],
    [r'Annona mucosa', "Annona mucosa", 10],
    [r'Ardisia revoluta', "Ardisia revoluta", 10],
    [r'Astronium graveolens', r"Astronium graveolens", 10],
    [r'Bauhinia purpurea', "Bauhinia purpurea", 10],
    [r'Bauhinia ungulata', "Bauhinia ungulata", 10],
    [r'Blackea maurafernandesiana', "Blackea maurafernandesiana", 10],
    [r'Brosimum alicastrumo', "Brosimum alicastrum", 10],
    [r'Calophyllum brasiliense', "Calophyllum brasiliense", 10],
    [r'Calycophyllum candidissimum', r"Calycophyllum candidissimum", 10],
    [r'Cedrela odorata', r"Cedrela odorata", 10],
    [r'Cestrum tomentosumo', r"Cestrum tomentosum", 10],
    [r'Citharexylum donnell-smithii', r"Citharexylum donnell-smithii", 10],
    [r'Clusia croatii', r"Clusia croatii", 10]
]
