import csv
import pandas as pd
import glob
def get_data_from_line(line):
    line = line.strip()
    #print(line)
    if line == '#':
        # We're between data sections; None will signal that
        return None 
    if ':' in line:
        # this is a "KEY=VALUE" line
        key, value = line.split(':', 1)
        #print(value)
        return {key: value}
    # if we get here, either we've missed something or there's bad data
    #raise ValueError("Couldn't parse line: {}".format(line))
def get_index_from_file(filename):
    data_dicts = []
    with open(filename) as infh:
        data_dict = {}
        for line in infh:
            update = get_data_from_line(line)
            if update is None:
                # we're between sections; add our current data to the list,
                # if we have data.
                if data_dict:
                    data_dicts.append(data_dict)
                data_dict = {}
            else:
                # this line had some data; this incorporates it into data_dict
                data_dict.update(update)
        # finally, if we don't have a section marker at the end,
        # we need to append the last section's data
        if data_dict:
            data_dicts.append(data_dict)
        return data_dicts
'''
def nestedlist2csv(list, csv_file):
    with open(csv_file, 'wb') as f:
        w = csv.writer(f)
        fieldnames=list[0].keys()  # solve the problem to automatically write the header
        print(fieldnames)
        w.writerow(fieldnames)
        for row in list:
            w.writerow(row.values())
'''
filenames = glob.glob('58457_2013*.txt')
filenames=sorted(filenames)
df=pd.DataFrame()
for filename in filenames:
    #print(filename)
    a=get_index_from_file(filename)
    outfile=pd.DataFrame(a)
    print(outfile)
    df = pd.concat([df,outfile], axis=0 )
#pd.DataFrame(data_dicts).to_csv(txt_file[0:16]+'58457.csv', index=False)
df.to_csv('58457.csv', index=False)
