from handler import *
from runner import *
import sys
from subprocess import check_call

inifile = main()
if not inifile:
    sys.exit()

config_path = get_configuration(inifile, "PATHS", "configFilepath")
configFile_name = get_configuration(inifile, "FILENAME", "configFilename")
file_config = config_path + configFile_name
run_number = get_configuration(inifile, "RUNSETTINGS", "runList")
eu_processors = ["noisypixel", "clustering", "hitmaker", "patternRecognition_tracks", "GBLTrackFit"]
runlist_path = get_configuration(inifile, "PATHS", "runlistPath")
runlistFile_name = get_configuration(inifile, "FILENAME", "runlistFilename")
geometry_files_path = get_configuration(inifile, "PATHS", "geometryFilepath")
# aligned_gear = get_configuration(inifile, "PATHS", "geometryFilepath")

# Modifying EUTel config file to run over the full data set
modify_config(file_config, "DEFAULT", "MaxRecordNumber", 150000)
modify_config(file_config, "hitmaker", "NoEvents", 1000000)
modify_config(file_config, "noisypixel", "NoOfEvents", 20000)
modify_config(file_config, "patternRecognition_tracks", "EventsAlign", 1000000)
modify_config(file_config, "patternRecognition_tracks", "EventsAlign", 1000000)
modify_config(file_config, "patternRecognition_tracks", "DUTWindow", "0.3")
modify_config(file_config, "patternRecognition_tracks", "DUTRadialWindow", "0.005")
modify_config(file_config, "patternRecognition_tracks", "DoubletCenDistCut", "0.08 0.08")
modify_config(file_config, "patternRecognition_tracks", "TripletConnectDistCut", "0.1 0.1")
modify_config(file_config, "patternRecognition_tracks", "TripletSlopeCuts", "0.01 0.01")
modify_config(file_config, "patternRecognition_tracks", "DoubletDistCut", "3 3")
modify_config(file_config, "GBLTrackFit", "r", 0.0045)
modify_config(file_config, "GBLTrackFit", "dutX", 1000)
modify_config(file_config, "GBLTrackFit", "dutY", 1000)
modify_config(file_config, "GBLTrackFit", "rFEI4X", 0.01)
modify_config(file_config, "GBLTrackFit", "rFEI4Y", 0.01)

for pro in eu_processors:
    run_recon(config_path + configFile_name, runlist_path + runlistFile_name, pro, run_number[0])

check_call("rm " + geometry_files_path + "*_pre*", shell=True)