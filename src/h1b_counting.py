import sys
from helper import write_output

# parse input parameters
input_file = sys.argv[1]
top_10_occupation_output_file = sys.argv[2]
top_10_state_output_file = sys.argv[3]

# code to create the two desired output text files
write_output(input_file, top_10_occupation_output_file, 'occupation')
write_output(input_file, top_10_state_output_file, 'state')


