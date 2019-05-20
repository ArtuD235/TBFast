import configparser
import os
import glob


def create_config(path):
    """
    Creating "standard"config file
    :param path: address to config file
    :return: config file
    """
    #  Creating configparser object = config_file
    config = configparser.ConfigParser(allow_no_value=True)
    config.optionxform = str                    # Allowing to parse strings keeping the format
    
    #
    config["DEFAULT"] = {'BasePath': '/afs/cern.ch/user/r/rodrigar/workspace/TBFast/R0strip/',
                         "NativePath": "/afs/cern.ch/user/r/rodrigar/workspace/LCIO_files",
                         "TemplatePath": "%(BasePath)s/steering",
                         "GearFile": "@GearGeoFile@",
                         "GearFilePath": "%(BasePath)s/geometry",
                         "HistoInfoFile": "%(TemplatePath)s/histoinfo.xml",
                         "FilePrefix": "run@RunNumber@",
                         "SkipNEvents": "0",
                         "DatabasePath": "/afs/cern.ch/user/r/rodrigar/workspace/TBFast/output/database",
                         "HistogramPath": "/afs/cern.ch/user/r/rodrigar/workspace/TBFast/output/histograms",
                         "LcioPath": "/afs/cern.ch/user/r/rodrigar/workspace/TBFast/output/lcio",
                         "LogPath": "/afs/cern.ch/user/r/rodrigar/workspace/TBFast/output/logs",
                         "ROOT_OUT_PATH": "/afs/cern.ch/user/r/rodrigar/workspace/TBFast/output/root",
                         "MaxRecordNumber": "25000",
                         "Verbosity": "MESSAGE5",
                         "NEventsMessage": "1000"
                         }
    
    config["noisypixel"] = {"NoOfEvents": "10000",
                            "M26SensorVec": "0 1 2 3 4 5",
                            "FiringFreqCutM26": "0.002",
                            "APIXSensorVec": "7",
                            "FiringFreqCutAPIX": "0.001",
                            "StripVec": "10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33",
                            "FiringFreqCutStrip": "0.5",
                            "StripXindexRangeOffset": "256",
                            }
    
    config["clustering"] = {}
    
    config["hitmaker"] = {"localDistDUT": "0 0",
                          "NoEvents": "10000",
                          "ResidualsXMax": "5. 5.  5. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. "
                                           "100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 10. 10. 100. 10.",
                          "ResidualsXMin": "-5. -5. -5. -100. -100. -100. -100. -100. -100. -100. -100. -100. -100. "
                                           "-100. -100. -100. -100. -100. -100. -100. -100. -100. -100. -100. -100. "
                                           "-100. -100. -5. -5. -100. -5.",
                          "ResidualsYMax": "5.  5.  5.  100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100."
                                           " 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 100. 5. 5.  100. "
                                           "5.",
                          "ResidualsYMin": "-5. -5. -5.  -100. -100. -100. -100. -100. -100. -100. -100. -100. -100."
                                           " -100. -100. -100. -100. -100. -100. -100. -100. -100. -100. -100. -100."
                                           " -100. -100. -5. -5. -100. -5.",
                          "ExcludedPlanesXCoord": "",
                          "ExcludedPlanesYCoord": "",
                          "ExcludedPlanes": "10 12 13 14 15 16 17 18 19 20 21 22 24 25 26 27 28 29 30 31 32 33",
                          "dropCollectionName": "",
                          }
    
    config["patternRecognition"] = {"dutDirection": "0",
                                    "EventsAlign": "25000",
                                    "DoubletDistCut": "3 3",
                                    "DoubletCenDistCut": "1 1",
                                    "TripletConnectDistCut": "1 1",
                                    "TripletSlopeCuts": "1 1",
                                    "excludeplanes": "10 12 13 14 15 16 17 18 19 20 21 22 24 25 26 27 28 29 30 31 32"
                                                     " 33",
                                    "planeDimensions": "2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2",
                                    "InitialDisplacement": "0",
                                    "DUTWindow": "1",
                                    "DUTRadialWindow": "0.1",
                                    "HitInputCollectionName": "local_hit",
                                    "TrackCandHitOutputCollectionName": "track_candidates",
                                    "Planes": "0 1 2 11 23 3 4 7 5",
                                    "OutputPathROOT": "PatRec.root",
                                    "outColSel": "selTrack"
                                    }
    
    config["GBLAlign"] = {"EventsAlign": "25000",
                          "lcioInputName": "trackcand",
                          "inputCollectionName": "track_candidates",
                          "BeamCharge": "+1",
                          "FixXshifts": "0 5",
                          "FixYshifts": "0 5",
                          "FixZshifts": "0 1 2 11 23 3 4 7 5",
                          "FixXrot": "0 1 2 3 4 5",
                          "FixYrot": "0 1 2 3 4 5",
                          "FixZrot": "0 5",
                          "r": "0.02",
                          "rFEI4X": "0.072",
                          "rFEI4Y": "0.0144",
                          "dutX": "1000",
                          "dutY": "1",
                          "xResolutionPlane": "%(r)s %(r)s %(r)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s"
                                              " %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s  %(dutX)s "
                                              "%(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s"
                                              " %(dutX)s %(dutX)s %(dutX)s %(r)s %(r)s %(rFEI4X)s %(r)s",
                          "yResolutionPlane": "%(r)s %(r)s %(r)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s"
                                              " %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s"
                                              " %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s"
                                              " %(dutY)s %(dutY)s %(r)s %(r)s %(rFEI4Y)s %(r)s",
                          "MilleBinaryFilename": "millepede.bin",
                          "MilleSteeringFilename": "steer.txt",
                          "MilleResultFilename": "millepede.res",
                          "GearAlignedFile": "alignedGear-%(FilePrefix)s.xml",
                          "outlierdownweighting": "outlierdownweighting 4",
                          "GBLMEstimatorType": "",
                          "TracksOutputCollectionName": "Alignment-tracks",
                          "excludeplanes": "10 12 13 14 15 16 17 18 19 20 21 22 24 25 26 27 28 29 30 31 32 33",
                          "pede": "chiscut 30 6"
                          }
                        
    config["GBLTrackFit"] = {"r": "0.2",
                             "rFEI4X": "0.015",
                             "rFEI4Y": "0.015",
                             "dutX": "1000",
                             "dutY": "1000",
                             "xResolutionPlane": "%(r)s %(r)s %(r)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s"
                                                 " %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s"
                                                 " %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s"
                                                 " %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(dutY)s %(r)s %(r)s %(rFEI4Y)s"
                                                 " %(r)s",
                             "yResolutionPlane": "%(r)s %(r)s %(r)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s"
                                                 " %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s"
                                                 " %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s"
                                                 " %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(dutX)s %(r)s %(r)s %(rFEI4X)s"
                                                 " %(r)s ",
                             "dutPlanes": "11 23",
                             "GBLMEstimatorType": "",
                             "dropCollectionName": "",
                             "inputCollectionName": "track_candidates",
                             "outputCollectionName": "tracks",
                             "lcioInputName": "trackcand",
                             "lcioOutputName": "GBLtracks",
                             "histoName": "GBLtracks",
                             "inColSel": "%(outputCollectionName)s",
                             "outColSel": "selTrack",
                             "mustHaveHit": "",
                             "mustNotHaveHit": "",
                             "chi2NormCut": "100",
                             "OutputPathROOT": "NTuple_@RunNumber@_R0S_@Threshold@_300.root",
                             "Planes": "0 1 2 3 4 5 11 23 7",
                             }
    
    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path, only_create=False):
    """
    Returns a config object
    :param path: filename
    :param only_create: just to create without charging memory
    """
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        create_config(path)
    if only_create:
        create_config(path)
    else:
        config = configparser.ConfigParser(allow_no_value=True)
        config.optionxform = str
        config.read(path)
        return config


