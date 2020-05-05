import json
import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def run_command(command):
    command_list = command.split(' ')

    try:
        logger.info("Running shell command: \"{}\"".format(command))
        result = subprocess.run(command_list, stdout=subprocess.PIPE)
        response = format(result.stdout.decode('UTF-8'))
    except Exception as e:
        logger.error("Exception: {}".format(e))
        return False

    return response