from theatre.layout.TheatreLoadingError import TheatreLoadingError


def _csv_to_list(values):
    value_list = values.split(',')
    return value_list


# reads text file and returns a map of section descriptions to lists of sections
# e.g. the list of sections that are 'central'
def read_data_file(filename):
    try:
        qualifier_sections = {}
        with open(filename, 'r') as data_file:
            lines = data_file.readlines()
            for line in lines:
                clean_line = line.strip()
                key, values = clean_line.split(':')
                value_list = _csv_to_list(values)
                qualifier_sections[key] = value_list
            return qualifier_sections
    except:  # error handling - raise exception if the input file is unreadable
        raise TheatreLoadingError
