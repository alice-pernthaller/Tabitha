import random
import sys
from datetime import datetime

import boto3

import FileNameResolver
from gui.GUI import GUI
from resources import config
from simulation.Simulation import Simulation
from theatre import my_constants
from theatre.bookings import Chain
from theatre.bookings.Availability import Availability
from theatre.consumer.SectionDataParser import read_data_file
from theatre.layout.TheatreLoader import load_theatre
from theatre.layout.TheatreLoadingError import TheatreLoadingError


def print_log_file_header():
    now = datetime.now()
    date_time_format = "%d/%m/%Y %H:%M:%S"
    print(f"Conversation information: {now.strftime(date_time_format)}")


def load_data_from_files():
    stage, seats = load_theatre(FileNameResolver.get_stage_file_name(), FileNameResolver.get_seats_file_name())
    qualifiers = read_data_file(FileNameResolver.get_areas_file_name())
    return stage, seats, qualifiers


def get_chains(seats):
    chains = Chain.calculate_chains(seats)
    return chains


def get_availability(seats, stage):
    chains = get_chains(seats)
    availability = Availability(chains, stage)
    return availability


def run_simulation(availability, price_list):
    simulation = Simulation(availability, price_list)
    random_capacity = random.randrange(350, 1100)
    while simulation.availability.calculate_remaining_seats() > random_capacity:
        next(simulation)  # runs simulation until theatre is between one and three quarters full


def get_client():
    client = boto3.client('lexv2-runtime',
                          aws_access_key_id=config.aws_access_key_id,
                          aws_secret_access_key=config.aws_secret_access_key,
                          region_name=config.region)
    return client


def run_gui(stage, seats, availability, qualifiers):
    client = get_client()
    gui = GUI(stage, seats, availability, client, qualifiers)
    gui.run()


def print_log_file_footer():
    print('\n')


try:
    with open("output/ConversationHistory.txt", "a") as log_file:
        # set up the logging file
        sys.stdout = log_file
        print_log_file_header()

        # load the stage and seats from files and
        stage, seats, qualifiers = load_data_from_files()
        availability = get_availability(seats, stage)

        run_simulation(availability, my_constants.price_list)

        run_gui(stage, seats, availability, qualifiers)

        print_log_file_footer()


except TheatreLoadingError:

    print("failed to load theatre")
    print("stage file:", FileNameResolver.get_stage_file_name())
    print("seats file:", FileNameResolver.get_seats_file_name())
    print("areas file:", FileNameResolver.get_areas_file_name())

except:
    # catch-all errors
    sys.stdout = sys.__stdout__
    print("An unknown error has occurred")

finally:
    print("Goodbye, World!")
