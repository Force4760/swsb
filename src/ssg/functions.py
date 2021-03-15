from subprocess import call
def cp_dir(source, target):
    call(['cp', '-a', source, target])

def rm(path):
    call(['rm', '-r', path])