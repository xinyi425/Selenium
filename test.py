# print('hello world')
# 导包 from selenium import webdriver
# 导包 from selenium.webdriver.chrome.options import Options
# 导包 from selenium.webdriver.chrome.service import Service
from selenium import webdriver #用于操作浏览器
from selenium.webdriver.chrome.options import Options #用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service #用于管理谷歌驱动
import time
from selenium.webdriver.common.by import By  #用于元素的一个类型 定位的一个主语句 定位
#设置浏览器、启动浏览器
def she():
# 创建设置浏览器对象
    q1 = Options()
# 禁用沙盒模式(增加兼容性)
    q1.add_argument('--no-sandbox')
# 保持浏览器打开状态(默认是代码执行完毕自动关闭)
    q1.add_experimental_option('detach', True)
# 创建并启动浏览器
    a1 = webdriver.Chrome(service=Service('chromedriver.exe'), options=q1)
    a1.implicitly_wait(30)#通用设置
    return a1

a1 = she()
a1.get('https://www.baidu.com/')#打开指定网址
#time.sleep(2)

#网页的前进、后退
#a1.find_element(By.XPATH, '//*[@id="kw"]').send_keys('liu')
# time.sleep(2)
#a1.find_element(By.XPATH, '//*[@id="su"]').click()
# time.sleep(2)
#网页的后退
# a1.back()
# time.sleep(2)
#网页的前进
# a1.forward()


# 获取元素文本内容、是否可见
# 演示地址:https://jingji.cctv.com/2025/07/20/ARTItp6ecrpXZ7tUktOp5G8g250720.shtml
# 获取元素文本内容 text
# a2=a1.find_element(By.XPATH, '//*[@id="content_area"]/p[3]').text
# print(a2)
#元素是否可见 is_displayed() 可见是ture 不可见是false
# a3=a1.find_element(By.XPATH, '//*[@id="tb-beacon-aplus"]').is_displayed()
# print(a3)

# iframe嵌套页面进入、退出
# 演示地址:https://sahitest.com/demo/iframesTest.htm
# 获取iframe元素
# a2=a1.find_element(By.XPATH, '/html/body/iframe')
# 进入iframe嵌套页面
# a1.switch_to.frame(a2)
# time.sleep(2)
# 再点击页面的页面里面的按钮
# a1.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
# 退出iframe嵌套页面(返回到默认页面)
# a1.switch_to.default_content()
# time.sleep(2)
# 点击页面的按钮
# a1.find_element(By.XPATH, '/html/body/input[2]').click()



#提示框(prompt)元素交互
#演示地址:https://sahitest.com/demo/promptTest.htm
#弹窗输入内容
# a1.find_element(By.XPATH, '/html/body/form/input[1]').click()
# time.sleep(2)
#弹窗输入内容
# a1.switch_to.alert.send_keys('liu')
# time.sleep(2)
#弹窗点击确定
# a1.switch_to.alert.accept()


#确认框(confirm)元素交互
#演示地址:https://sahitest.com/demo/confirmTest.htm
#a1.find_element(By.XPATH, '/html/body/form/input[1]').click()
#time.sleep(2)
#点击弹窗确定按钮
# a1.switch_to.alert.accept()
#点击弹窗取消按钮
#a1.switch_to.alert.dismiss()

#警告框(alert)元素交互
#演示地址:https://sahitest.com/demo/alertTest.htm
# a1.find_element(By.XPATH, '/html/body/form/input[1]').clear()
# a1.find_element(By.XPATH, '/html/body/form/input[1]').send_keys('liu')
# a1.find_element(By.XPATH, '/html/body/form/input[2]').click()
#获取弹窗的文本内容 必须先获取，如果先点击弹窗就消失了无法获取了
# print(a1.switch_to.alert.text)
# 点击弹窗确定按钮
# time.sleep(2)
# a1.switch_to.alert.accept()



# 获取句柄、切换标签页
#for x in range(2):(循环俩次)
    #a2 = a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]').click()
#获取全部标签页句柄
    #a2 = a1.window_handles 获取出了几个页面 例子里出了俩个
    #print(a2) 获取出了几个页面
#关闭当前标签页
    #a1.close()
#通过句柄切换标签页
    #a1.switch_to.window(a2[1]) 转换到第二个句柄
# 获取当前标签页句柄
# a2 = a1.current_window_handle
# print(f'当前控制标签页的句柄:{a2}')

# 日期、评星、上传元素交互
#上传元素要全路径(绝对路径)例子:a2 = a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]').send_keys(r'D:\xue1\Selenium\logo2.png')

