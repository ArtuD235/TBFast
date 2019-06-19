# Write here the runs and threshold you want to add
# Right relation between run number at threshold has to handle but the user
# run_number_string = "470	471	472	473	474	475	477	478	479	480	481	482"
# run_number_string = "574	575	576	577	578	579	580	582	583	584	585	586	587	588	589"
# threshold_str = "24	30	40	50	60	70	80	100	110	120	130	140	150	160	170"
# run_number_string = "300	301	302	303	305	306	307	308	309	310	311	312	313"
# threshold_str = "30	24	40	50	70	80	90	100	110	120	130	140	150"
# run_number_string = "318	319	322	324	325	326	327	328	329	330	331	332	333"
# threshold_str = "24	30	50	70	80	90	100	110	120	130	140	150	160"
# run_number_string = "221	222	223	224	225	226	228	229	230	231	232	233	234	235	236	237	238"
# threshold_str = "20	24	30	40	50	60	70	80	90	100	110	120	130	140	150	160	170"
# run_number_string = " 240	241	242	243	244	245	246	247	248	249	250	251	252	253	254	255"
# threshold_str = " 24	30	40	50	60	70	80	90	100	110	120	130	140	150	160	170"
# run_number_string = " 186	187	188	189	190	191	192	193	194	195	196	197	198	199	200	201"
# threshold_str = " 20	30	40	50	60	70	80	90	100	110	120	130	140	150	160	170"
run_number_string = "205	206	207	208	209	210	211	212	213	214	215	216	217	218	219"
threshold_str = "30	40	50	60	70	80	90	100	110	120	130	140	150	160	170 "
run_number = run_number_string.split()
threshold = threshold_str.split()
beam_energy = 5.8
# align_gear = "alignedGear-run000323.xml"
# align_gear = "aligned-iter3-run000247.xml"
# align_gear = "aligned-iter4-run000193.xml"
align_gear = "aligned-iter4-run000211.xml"

def runlist_builder(path_to_file, inp_geo_name, run_number=[897], threshold=[90], beam_energy=5.8):
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
        for i in range(len(run_number)):
            if i == len(run_number)-1:
                # hardcoded number of 0s to find right run number TODO: fix this
                file.write("000" + str(run_number[i]) + "," + str(beam_energy) + "," +
                           str(threshold[i]) + "," + inp_geo_name)
            else:
                file.write("000" + str(run_number[i]) + "," + str(beam_energy) + "," +
                           str(threshold[i]) + "," + inp_geo_name + "\n")

    except (IndexError, SyntaxError):
        print("+{:-^78s}+".format("-"))
        print("+{:^78s}+".format(" "))
        print("+ the length of your input run number list is different from the threshold one +")
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


runlist_builder("./runlist_recons.csv", align_gear, run_number, threshold)
build_bashscript_reconpos(run_number)

