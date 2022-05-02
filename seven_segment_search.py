from collections import Counter

with open('../data/seven_segment_search') as f:
    lines = f.readlines()

output_sum = 0

#Check if all signals in comparison are also in test
def check_inside(str_test,str_compare):
    if all(char in list(str_test) for char in str_compare):
        return True

for line in lines:
    line_array = [l.split() for l in line.split('|')]
    signal_array = line_array[0]
    segment_array = line_array[1]
    
    signal_dict = {'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
    
    # Identify numbers with unique number of edges: 1,4,7,8
    for signal in signal_array:
        if len(signal) == 2:
            signal_dict['1'] = signal
        elif len(signal) == 3:
            signal_dict['7'] = signal
        elif len(signal) == 4:
            signal_dict['4'] = signal
        elif len(signal) == 7:
            signal_dict['8'] = signal
    
    corner = ''.join(set(signal_dict['4']) - set(signal_dict['1']))
    
    # To identify the remaining numbers, I use two features, each composed of two segments
    # Feature 1) the rightmost column, or the two segments that make the number one
    # Feature 2) an L-shaped "corner" piece, made up of middle segment, and top left vertical segment
    
    for signal in signal_array:
        # Identify numbers with 6 segments
        if len(signal) == 6:
            # 9 contains feature 1 and 2
            if check_inside(signal,corner) and check_inside(signal,signal_dict['1']):
                signal_dict['9'] = signal
            # 6 contains feature 2 only
            elif check_inside(signal, corner) and not check_inside(signal,signal_dict['1']):
                signal_dict['6'] = signal
            # 0 contains feature 1 only
            elif not check_inside(signal,corner) and check_inside(signal,signal_dict['1']):
                signal_dict['0'] = signal
    for signal in signal_array:
        # Now identify numbers with 5 segments
        if len(signal) == 5:
            # 2 contains neither feature 1 or 2
            if not check_inside(signal,corner) and not check_inside(signal,signal_dict['1']):
                signal_dict['2'] = signal
            # 5 includes feature 2 only
            elif check_inside(signal, corner) and not check_inside(signal,signal_dict['1']):
                signal_dict['5'] = signal
            # 3 contains feature 1 only
            elif not check_inside(signal,corner) and check_inside(signal,signal_dict['1']):
                signal_dict['3'] = signal
    
    signal_dict = {''.join(sorted(v)): k for k, v in signal_dict.items()}
    segment_array = [''.join(sorted(segment)) for segment in segment_array]
    output_sum += int(''.join([signal_dict[segment] for segment in segment_array]))

print(output_sum)
    
    