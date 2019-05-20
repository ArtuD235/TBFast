from handler import *
from runner import *
from subprocess import call
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
eu_processors = get_configuration(inifile, "RUNSETTINGS", "reconstProcessors")
thr = get_configuration(inifile, "RUNSETTINGS", "threshold")

# Creating directories to store gear files and filepaths
geo_folder(geometry_files_path)
file_config = config_path + config_file
file_geo = geometry_files_path + basic_geo
no_debugg = False

# Checking that the confing file has the right number of patternRecognition and GBLAlign iterations
with open(file_config) as cfgfile:
    data = cfgfile.read()
    count_pattern = float(data.count("patternRecognition"))/2.
    count_gbl = float(data.count("GBLAlign"))/2.
cfgfile.close()

for run in run_list:
    # Creating runlist with gear files to be used
    gears = name_georun(basic_geo, run, iterations)
    for gear in gears:
        runlist_builder(runlist_path + runlist_file, gear, thr, beam_energy)

    # Creating directory to store gear files per run
    gears_dir = geometry_files_path + "/" + "run_%s" % run
    call("mkdir " + gears_dir, shell=True)

    # Reconstruction process begins

    # Running noisypixel, clustering and hitmaker
    run_recon(config_path + config_file, runlist_path + runlist_file, "noisypixel", run)
    run_recon(config_path + config_file, runlist_path + runlist_file, "clustering", run)
    run_recon(config_path + config_file, runlist_path + runlist_file, "hitmaker", run)

    # Running pattern recognition and GBLAlign iteration 1
    run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition1", run)
    run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign1", run)

    # Running pattern recognition and GBLAlign iteration 2
    run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition2", run)
    run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign2", run)

    # Running pattern recognition and GBLAlign iteration 3
    run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition3", run)
    run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign3", run)

    # Running pattern recognition and GBLAlign iteration 4
    run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition4", run)
    run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign4", run)

    if no_debugg:
        if count_pattern != iterations or count_gbl != iterations:
            print("The number of GBLAlig ({0}) or patternRecognition ({1}) sections in your config does not match"
                  " the number of iterations ({2})".format(count_gbl, count_pattern, iterations))
        else:
            for it in range(1, iterations + 1):
                run_recon(config_path + config_file, runlist_path + runlist_file, "patternRecognition%s" % it, run)
                run_recon(config_path + config_file, runlist_path + runlist_file, "GBLAlign%s" % it, run)

                # Checking alignment and stopping if the number of rejects is too large
                logzip = get_configuration(inifile, "PATHS", "LogPath") + "GBLAlign-00" + str(run) + ".zip"
                if readzipfile(logzip, "GBLAlign-00" + str(run) + ".log"):
                    print("Check your cuts, the alignment has crashed")
                    break
                else:
                    print("Good alignment!! continuing")


    # Popen(["ls " + input_path + "*00" + str(run) + "*"], stdout=PIPE, shell=True)




