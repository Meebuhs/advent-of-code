from itertools import combinations
from copy import deepcopy

prime = 3145739


class State:
    """ Class to represent a state, defined by the machine layout on each floor and the position of the elevator. """
    def __init__(self, layout, elevator):
        self.layout = layout
        self.elevator = elevator
        self.cost = 0

    def __repr__(self):
        return "E: {}, {}".format(self.elevator, self.layout)

    def __eq__(self, other):
        if self.get_elevator_floor() != other.get_elevator_floor():
            return False
        if len(self.get_layout()) != len(other.get_layout()):
            return False
        for i, floor in enumerate(self.get_layout()):
            if floor != other.get_single_floor(i):
                return False
        return True

    def __hash__(self):
        return hash(str(self.layout)) + self.elevator * prime

    def get_elevator_floor(self):
        return self.elevator

    def get_layout(self):
        return deepcopy(self.layout)

    def get_single_floor(self, floor):
        return self.layout[floor]

    def get_cost(self):
        return self.cost

    def set_cost(self, value):
        self.cost = value


def construct_inital_state(lines):
    """ Takes input lines and constructs the starting state. This method requires that no two elements start with the
    same letter. """
    layout = []
    for i, line in enumerate(lines):
        floor = []
        items = line.replace(' and', ',').strip().split('contains ')[1]
        for item in items.split(', '):
            if item[:3] == 'and':
                item = item.split('and ')[1]
            if not item == 'nothing relevant.':
                item_pieces = item.split(' ')
                element = item_pieces[1][:1].upper()
                machine = item_pieces[2][:1].upper()
                floor.append("{}{}".format(element, machine))
        layout.append(set(floor))
    return State(layout, 0)


def start_search(state):
    """ Performs a breadth first search. """
    visited_states = set()
    state_queue = [state]
    goal_state = construct_goal_state(state)
    while len(state_queue) > 0:
        current_state = state_queue.pop(0)
        print(current_state)
        if current_state == goal_state:
            print(current_state.get_cost())
            break
        for state in get_reachable_states(current_state, visited_states):
            if state not in state_queue:
                state_queue.append(state)
        visited_states.add(current_state)


def construct_goal_state(initial):
    """ Uses the initial layout to construct the goal state. The goal is to have all machines on the top floor
    with the elevator. """
    final_floor = []
    goal_layout = []
    for floor in initial.get_layout():
        goal_layout.append(set())
        for machine in floor:
            final_floor.append(machine)
    goal_layout[-1] = set(final_floor)
    return State(goal_layout, len(goal_layout) - 1)


def get_reachable_states(state, visited_states):
    """ Returns a list of unvisited states which can be reached from the given state. """
    reachable_states = []
    elevator_floor = state.get_elevator_floor()
    possible_cargo = []
    for pair in combinations(state.get_single_floor(elevator_floor), 2):
        item_1, item_2 = pair[0], pair[1]
        if not (item_1[1] == 'G' and item_2[1] == 'M' and item_1[0] != item_2[0]):
            if not (item_1[1] == 'M' and item_2[1] == 'G' and item_1[0] != item_2[0]):
                possible_cargo.append([item_1, item_2])
    for item in state.get_single_floor(elevator_floor):
        possible_cargo.append([item])
    for items in possible_cargo:
        for i in [-1, 1]:
            layout = state.get_layout()
            if 0 <= elevator_floor + i < len(layout):
                new_floor = elevator_floor + i
                for item in items:
                    layout[elevator_floor].remove(item)
                    layout[new_floor].add(item)
                new_state = State(layout, new_floor)
                if new_state not in visited_states and validate_state(new_state):
                    new_state.set_cost(state.get_cost() + 1)
                    reachable_states.append(new_state)
    return reachable_states


def validate_state(state):
    """ Returns false if the given state would destroy a microchip and true otherwise. """
    for floor in state.get_layout():
        for item in floor:
            correct_generator_present = False
            incorrect_generator_present = False
            if item[1] == 'M':
                for other in floor:
                    if other[1] == 'G':
                        if other[0] == item[0]:
                            correct_generator_present = True
                        else:
                            incorrect_generator_present = True
            if incorrect_generator_present and not correct_generator_present:
                return False
    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        initial_state = construct_inital_state(f.readlines())
        start_search(initial_state)
