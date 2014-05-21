#!/usr/bin/python
import argparse
import pandas as pd

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Parser for CCPT logs')
    parser.add_argument("-i", dest="file_name",help="path to the log file", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.file_name)
    correct_RTs = df[(df.response == "space") & (df.trial_shape == "red_square")].response_time
    false_positive_RTs = df[(df.response == "space") & (df.trial_shape != "red_square")].response_time
    false_negative_RTs = df[(df.response != "space") & (df.trial_shape == "red_square")].response_time


    print "Correct answers (n = %d): mean response time = %g, standard deviation of response time = %g"%(len(correct_RTs),
                                                                                                       correct_RTs.mean(),
                                                                                                       correct_RTs.std())
    print "False positive answers (false alarms) (n = %d): mean response time = %g, standard deviation of response time = %g"%(len(false_positive_RTs),
                                                                                                              false_positive_RTs.mean(),
                                                                                                              false_positive_RTs.std())
    print "False negative answers (missed targets) (n = %d)"%(len(false_negative_RTs))

    first_quartile_RTs = correct_RTs[correct_RTs.index < 80]
    print "First quartile (n = %d): mean = %g; stddev = %g"%(len(first_quartile_RTs),
                                                             first_quartile_RTs.mean(),
                                                             first_quartile_RTs.std())

    second_quartile_RTs = correct_RTs[(correct_RTs.index >= 80) & (correct_RTs.index < 160)]
    print "Second quartile (n = %d): mean = %g; stddev = %g"%(len(second_quartile_RTs),
                                                             second_quartile_RTs.mean(),
                                                             second_quartile_RTs.std())

    third_quartile_RTs = correct_RTs[(correct_RTs.index >= 160) & (correct_RTs.index < 240)]
    print "Third quartile (n = %d): mean = %g; stddev = %g"%(len(third_quartile_RTs),
                                                             third_quartile_RTs.mean(),
                                                             third_quartile_RTs.std())

    fourth_quartile_RTs = correct_RTs[(correct_RTs.index >= 240)]
    print "Fourth quartile (n = %d): mean = %g; stddev = %g"%(len(fourth_quartile_RTs),
                                                             fourth_quartile_RTs.mean(),
                                                             fourth_quartile_RTs.std())
