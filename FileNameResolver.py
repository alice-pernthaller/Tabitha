import os

def get_stage_file_name():
    return os.getenv('TABITHA_STAGE')

def get_seats_file_name():
    return os.getenv('TABITHA_SEATS')

def get_areas_file_name():
    return os.getenv('TABITHA_AREAS')