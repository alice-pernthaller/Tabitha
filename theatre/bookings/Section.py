from theatre.bookings.Chain import Chain


def _compute_remaining_chains_after_removing_selection(selection, selection_chain):
    blocks = []  # array of arrays
    contiguous_seats = []  # array

    for seat in selection_chain.seats:
        if seat not in selection.seats:
            contiguous_seats.append(seat)
            if len(contiguous_seats) == 1:
                blocks.append(contiguous_seats)
        else:
            contiguous_seats = []

    resultant_chains = []
    for contiguous_seats in blocks:
        resultant_chains.append(Chain(contiguous_seats))

    return resultant_chains


# A section is a subsection of the theatre, containing a list of chains
class Section:
    def __init__(self, name, chains, stage):
        self.name = name
        self.chains = chains
        self.stage = stage

    def return_chains(self):
        return self.chains

    def _find_chain_containing_selection(self, selection):
        for chain in self.chains:
            if all(seat in chain.seats for seat in
                   selection.seats):
                return chain

    def _replace_original_chain_with_remaining_chains(self, old_chain, new_chains):
        self.chains.remove(old_chain)
        if len(new_chains) == 0:
            return
        if len(new_chains) == 1:
            self.chains.append(new_chains[0])
        if len(new_chains) == 2:
            for chain in new_chains:
                self.chains.append(chain)

    def remove_selection_from_availability(self, selection):
        if selection is None:
            return False
        selection_chain = self._find_chain_containing_selection(selection)
        if selection_chain is None:
            return False
        resultant_chains = _compute_remaining_chains_after_removing_selection(selection, selection_chain)
        self._replace_original_chain_with_remaining_chains(selection_chain, resultant_chains)
        return True

    def calculate_remaining_seats(self):
        number = 0
        for chain in self.chains:
            number += chain.len
        return number

    def get_max_chain_length(self):
        longest_chain_length = 0
        for chain in self.chains:
            if chain.len > longest_chain_length:
                longest_chain_length = chain.len
        return longest_chain_length
