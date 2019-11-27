  
  
    src   
    ├── __init__.py 
    ├── actions
    │   └── __init__.py
    ├── common
    │   ├── __init__.py
    │   ├── base_page_objs.py ----------------------封装的 webdriver Api 
    │   ├── get_config.py     --------------------- 获取配置文件方法       
    │   └── get_log.py        --------------------- 日志配置方法
    ├── config
    │   ├── __init__.py
    │   └── config.txt        --------------------- 配置文件， 日志、报告、截图的目录等
    ├── elements
    │   ├── __init__.py
    │   └── login_page_element
    │       ├── __init__.py
    │       └── login_page_element.py
    ├── pageobjs
    │   ├── __init__.py
    │   ├── svc
    │   │   └── __init__.py
    │   └── v7k
    │       ├── __init__.py
    │       └── loginPage
    │           ├── __init__.py
    │           └── login_page.py
    ├── reports                  --------------------- 输出
    │   ├── allure-report        --------------------- allure report
    │   ├── logs                 --------------------- 日志
    │   │   └── 2019-11-27.log    
    │   └── screenshots          --------------------- 截图
    │       └── login\ success-passed_2019-11-27_10_55_03.png   
    ├── testcases             ----------测试用例模块
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── svc
    │   │   └── __init__.py
    │   └── v7k
    │       ├── __init__.py
    │       └── logincases     ------------测试模块1
    │           ├── __init__.py
    │           ├── conftest.py
    │           └── test_login.py
    ├── testdata               -------------- 测试数据
    │   └── logindata
    │       ├── __init__.py
    │       └── login_data.py
    ├── testsuite
    │   ├── __init__.py
    │   ├── suite1
    │   │   └── __init__.py
    │   └── suite2
    │       └── __init__.py
    └── utils                 ------------工具方法
        ├── SSHConnection.py
        └── __init__.py
