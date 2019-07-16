#unittest培训后总结记录 
　　今天在给同学们上了自动化测试单元框架unittest之后，突发奇想，要总结下自己今天上的课程内容。于是有了下面的一幕：

　　首先，今天上课的目标是要学会关于unittest框架的基本使用及断言、批量执行。

　　第一个，unittest是什么：
　　为了让单元测试代码能够被测试和维护人员更容易地理解，最好的解决办法是让开发人员遵循一定的规范来编写用于测试的代码，
所以说unittest就随机缘而生，又因为用的人多了，所以逐渐的变成了python的单元测试标准。unittest单元测试框架不仅可以适
用于单元测试，还可以适用WEB自动化测试用例的开发与执行，该测试框架可组织执行测试用例，并且提供了丰富的断言方法，判断测试
用例是否通过，最终生成测试结果。

　　第二个，unittest类和方法的简介：
　　（注：所有的测试用例需要使用test开头作为用例名称）

　　unittest.TestCase：所有测试用例类必须继承TestCase类。

　　TestCase.setUp()：setUp()方法用于测试用例执行前的初始化工作。例如可以初始化driver对象，可以新建数据库访问对象，可以存放公共变量等。

　　TestCase.tearDown()：tearDown()方法用于测试用例执行之后的善后工作。如关闭浏览器，关闭数据库连接等。

　　TestCase.assert*()：assert是一些断言方法：在执行测试用例的过程中，最终用例是否执行通过，是通过判断测试得到的实际结果和预期结果是否相
等决定的。（常用的断言有：assertEqual，assertIs，assertIn等）

　　unittest.skip()：装饰器，当运行用例时，有些用例可能不想执行等，可用装饰器暂时屏蔽该条测试用例。

　　unittest.main()：main()方法使用TestLoader类来搜索所有包含在该模块中以“test”命名开头的测试方法，并自动执行他们。执行方法的默认顺序
是：根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。所以以A开头的测试用例方法会优先执行，以a开头会后执行。

　　unittest.TestSuite()：TestSuite()类是用来创建测试集的。

　　unittest.TestSuite().addTest()：addTest()方法是将测试用例添加到测试集合中。

　　unittest.defaultTestLoader().discover()：通过defaultTestLoader类的discover()方法可自动更具测试目录start_dir匹配查找测试用例
文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。

　　unittest.TextTextRunner()：通过该类下面的run()方法来运行suite所组装的测试用例，入参为suite测试套件。

　　第三，进行代码unittest实践：
　　具体实现代码如下：

　　新建Test_baidu测试类:
import unittest
from selenium import webdriver

class testBaidu1(unittest.TestCase):
    # 添加setup进行初始化工作
    def setUp(self):
        self.driver = webdriver.Firefox()

    #   测试用例使用test开头
    def testbaidu(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        text = self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").get_attribute("text")
        print(text)

        #   断言判断文本是否存在于页面中
        self.assertIn("Web Browser Automation",text)

    def testbaidu1(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        text = self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").get_attribute("text")
        #   断言判断文本是否存在于页面中
        self.assertIn("Web Browser Automation",text)

    #   添加teardown进行善后处理
    def tearDown(self):
        self.driver.quit()

#   添加测试集合
suit = unittest.TestSuite()
suit.addTest(testBaidu1("testbaidu"))
suit.addTest(testBaidu1("testbaidu1"))

if __name__ == '__main__':
    #  使用main()方法进行运行用例
    # unittest.main()

    #   使用 run放进行运行测试用例集
    run = unittest.TextTestRunner()
    run.run(suit)
    
    
    新建 run_all_case类：

    import os
import unittest

#   添加用例搜索目录
case_path = os.path.join(os.getcwd(),"case")

def all_case():
    # 使用discover进行自动搜索测试集
    discover = unittest.defaultTestLoader.discover(case_path,
                                              pattern="Test*.py",
                                              top_level_dir=None
    )
    print(discover)
    return discover


if __name__ == '__main__':
    #   使用run方法运行测试集
    run = unittest.TextTestRunner()
    run.run(all_case())
