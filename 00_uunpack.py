import glob
import os

init = input("Pre-name: ")
list_of_files = glob.glob(os.getcwd()+'/{}*'.format(init)) # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)


input_string = input('Folder tag: ')

print('extract {:s} -C paper_{:s}'.format(latest_file, input_string))


os.system('mkdir paper_{:s}'.format(input_string))
os.system('tar -xvf {:s} -C paper_{:s}'.format(latest_file, input_string))
os.system('rm {:s}'.format(latest_file))
os.system('rm *Zone.Identifier')
