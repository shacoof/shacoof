
from datetime import datetime
import csv


def createCSV(filename,list):   
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for r in list:
            print(r)
            writer.writerow(r)


def debug_print(app_logger, str):
    app_logger.debug(datetime.now().ctime() + " :: " + str) 
    print(str)
    return str+'<br>'

def to_object(item):
    """
    usage : 
        
    Convert a dictionary to an object (recursive).
    """
    def convert(item): 
        if isinstance(item, dict):
            return type('jo', (), {k: convert(v) for k, v in item.items()})
        if isinstance(item, list):
            def yield_convert(item):
                for index, value in enumerate(item):
                    yield convert(value)
            return list(yield_convert(item))
        else:
            return item

    return convert(item)






