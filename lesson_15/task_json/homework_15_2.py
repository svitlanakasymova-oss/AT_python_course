import json
import logging

logging.basicConfig(
            filename='json_Kasymova.log',
            level=logging.ERROR,
            format='%(asctime)s - %(message)s'
        )
logger = logging.getLogger("log_event")

def check_json(json_file):
    try:
        with open(json_file, 'r') as file:
            json.load(file)
    except json.JSONDecodeError as error:
        logger.error(f"{json_file} is not a valid json file")
    except FileNotFoundError as error:
        logger.error(f"{json_file} does not exist.")
    except Exception as error:
        logger.error(f"{json_file} - unexpected error")

check_json('localizations_en.json')
check_json('localizations_ru.json')
check_json('login.json')
check_json('swagger.json')