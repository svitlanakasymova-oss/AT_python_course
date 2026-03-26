import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
logger = logging.getLogger("log_event")

def get_timingExbytes_incoming(file, group_number):
    tree = ET.parse(file)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(group_number):
            timingExbytes = group.find('timingExbytes')
            if timingExbytes is not None:
                incoming = timingExbytes.find('incoming')
                if incoming is not None:
                    logger.info(f"timingExbytes/incoming = {incoming.text}")
                else:
                    logger.error(f"timingExbytes/incoming not found")
            else:
                logger.info(f"timingExbytes not found")
        elif number is None:
            logger.info(f"group/number not found")


get_timingExbytes_incoming('groups.xml', 0)