def get_configuration(config_path, section, setting):

    # TODO add try except in case one of the Settings is not there

    """
    Returns value from given "section" and "setting" in config file
    :param config_path:
    :param section:
    :param setting:
    :return:
    """

    # Getting the config file
    env_config = get_config(config_path)
    
    # List containing "special" settings. Can have a list of values
    spec_sets = ["runList", "reconstProcessors", "StripVec", "localDistDUT", "ExcludedPlanes", "ExcludePlanes",
                 "excludePlanes", "DoubletDistCut", "DoubletCenDistCut", "TripletConnectDistCut", "TripletSlopeCuts",
                 "planeDimensions", "DUTWindow", "DUTRadialWindow", "Planes", "dutPlanes",
                 "FixZshifts", "r", "rFEI4X", "rFEI4Y", "dutX", "dutY", "NoEvents", "dutA", "dutR", "thresholdlist"]
    str_value = env_config.get(section, setting, raw=True)
    
    # Making distinction for settings
    if setting in spec_sets:
        value = str_value.split()
        return value
    else:
        return str_value


def modify_config(path, section, setting, value):
    """
    Create, read, update config file
    :param path: filename
    :param section: processor
    :param setting: variable
    :param value: variable value
    :return: modified config file
    """
    #  Getting the config file
    config = get_config(path)
    
    #  Changing and writing
    with open(path, "w") as config_file:
        #  Changing the value of a given setting in section and making sure to have str values
        if type(value) == str:
            config.set(section, setting, value)
        else:
            config.set(section, setting, str(value))
        config.write(config_file)


