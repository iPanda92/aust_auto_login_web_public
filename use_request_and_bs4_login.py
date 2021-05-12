from bs4 import BeautifulSoup
import requests, time, os


def connect_web():
    bs = BeautifulSoup((requests.get('http://10.255.0.19/')).text, 'lxml')
    if '注销页' in bs.find('title'):
        print('已登录，不用重复登录')
    else:
        print('开始执行登录程序')
        f = open('user_infornation.txt', 'r')
        # 选择运营商
        choose = ('@aust', '@unicom')
        operator = int(f.readline())
        user_infornation = {
            "callback": "dr1003",
            "DDDDD": f.readline()[0:-1]+choose[operator],
            "upass": f.readline(),
            "0MKKey": "123456",
            "R1": "0",
            "R3": "0",
            "R6": "0",
            "para": "00",
            "v6ip": "",
            "v": "5169"
        }
        for i in range(1, 11):
            print('第' + str(i) + '次尝试登录')
            return_page = requests.post(url='http://10.255.0.19/',
                                        data=user_infornation)
            if '成功' in return_page.text:
                break
            time.sleep(2)
        print('成功') if '成功' in return_page.text else print('失败')
        f.close()


def create_start_up_in_turn_on_programm():
    # 为用户创建开机自启动
    user_path = os.path.expanduser(
        '~/AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
    if not os.path.exists(os.path.join(user_path, 'auto_login.bat')):
        auto_login_file = open(os.path.join(user_path, 'auto_login.bat'), 'w')
        auto_login_file.write(
            os.path.abspath('.') + '/use_request_and_bs4_login.exe')
        auto_login_file.close()


if __name__ == '__main__':
    create_start_up_in_turn_on_programm()
    connect_web()
