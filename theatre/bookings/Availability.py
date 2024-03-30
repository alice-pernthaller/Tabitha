from theatre import my_constants
from theatre.bookings.Section import Section


def _get_section_name_for_chain(chain):
    first_seat = chain.seats[0]
    section_name = first_seat.section
    return section_name


def _get_section_name_for_selection(selection):
    first_seat = selection.seats[0]
    section_name = first_seat.section
    return section_name


def _infer_distinct_section_names_from_chains(chains):
    distinct_section_names = set()
    for chain in chains:
        section_name = _get_section_name_for_chain(chain)
        distinct_section_names.add(section_name)
    return distinct_section_names


def _create_sections(distinct_section_names, chains, stage):
    chains_grouped_by_section = {}
    for section_name in distinct_section_names:
        chains_grouped_by_section[section_name] = []

    for chain in chains:
        section_name = _get_section_name_for_chain(chain)
        chains_in_named_section = chains_grouped_by_section[section_name]
        chains_in_named_section.append(chain)

    sections = {}
    for (section_name, list_of_chains) in chains_grouped_by_section.items():
        sections[section_name] = Section(section_name, list_of_chains, stage)

    return sections


def _find_best_selection(chains, query):
    best_selection = None
    for chain in chains:
        if query.party_size <= chain.len:
            selection = query.find_best_selection_in_chain(chain)
            if selection is None:
                pass
            elif best_selection is None:
                best_selection = selection
            elif selection.score < best_selection.score:
                best_selection = selection
    return best_selection


# availability contains sections which each in turn contain chains of seats
class Availability:
    def __init__(self, chains, stage):
        self.stage = stage
        distinct_section_names = _infer_distinct_section_names_from_chains(chains)
        self.sections = _create_sections(distinct_section_names, chains, stage)

    def calculate_remaining_seats(self):
        remaining_seats = 0
        for section in self.sections.values():
            remaining_seats += section.calculate_remaining_seats()
        return remaining_seats

    def _compute_combined_chains(self):
        combined_chains = []
        for section in self.sections.values():
            section_chains = section.return_chains()
            combined_chains.extend(section_chains)
        return combined_chains

    # searches each of the sections for the selection that best fits the query
    # returns a list of non-dominated selections (more expensive, lower-scoring selections are filtered out)
    def find_best_selection(self, query):

        # finds the best selection in each section (price point)
        best_selections = {}
        for section in self.sections.values():
            best_selection = _find_best_selection(section.chains, query)
            if best_selection is not None:
                best_selections[section.name] = best_selection

        # sorts the selections by price
        choice_information = []
        for section_name, selection in best_selections.items():
            choice_information.append(
                (my_constants.price_list[section_name], best_selections[section_name].score, selection,
                 my_constants.price_list[section_name],
                 my_constants.section_descriptions[section_name]))
        sorted_choices = sorted(choice_information, key=lambda choice: choice[0], reverse=True)

        # discards any selection for which there is a cheaper selection with a better score
        best_score_so_far = float('inf')
        record_of_best_score = []
        for choice in reversed(sorted_choices):
            if choice[1] < best_score_so_far:
                best_score_so_far = choice[1]
            record_of_best_score.append(best_score_so_far)
        record_of_best_score.reverse()

        non_dominated_list = []
        for i in range(len(sorted_choices)):
            if sorted_choices[i][1] <= record_of_best_score[i]:
                non_dominated_list.append(sorted_choices[i])

        previous_price = None
        choices_to_remove = []
        for choice in non_dominated_list:
            if choice[0] == previous_price:
                choices_to_remove.append(choice)
            previous_price = choice[0]

        for choice in choices_to_remove:
            non_dominated_list.remove(choice)

        return non_dominated_list

    # books the chosen seats
    def remove_selection_from_availability(self, selection):
        section_name = _get_section_name_for_selection(selection)
        section = self.sections[section_name]
        section.remove_selection_from_availability(selection)

    def get_all_chains(self):
        return self._compute_combined_chains()

    # this is used to determine approximate remaining availability
    def max_available_in_sections(self, section_names):
        max_chain_length = 0
        for section_name in section_names:
            section = self.sections[section_name]
            section_max_chain_length = section.get_max_chain_length()
            if section_max_chain_length > max_chain_length:
                max_chain_length = section_max_chain_length
        return max_chain_length