def up_from_ini(config_path, ini_path):
    # Getting .ini and .cfg files
    tel_conf = get_config(config_path)
    ini_conf = get_config(ini_path)
    
    # Getting list of sections. Default not included
    ini_section = ini_conf.sections()
    conf_section = tel_conf.sections()

    # List of "special treatment" settings which are not updated in the beginning (the initial values for these ones
    # are taken for the EUTelescope config file)
    spec_opt2 = ["DoubletDistCut", "DoubletCenDistCut", "TripletConnectDistCut", "TripletSlopeCuts"]
    spec_opt = ["DUTWindow", "DUTRadialWindow", "r", "rFEI4X", "rFEI4Y", "dutX", "dutY", "NoEvents", "dutA", "dutR"]
    
    # Looping over sections and settings in .ini file
    for ini_sec in ini_section:
        for opt_ini in ini_conf.options(ini_sec):
            
            # Looping over sections and setting in .cfg file
            for conf_sec in conf_section:

                # To get rid off default settings in every setting list (see configparser behavior)
                if conf_sec == "clustering":
                    opt_list = []
                else:
                    # defaultopt is the number of options in default setting of the Telescope config, which has
                    # to be subtracted from each section option list
                    defaultopt = len(tel_conf.defaults().keys())
                    re = len(tel_conf.options(conf_sec)) - defaultopt
                    opt_list = tel_conf.options(conf_sec)[:re]

                for opt_conf in opt_list:

                    # Checking options from .ini and .cfg
                    if (opt_ini == opt_conf) and (opt_ini not in spec_opt) and (opt_ini not in spec_opt2):

                        # Updating option value in .cfg file
                        tmp = ini_conf.get(ini_sec, opt_ini)
                        modify_config(config_path, conf_sec, opt_conf, tmp)
                        # print("now changing", opt_conf, "to value", tmp, "\n")
                    
                    elif opt_ini == opt_conf and opt_ini in spec_opt:
                        
                        # print("second if", "opt_ini is", opt_ini, "opt_conf", opt_conf, "\n")
                        tmp = get_configuration(ini_path, ini_sec, opt_ini)
                        modify_config(config_path, conf_sec, opt_conf, tmp[0])
                        # print("now changing", opt_conf, "to value", tmp, "\n")
                    
                    elif opt_ini == opt_conf and opt_ini in spec_opt2:
                        
                        # print("third if", "opt_ini is", opt_ini, "opt_conf", opt_conf, "\n")
                        tmp = get_configuration(ini_path, ini_sec, opt_ini)
                        modify_config(config_path, conf_sec, opt_conf, tmp[0] + " " + tmp[1])
                        # print("now changing", opt_conf, "to value", tmp, "\n")
                        
    # for updating DEFAULT section in telescope config file
    
        for opt in ini_conf.options(ini_sec):
            opt_inival = ini_conf[ini_sec][opt]
            if tel_conf.has_option("DEFAULT", opt):
                if opt_inival == tel_conf['DEFAULT'][opt]:
                    continue
                else:
                    modify_config(config_path, 'DEFAULT', opt, opt_inival)
    
 
def update_cuts(config_path, ini_config, ini_section, config_section, setting, iterations, iter_num):
    try:
        setting_values = get_configuration(ini_config, ini_section, setting)
        size_of_setting = len(setting_values)
        if setting not in ['runList', 'alignIterations', 'ExcludedPlanes', 'ExcludePlanes', "excludeplanes", "Planes",
                           "dutPlanes", "FixZshifts", "FixXrot", "FixYrot", "EventsAlign", "EventsAlign", "NoEvents"]:

            if setting in ["DUTWindow", "DUTRadialWindow", "r", "rFEI4X", "rFEI4Y", "dutX", "dutY", "dutA", "dutR"]:

                if iterations - (size_of_setting - 1) > 0 and setting != 'runList' and setting != 'alignIterations':
                    print("Check list of cuts in ini config file for " + setting + ". Cut will not be updated")
                else:
                    modify_config(config_path, config_section, setting, setting_values[iter_num + 1])
                    print("----                                     ----")
                    print("Cut for " + setting + " was updated to ", setting_values[iter_num + 1])
                    print("----                                     ----")
            else:
                # checking size of setting with two number. -2 is because the first two are used in the initial iteration
                if (setting_values == []) or ((size_of_setting - 2) < 2*iterations):
                    print("Check list of cuts in ini config file for " + setting + ". Cuts will not be updated")
                else:
                    modify_config(config_path, config_section, setting, setting_values[2 * iter_num + 2] + " "
                                                + setting_values[2 * iter_num + 3])
                    print("----                                     ----")
                    print("Cuts for " + setting + " were updated to", setting_values[2 * iter_num + 2] + " "
                                                + setting_values[2 * iter_num + 3])
                    print("----                                     ----")
    except:
        print("Cut", setting, " not found, please check your .ini file")


