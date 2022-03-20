 #Graph_coloring
 
 colors = ['Red', 'Green', 'Blue']

states = ['AP', 'TN', 'T', 'KAR', 'KER', 'ODI', 'MRH']

neighbors = {}
neighbors['AP'] = ['TN', 'T']
neighbors['TN'] = ['AP', 'T', 'KAR']
neighbors['T'] = ['AP', 'TN', 'KAR', 'KER', 'ODI']
neighbors['KAR'] = ['TN', 'T', 'KER']
neighbors['KER'] = ['T', 'KAR', 'ODI']
neighbors['ODI'] = ['T', 'KER']
neighbors['MRH'] = []

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states)


main()
