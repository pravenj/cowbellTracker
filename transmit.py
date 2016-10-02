import GroveGPS
import gpsToCalc
import subprocess
import time

#Namo Buddha Resort : 27.58069 85.5904714

if __name__ == "__main__":
	print "While Looping..."
	while 1:
		print "Currently getting GPS"
		proc = subprocess.Popen(['sudo', 'python', 'GroveGPS_modified.py'], shell=False)
		time.sleep(20)
		pid = proc.pid #if proc id is required
		proc.terminate()
		print "Now converting to dist and dir"
		proc = subprocess.Popen(['sudo', 'python', 'gpsToDistance.py'], shell=False)
		time.sleep(2)
		proc.terminate()
		print "Now converting to speech"
		proc = subprocess.Popen(['sudo', 'espeak', '-f', 'foo.txt', '-w', 'foo.wav'], shell=False)
		time.sleep(2)
		proc.terminate()
		print "Now transmitting speech"
		proc = subprocess.Popen(['sudo', './pi_fm_rds', '-audio', 'foo.wav'], shell=False)
		time.sleep(10)
		proc.terminate()
