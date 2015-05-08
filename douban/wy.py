#coding=utf8
#import os,requests
import md5
import requests,json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in xrange(len(byte2)):
        byte2[i] = byte2[i]^byte1[i%byte1_len]
    m = md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result

def wangyi(song,artist):
	s = requests.session()
	data = {
			'hlpretag':'<span class="s-fc7">',
			'hlposttag':'</span>',
			's':song,
			'type':'1',
			'limit':'8',
			'offset':'0',
			#'total':'true'
			}
	r = s.post('http://music.163.com/api/search/get/web?csrf_token=',data=data,headers={'referer':'http://music.163.com/','User-Agent':'ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'})
	#print(str(r.text))
	d = json.loads(r.text)
	#print(d)
	d = d['result']['songs']
	#print(d[0]['id'])
	#print(len(d['result']['songs']))
	#exit()
	for i in range(len(d)):
		if d[i]['artists'][0]['name'].encode('utf-8').lower() == artist.encode('utf-8').lower():
		#if d[i]['artists'][0]['name'].lower() == artist.lower():
			id = str(d[i]['id'])
	#print(id)
	#exit()
	#id = str(d['result']['songs'][0]['id'])
			r = s.get('http://music.163.com/api/song/detail/?id=' + id + '&ids=%5B' + id +'%5D&csrf_token=')
			d1 = json.loads(r.text)
			if d1['songs'][0]['hMusic'] != None:
				break
	#print(d['songs'][0])
	dfsid = str(d1['songs'][0]['hMusic']['dfsId'])
	#print(dfsid)
	eid = encrypted_id(dfsid)
	url = 'http://m1.music.126.net/' + eid +'/'+ dfsid + '.mp3'
	#print(url)
	return url

'''
id = '7860408627359797'
eid = encrypted_id(id)
os.system('wget http://m1.music.126.net/' + eid + '/' + id + '.mp3')
'''

if __name__ == '__main__':
	song = 'Butter-Fly'
	artist = '和田光司'
	wangyi(song,artist)
	#print(wangyi(song))
	#print(wangyi(song,artist))

