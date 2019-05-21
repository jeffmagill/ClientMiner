import os
import csv
from .hammers.http_hammer import HTTPHammer
from .hammers.mobile_hammer import MobileHammer
from .hammers.page_speed_hammer import PageSpeedHammer
from .hammers.wappalyzer_hammer import WappalyzerHammer
from .hammers.wget_hammer import WgetHammer
from .miner import Miner
from .jeweler import Jeweler

def run(target_path):
    
    print ("Opening file: ", target_path)

    #TODO huge security vulnerability here. prevent "../" for starters
    path = os.environ["MINING_BASE_PATH"] + target_path

    urls = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            urls.append(row[0])

    m = Miner()
    # m.add_hammer(HTTPHammer)
    # m.add_hammer(MobileHammer)
    m.add_hammer(PageSpeedHammer)
    # m.add_hammer(WappalyzerHammer)
#     m.add_hammer(WgetHammer)
    gems = m.hit(urls)

    print (Jeweler.polish(gems))
