'''
Write responses -- TODO: formatting
'''

def write_outfile(outfile, responses):
    with open(outfile, 'w') as f_out:
        for r in responses:
            f_out.write(r + "\n")