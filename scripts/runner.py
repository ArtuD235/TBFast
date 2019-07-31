import os
import sys
import zipfile
from handler import get_config, update_cuts


def main():
    try:
        if sys.argv[1]:
            return sys.argv[1]
    except IndexError:
        print("Please introduce full path to the .ini file")


def geo_folder(path):
    """
    Creates two new directories to save geo files
    """
    #  Creating directories for pre and align geometry files
    geometry_directory = os.listdir(path)
    if "Aligned_geo" not in geometry_directory:
        os.system("mkdir " + path + "Align_geo")


def name_georun(geofilename, run, iterations):
    """
    Creates file name with format "_run.xml" in the end of geofilename
    """
    # Renaming gear file to use for reconstruction
    gears = []
    georun_name = geofilename.partition(".")[0] + '_' + str(run) + '.xml'
    geo_pre = georun_name.partition(".")[0] + "_pre" + ".xml"
    geo_m1 = "aligned" + '-iter1-run00' + str(run) + "_m1" + ".xml"
    geo_m2 = "aligned" + '-iter2-run00' + str(run) + "_m2" + ".xml"
    geo_m3 = "aligned" + '-iter3-run00' + str(run) + "_m3" + ".xml"
    gears.append(georun_name)
    gears.append(geo_pre)
    gears.append(geo_m1)
    gears.append(geo_m2)
    gears.append(geo_m3)
    for it in range(1, iterations+1):
        tmp = "aligned" + '-iter%s-run00' % it + str(run) + '.xml'
        gears.append(tmp)
    return gears


def run_recon(configfile, runlistfile, processor, runnumber):
    """
    Execute jobsub command
    :param configfile: path
    :param runlistfile: path
    :param processor: processor name
    :param runnumber: number
    :return:
    """
    ex_command = "jobsub -g -c " + configfile + " -csv " + runlistfile
    print(ex_command + ' ' + processor + " " + str(runnumber), '\n')
    os.system(ex_command + ' ' + processor + " " + str(runnumber))
    

def auto_cuts(ini_file, config_file, iterations, iter_num):
    init = get_config(ini_file)
    config = get_config(config_file)
    
    for key in init.options('RUNSETTINGS'):
        if key in config.options('patternRecognition'):
            update_cuts(config_file, ini_file, "RUNSETTINGS", "patternRecognition", key, iterations, iter_num)
        elif key in config.options('GBLAlign'):  # or config.options('GBLTrackFit'):
            update_cuts(config_file, ini_file, "RUNSETTINGS", "GBLAlign", key, iterations, iter_num)
            # update_cuts(config_file, ini_file, "RUNSETTINGS", "GBLTrackFit", key, iterations, iter_num)


def print_status(processor, iteration="no"):
    if iteration == "no":
        print('\n')
        print(" --------------------------------- ")
        print("                                   ")
        print(" -   Running ", processor, "      -")
        print("                                   ")
        print(" --------------------------------- ")
        print('\n')
    else:
        print('\n')
        print(" --------------------------------- ")
        print("                                   ")
        print("     Running ", processor, "       ")
        print("      iteration ", iteration, "    ")
        print(" --------------------------------- ")
        print('\n')


def readzipfile(filezip, name):
    global final
    with zipfile.ZipFile(filezip) as myzip:
        with myzip.open(name) as myfile:
            for line in myfile:
                if "THE NUMBER OF REJECTED TRACKS IS TOO LARGE." in line.decode("utf-8"):
                    final = True
                else:
                    final = False
    return final
