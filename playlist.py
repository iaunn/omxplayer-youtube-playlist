import urllib, json,sys
import subprocess

def play_url(url):
    yt_dl = subprocess.Popen(['youtube-dl', '--max-quality' , '18', '-g', url], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    (url, err) = yt_dl.communicate()
    if yt_dl.returncode != 0:
        sys.stderr.write(err)
        raise RuntimeError('Error getting URL.')
	print "Playing"
    mplayer = subprocess.Popen(
            ['omxplayer','-b', url.decode('UTF-8').strip()],
            stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    mplayer.wait()
	

input = sys.argv
keyword = input[1]

print 'Play List:', str(input[1])
 
url = "https://gdata.youtube.com/feeds/api/playlists/"+keyword+"?alt=json"
response = urllib.urlopen(url);
data = json.loads(response.read())
feed = data['feed']['entry']

print 'Found ',len(feed),' Video'

for d in feed:
	jsonstring = json.dumps(d)
	title = d['title']['$t']
	link = d['link'][0]['href']
	print "Play : ",title
	play_url(link)
	print "DONE"
print "############# Play All Done ################"


