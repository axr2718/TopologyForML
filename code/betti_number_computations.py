# betti_number_computations.py

def calculate_betti_numbers_at_thresholds(persistence, thresholds):
    """ 
    Calculate Betti-0 and Betti-1 at each threshold. 
    """
    betti_0_list = []
    betti_1_list = []
    
    for threshold in thresholds:
        betti_0 = 0
        betti_1 = 0
        
        for interval in persistence:
            dimension = interval[0]
            birth, death = interval[1]
            
            # Count connected components (Betti-0)
            if dimension == 0:
                if birth <= threshold < death:
                    betti_0 += 1
            
            # Count loops (Betti-1)
            if dimension == 1:
                if birth <= threshold < death:
                    betti_1 += 1
        
        betti_0_list.append(betti_0)
        betti_1_list.append(betti_1)
    
    return betti_0_list, betti_1_list

def calculate_betti_numbers(persistence_intervals, thresholds):
    """Calculate Betti numbers at given thresholds."""
    betti_numbers = []
    for threshold in thresholds:
        betti_number = sum(1 for birth, death in persistence_intervals if birth <= threshold < death)
        betti_numbers.append(betti_number)
    return betti_numbers