# Gets the last modified file in the directory given by path
def get_latest_file(path):
    files = glob.glob(path + "*")  # * means all if need specific format then *.csv
    latest_file = max(files, key=os.path.getctime)
    return os.path.basename(latest_file)


# def runlist_builder(path_to_file, inp_geo_name, run_number, beam_energy, threshold,flag_geo=False, flag_run=False, flag_thr=False):
#     """
#     Generates/modifies runlist file. (not working completely as expected)
#     :param path_to_file: full path to runlist file
#     :param inp_geo_name: name of geometry file
#     :param flag_geo: should control changing only geo name
#     :param flag_run: should control changing only run number
#     :param flag_thr: should control changing only threshold
#     :param run_number:
#     :param beam_energy:
#     :param threshold:
#     :return:
#     """
#     f = open(path_to_file, "w+")
#     lines = f.read().splitlines()
#     if os.path.getsize(path_to_file) == 0:
#         lines.insert(0, "RunNumber,BeamEnergy,Threshold,GearGeoFile")
#         lines.insert(1, "")
#         lines.insert(2, "00" + str(run_number) + "," + str(beam_energy) + "," + str(threshold) + "," + inp_geo_name)
#     else:
#         if flag_geo:
#             myline = lines[2].split(",")
#             myline[-1] = inp_geo_name
#             lines[2] = myline[0] + "," + myline[1] + "," + myline[2] + "," + myline[3]
#         if flag_run:
#             myline = lines[2].split(",")
#             myline[0] = "00" + (str(run_number))
#             lines[2] = myline[0] + "," + myline[1] + "," + myline[2] + "," + myline[3]
#         if flag_thr:
#             myline = lines[2].split(",")
#             myline[0] = str(threshold)
#             lines[2] = myline[0] + "," + myline[1] + "," + myline[2] + "," + myline[3]
#     f.close()
#     f = open(path_to_file, "w")
#     f.write('\n'.join(lines))
#     f.write('\n')
#     f.close()
    
    # Call this function in this way:
    # runlist_builder("runlist.csv", "my_geofile.xml", flag_geo=False, flag_run=True, run_number=1447)

def runlist_builder(path_to_file, gears, run_number, threshold, beam_energy):
    """
    Generates/modifies runlist file. (not working completely as expected)
    :param path_to_file: full path to runlist file
    :param inp_geo_name: name of geometry file
    :param run_number:
    :param beam_energy:
    :param threshold:
    :return:
    """
    file = open(path_to_file, "w+")
    file.write("RunNumber,BeamEnergy,Threshold,GearGeoFile \n")
    file.write("\n")
    try:
        for gear in gears:
                file.write("000" + str(run_number) + "," + str(beam_energy) + "," +
                           str(threshold) + "," + gear)
    except (IndexError, SyntaxError):
        print("+{:-^78s}+".format("-"))
        print("+{:^78s}+".format(" "))
        print("+ Please check the input list with gear file names +")
        print("+{:^78s}+".format(" "))
        print("+{:-^78s}+".format("-"))
    file.close()


def build_bashscript_reconpos(run_number, your_script_name="runProcessor.sh", path_to_file="./runTelescope.sh", job_same_time=5):
    file = open(path_to_file, "w+")
    file.write("#!/bin/bash \n")
    file.write("\n")
    try:
        for i in range(1, len(run_number)+1):
            if i % job_same_time:
                file.write("source " + your_script_name + " 0"+str(run_number[i-1]) + " &\n")
            else:
                file.write("source " + your_script_name + " 0"+str(run_number[i-1]) + "\n")
    except (IndexError, SyntaxError):
        print("+{:-^105s}+".format("-"))
        print("+{:^105s}+".format(" "))
        print("+ check length or you run number list or python is interpreting format 0XXX"
              " as octet which is not allowed +")
        print("+{:^105s}+".format(" "))
        print("+{:-^105s}+".format("-"))
    file.close()
    
#if __name__ == "__main__":
#    up_from_ini("config_2R0_2018_test_concept.cfg", "recons.ini")
