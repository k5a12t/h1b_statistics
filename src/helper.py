# function to get the column number corresponding to
# application status
def get_status_col_num(file):
    f = open(file)
    header = f.readline()
    cols = header.split(';')
    cols = [item.strip() for item in cols]
    f.close()
    try:
        num = cols.index('CASE_STATUS')
    except:
        num = cols.index('STATUS')
    return(num)

# function to get the column number corresponding to
# occupation name
def get_occupation_col_num(file):
    f = open(file)
    header = f.readline()
    cols = header.split(';')
    cols = [item.strip() for item in cols]
    f.close()
    try:
        num = cols.index('SOC_NAME')
    except:
        num = cols.index('LCA_CASE_SOC_NAME')
    return(num)

# function to get the column number corresponding to
# worksite state
def get_state_col_num(file):
    f = open(file)
    header = f.readline()
    cols = header.split(';')
    cols = [item.strip() for item in cols]
    f.close()
    try:
        num = cols.index('WORKSITE_STATE')
    except:
        num = cols.index('LCA_CASE_WORKLOC1_STATE')
    return(num)


# function to get total number of certified applications
def get_total_certified(file):
    col_num = get_status_col_num(file)
    num = 0
    f = open(file)
    for line in f:
        if line.split(';')[col_num].strip() == 'CERTIFIED':
            num = num + 1
    f.close()
    return(num)


# function to get the counts of certified applications for
# all possible values of a variable of interest
def get_counts(file, variable):
    f = open(file)
    col_name = ''
    if variable == 'occupation':
        variable_col_num = get_occupation_col_num(file)
    elif variable == 'state':
        variable_col_num = get_state_col_num(file)
    else:
        sys.exit('The specified variable is unknown. Permitted options are "occupation" or "state".')
    status_col_num = get_status_col_num(file)
    counts = dict()
    for line in f:
        if line.split(';')[status_col_num].strip() == 'CERTIFIED':
            if line.split(';')[variable_col_num].strip() in counts:
                counts[line.split(';')[variable_col_num].strip()] = counts[line.split(';')[variable_col_num].strip()] + 1
            else:
                counts[line.split(';')[variable_col_num].strip()] = 1
    counts = sorted(counts.items(), key = lambda x: (-x[1], x[0].strip('"')))
    f.close()
    return(counts)


# function to write the output file
def write_output(infile, outputfile, variable):
    counts = get_counts(infile, variable)
    # restrict to 10 lines
    counts = counts[0:10]
    total = get_total_certified(infile)
    f = open(outputfile, 'w')
    if variable == 'occupation':
        f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    elif variable == 'state':
        f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for item in counts:
        f.write("%s;%d;%.1f%%" % (item[0].strip('"'), item[1], item[1]*100/total))
        f.write('\n')
    f.close()
