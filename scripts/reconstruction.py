from handler import *
from runner import *
from subprocess import check_call, CalledProcessError
import sys

inifile = main()
if not inifile:
    sys.exit()


# Defining variables for paths. Please always add "/" at the end of your path
config_path = get_configuration(inifile, "PATHS", "configFilepath")
runlist_path = get_configuration(inifile, "PATHS", "runlistPath")
geometry_files_path = get_configuration(inifile, "PATHS", "geometryFilepath")

# Defining variable for files
config_file = get_configuration(inifile, "FILENAME", "configFilename")
runlist_file = get_configuration(inifile, "FILENAME", "runlistFilename")
basic_geo = get_configuration(inifile, "FILENAME", "basicGeometryFilename")

# Defining the runs for reconstruction and alignment iterations
beam_energy = get_configuration(inifile, "RUNSETTINGS", "beam_energy")
run_list = get_configuration(inifile, "RUNSETTINGS", "runList")
iterations = int(get_configuration(inifile, "RUNSETTINGS", "alignIterations"))
thr = get_configuration(inifile, "RUNSETTINGS", "threshold")

# Creating directories to store gear files and filepaths
file_config = config_path + config_file
file_geo = geometry_files_path + basic_geo
no_debugg = False

# Updating config file
up_from_ini(file_config, inifile)


# Checking that the confing file has the right number of patternRecognition and GBLAlign iterations
with open(file_config) as cfgfile:
    data = cfgfile.read()
    count_pattern = float(data.count("patternRecognition"))/2.
    count_gbl = float(data.count("GBLAlign"))/2.
cfgfile.close()

for run_number in run_list:

    # Creating runlist with gear files to be used
    gears = name_georun(basic_geo, run_number, iterations)

    # Creating directory to store gear files per run
    gears_dir = geometry_files_path + "run_%s" % run_number
    print(gears)
    try:
        check_call("mkdir " + gears_dir, shell=True)
    except CalledProcessError:
        print("\n+---------------------------------------------------------+")
        print("Directory " + "run_%s" % run_number + " already initialized")
        print("+---------------------------------------------------------+\n")

    # Creating run specific gear file
    check_call("cp " + file_geo + " " + geometry_files_path + gears[0], shell=True)

    # +-----------------------------------------------------------
    # Reconstruction process begins
    # +-----------------------------------------------------------

    # Running noisypixel, clustering and hitmaker
    if False:
        runlist_builder(runlist_path + runlist_file, gears[0], run_number, beam_energy, thr)
        run_recon(config_path + config_file, runlist_path + runlist_file, "noisypixel", run_number)
        run_recon(config_path + config_file, runlist_path + runlist_file, "clustering", run_number)
        run_recon(config_path + config_file, runlist_path + runlist_file, "hitmaker", run_number)

    # Running pattern recognition and GBLAlign iteration 1
    if False:
        runlist_builder(runlist_path + runlist_file, gears[1], run_number, beam_energy, thr)
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition1", run_number)
        run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign1", run_number)
        runlist_builder(runlist_path + runlist_file, gears[2], run_number, beam_energy, thr)
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition1", run_number)

    # Running pattern recognition and GBLAlign iteration 2
    if False:
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition2", run_number)
        run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign2", run_number)
        runlist_builder(runlist_path + runlist_file, gears[3], run_number, beam_energy, thr)
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition2", run_number)

    # Running pattern recognition and GBLAlign iteration 3
    if False:
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition3", run_number)
        run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign3", run_number)
        runlist_builder(runlist_path + runlist_file, gears[4], run_number, beam_energy, thr)
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition3", run_number)

    # Running pattern recognition and GBLAlign iteration 4
    if False:
        runlist_builder(runlist_path + runlist_file, gears[4], run_number, beam_energy, thr)
        run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition4", run_number)
        run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign4", run_number)

    no_debugg = False
    if no_debugg:
        if count_pattern != iterations or count_gbl != iterations:
            print("The number of GBLAlig ({0}) or patternRecognition ({1}) sections in your config does not match"
                  " the number of iterations ({2})".format(count_gbl, count_pattern, iterations))
        else:
            for it in range(1, iterations + 1):
                run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition%s" % it, run_number)
                run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign%s" % it, run_number)

                # Checking alignment and stopping if the number of rejects is too large
                logzip = get_configuration(inifile, "PATHS", "LogPath") + "GBLAlign-00" + str(run_number) + ".zip"
                if readzipfile(logzip, "GBLAlign-00" + str(run_number) + ".log"):
                    print("Check your cuts, the alignment has crashed")
                    break
                else:
                    print("Good alignment!! continuing")

    # Cleaning and organizing geometry directory
    organize = True
    if organize:
        try:
            check_call("rm " + geometry_files_path + gears[0], shell=True)
            for file in range(1, len(gears)+1):
                check_call("mv " + geometry_files_path + gears[file] + " " + geometry_files_path + "run_%s" % run_number + "/", shell=True)
        except CalledProcessError:
            print("")