#单选、多选、下拉元素交互


#元素定位隐性等待(多少秒内找到元素就立刻执行，没找到元素就报错)
# 演示地址:https://bahuyun.com/bdp/form/1327923698319491072
#a2 = a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]').click()
#a1.implicitly_wait(10) a1通用设置后 以后就不需要再设置了


#元素定位-XPATH
#1，复制谷歌浏览器 Xpath(通过属性+路径定位 属性如果是随机的，可能定位不到)
#2.复制谷歌浏览器 Xpath 完整路径(缺点是定位值比较长，优点是基本100%准确)
#a2 = a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]').click()

#元素定位-CSS_SELECTOR[样式的选择器]
#1.#id = 井号+id值 通过id定位
#2..class = 点+class值 通过class定位
#3.不加修饰符 = 标签头
#4.通过任意类型定位:"[类型='精准值']"
#5.通过任意类型定位:"[类型*='模糊值']"
#6.通过任意类型定位:"[类型^='开头值']"
#7.通过任意类型定位:"[类型$='结尾值']"
#以上这些方法都属于理论定位法
#8.更简单的定位方式:在谷歌控制台直接复制 SELECTOR (个别元素定位值会比较长)
#a2 = a1.find_element(By.CSS_SELECTOR, "#kw").send_keys('liu')

#元素定位-PARTIAL_LINK_TEXT
#通过模糊链接文本找到标签a的元素[模糊文本定位]
#有重复的文本，需要切片
#a2 = a1.find_element(By.PARTIAL_LINK_TEXT, '音').click()

#元素定位-LINK_TEXT
#通过精准链接文本找到标签a的元素
#有重复的文本，需要切片
#a2 = a1.find_element(By.LINK_TEXT, '新闻').click()

#元素定位-TAG_NAME
#1.找出<开头标签名字>
#2.重复的标签名字特别多,需要切片
#a2 = a1.find_elements(By.TAG_NAME, 'a')[3].click()

#元素定位-CLASS_NAME
#1.CLASS值不能有空格，否则报错
#2.CLASS值重复的有很多，需要切片-后面加个[]
#3.CLASS值有的网站是随机的
#多个元素一定要加s
#a2 = a1.find_element(By.CLASS_NAME, 's_ipt').send_keys('liuyazhou')
#a2 = a1.find_element(By.CLASS_NAME, 'bg s_bt').click()
#a2 = a1.find_elements(By.CLASS_NAME, 'icon-bg--icon')[1].click()
#a2 = a1.find_element(By.CLASS_NAME, 'icon-bg--icon').click()

#元素定位-NAME
#1.通过NAME定位元素，一般比较准确
# 2.并不是所有网页或者页面 都有NAME值
#a2 = a1.find_element(By.NAME, 'wd').send_keys('liuyazhou')

# 元素定位-ID
# 1.通过ID定位元素，一般比较准确
# 2.并不是所有网页或者页面 都有ID值
#a2 = a1.find_element(By.ID, 'kw').send_keys('liuyazhou')
#元素的交互操作
# a2 = a1.find_element(By.ID, 'kw')
#元素的输入
# a2.send_keys('liuyazhou')
# time.sleep(2)
#元素的清空
# a2.clear()
# time.sleep(2)
#元素的输入
# a2.send_keys('liuyazhou')
# time.sleep(2)
#找到按钮
# a2 = a1.find_element(By.ID, 'su')
#元素的点击
# a2.click()


#定位一个元素或者定位多个元素
#通过谷歌浏览器的控制台查找多个元素
#document.getElementById('元素值')
#定位一个元素 By就是需要的定位的类型 八大定位(找到的话返回结果,找不到的话报错)
#a2 = a1.find_element(By.ID, 'kw')
#定位多个元素(找到的话返回列表形式，找不到返回空列表)
#a2 = a1.find_elements(By.ID, 'kw')
#print(a2)

#浏览器截图，刷新当前网页
#浏览器截图
#a1.get_screenshot_as_file('1.png')
#刷新当前网页
#a1.refresh()

#浏览器打开的位置和尺寸
#浏览器的打开位置,x离左侧的距离，y上侧的距离
#a1.set_window_position(0, 0)
#浏览器打开的尺寸
#a1.set_window_size(600, 600)

# 浏览器最大化最小化
# time.sleep(2)
# 浏览器最大化
# a1.maximize_window()
# time.sleep(2)
# 浏览器最小化
# a1.minimize_window()

#关闭标签页,退出浏览器并释放驱动
#time.sleep(3)
#关闭标签页
# a1.close()
#退出浏览器并释放驱动
#a1.quit()


