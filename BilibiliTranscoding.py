import requests
import re
import argparse
import time


def banner():
    banner = '''
                                    Lisence
    
    Biliblli视频转码,无需登录即可观看高清画质,支持下载本地，无去水印功能,自测适用于大部分视频
    但是有一部分视频由于未知原因(作者禁转载、互动视频等)，不适用此种方法

                                    @Givemefivw  Just For Fun
    '''
    print(banner)


def trans(url):
    print("[*] 正在获取视频的AID&CID...")
    time.sleep(0.5)
    original_res = requests.get(url.replace("bilibili","ibilibili"))
    key = re.compile(r"//player.bilibili.com/player.html?(.*)&page=1",re.DOTALL)
    aid = key.findall(original_res.text)[0]
    print("[*] 正在替换ACID...")
    time.sleep(0.5)
    acid = aid.replace("aid","avid")
    middle_url = "https://api.bilibili.com/x/player/playurl" + acid + "&qn=1&type=&otype=json&platform=html5&high_quality=1"
    print("[*] 正在获取最终视频地址...\n")
    time.sleep(0.5)
    middle_res = requests.get(middle_url)
    key1 = re.compile(r'"vhead":"","url":"(.*)","backup_url"',re.DOTALL)
    fina = key1.findall(middle_res.text)[0]
    finally_url = fina.encode('latin-1').decode('unicode_escape')
    print(finally_url)


def main():
    parser = argparse.ArgumentParser(description='Bilibillitrans Help')
    parser.add_argument('-u','--url',help='Bilibilli url',default='')
    args = parser.parse_args()
    if args.url:
        url = args.url
        trans(url)



if __name__ == '__main__':
    banner()
    main()