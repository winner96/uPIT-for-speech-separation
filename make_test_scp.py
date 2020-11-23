import os
import sys

mydir = os.path.dirname(__file__)
scp_dir = mydir + "/scp"

if len(sys.argv) > 1:
    avs_audio = sys.argv[1]
else:
    avs_audio = mydir# + "/" + "avs_audio" # default path of my code


if not os.path.exists(scp_dir):
    os.makedirs(scp_dir)
    print("made {}".format(scp_dir))
else:
    print("{} already exists".format(scp_dir))

if not os.path.exists(scp_dir):
    raise NameError("no {} exists".format(scp_dir))


tt_s1_scp = scp_dir + "/" + "tt_s1.scp"
tt_s2_scp = scp_dir + "/" + "tt_s2.scp"
tt_mx_scp = scp_dir + "/" + "tt_mx.scp"

tt_mx = avs_audio + "/avs_tt/mix"


w1 = open(tt_s1_scp, mode= 'w')
w2 = open(tt_s2_scp, mode= 'w')
wm = open(tt_mx_scp, mode= 'w')
for root, dirs, files in os.walk(tt_mx):
    for file in files:
        key = file[:-4]
        s1 = file[:11] + ".wav"
        s2 = file[12:23] + ".wav"
        w1.write(key + " " + avs_audio + "/avs_tt/spk1/" + s1 + '\n')
        w2.write(key + " " + avs_audio + "/avs_tt/spk2/" + s2 + '\n')
        wm.write(key + " " + avs_audio + "/avs_tt/mix/" + file + '\n')

w1.close()
w2.close()
wm.close()
print("test scp done")

