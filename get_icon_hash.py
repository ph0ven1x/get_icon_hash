import requests
import base64
import mmh3
import sys


def get_icon_hash():
    print("命令行输入的参数为：", sys.argv)

    if len(sys.argv) != 3:
        print(
            "请执行格式为[ python get_icon_hash.py https://www.example.com/favicon.ico shodan/fofa ] 的命令"
        )
        return

    url = sys.argv[1]
    response = requests.get(url)
    favicon = base64.encodebytes(response.content)
    hash = mmh3.hash(favicon)
    if sys.argv[2] == "fofa":
        print("icon_hash=" + str(hash))
    elif sys.argv[2] == "shodan":
        print("http.favicon.hash:" + str(hash))
    else:
        print(
            "请执行格式为[ python get_icon_hash.py https://www.example.com/favicon.ico shodan/fofa ] 的命令"
        )
        return


if __name__ == "__main__":
    get_icon_hash()
