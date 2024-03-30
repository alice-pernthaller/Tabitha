import sys
from datetime import datetime

import boto3

from gui.GUI import GUI
from resources import config
from theatre.bookings import Chain
from theatre.bookings.Availability import Availability
from theatre.consumer.SectionDataParser import read_data_file
from theatre.layout.TheatreLoader import load_theatre

stage, seats = load_theatre("../resources/TestStage.csv", "../resources/TestSeats.csv")
chains = Chain.calculate_chains(seats)
today = Availability(chains, stage)

sys.stdout = open("../output/TestConversationHistory.txt", "a")
now = datetime.now()
date_time_format = "%d/%m/%Y %H:%M:%S"
print(f"Conversation information: {now.strftime(date_time_format)}")

client = boto3.client('lexv2-runtime',
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key,
                      region_name=config.region)


qualifiers = read_data_file("../resources/test_sections.dat")

main_screen = GUI(stage, seats, today, client, qualifiers)
main_screen.run()
print('\n')
