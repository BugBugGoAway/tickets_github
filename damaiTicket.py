# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from splinter.browser import Browser


class DaMaiTicket(object):

    username = "13701501927"
    password = "19890605lb"
    url = "https://piao.damai.cn/143439.html?spm=a2o6e.search.0.0.2bd01e33evOkdz"
    count = 0

    def __init__(self):
        print("Welcome use Tickets...")

    def login(self):  # 登录
        self.driver.find_element_by_id('login_email').send_keys(self.username)
        time.sleep(2)
        self.driver.find_element_by_id('login_pwd_txt').click()
        time.sleep(1)
        self.driver.find_element_by_id('login_pwd').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_id("subbtn").click()
        time.sleep(1)
        if None is self.driver.get_cookie("damai.cn_email"):
            print("遇到该死的验证系统了，请按页面提示登陆进去...")
            time.sleep(1)
            self.slide()
            #点击汉字验证码函数
            # ...
            # ...
            # ...
            self.driver.find_element_by_id('login_pwd_txt').click()
            time.sleep(0.5)
            self.driver.find_element_by_id('login_pwd').send_keys(self.password)
        # while True:
        #     # print(self.driver.get_cookie("damai.cn_email"))
        #     # allCookies = self.driver.get_cookies()
        #     # for c in allCookies:
        #     #     # print(c)
        #     #     if c == "damai.cn_email":
        #     #         print("登陆成功！")
        #     #         return True
        #
        #     else:
        #         return True

    def slide(self):
        slider = self.get_slider()
        track = self.get_track(338)
        ActionChains(self.driver).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()
        check_method = EC.text_to_be_present_in_element((By.CLASS_NAME, 'nc-lang-cnt'), '请按住滑块，拖动到最右边')
        success = WebDriverWait(self.driver, 20, 0.5).until_not(check_method)
        print(success)

    def get_slider(self):
        # 获取滑块
        # slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        slider = self.driver.find_element_by_id("nc_1_n1z")
        return slider

    def get_track(self, distance):
        # 根据偏移量获取移动轨迹
        # :param distance: 偏移量
        # :return: 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))

        return track

    def loop(self):  # 循环刷新购票页面
        try:
            print("=====================页面title："+self.driver.title+"=====================")
            if self.driver.current_url == self.url:
                self.count += 1
                print("第" + str(self.count) + "次刷新页面")
                self.driver.find_element_by_link_text('2018-03-18 周日 19:30').click()
                priceDiv = self.driver.find_element_by_id("priceList")
                ul = priceDiv.find_element_by_tag_name("ul")
                lis = ul.find_elements_by_tag_name("li")
                print("票价共有" + str(len(lis)) + "种")
                availableLis = []
                for e in lis:
                    a = e.find_elements_by_tag_name("a")[0]
                    # span = a.find_elements_by_tag_name("span")[0]
                    if e.get_attribute('item'):
                        # print("票价：" + span.value)
                        print("票价："+e.get_attribute("data-pricename"))
                        availableLis.append(a)
                if len(availableLis) > 0:
                    #   选择最低的票价
                    availableLis[0].click()
                    print("点击了" + availableLis[0])
                    return True
                else:
                    print("全TM是灰色的....")
                print("=======================================================================")
            else:
                print("被定向去其他页面了，正在转回购票页面...")
                self.driver.get(self.url)
                time.sleep(2)
        except Exception as e:
            print("循环刷新页面时产生异常："+str(e))
            self.driver.refresh()
            time.sleep(2)

    def start(self):
        self.driver = webdriver.Firefox()
        time.sleep(1)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_elements_by_link_text("登录")[0].click()
        time.sleep(3)
        isLogin = self.login()
        if isLogin:
            while True:
                self.loop()


if __name__ == "__main__":
    damai = DaMaiTicket()
    damai.start()




