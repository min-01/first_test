# first_test
first
皿心水个人应用网（非正式版）
开发者：皿心水
功能：简单信息录入功能，登录功能，待办功能，查看录入名单
界面：简易菜单条+各功能实现

设计：使用Python Flask框架设计接口，pymysql连接数据库，bootstrap前端框架
jinjia2模板引擎实现数据交互。
主页信息录入使用form表单将各数据以post方法提交到/apply接口，
接收后调用方法插入数据表，查看名单时，请求接口为name_list，返回查询结果放入User类
的实例中方便输出，界面使用循环将传过来的对象输出：
{% for user in users %}
{{ user.id }}---{{ user.name }}
    <br>
{% endfor %}
在之前测试时一直存在数据库断开的错误
解决办法为在每个操作方法前加connect.ping(reconnect=True)
确报在调用数据时正常连接数据库。
登录后关联待办，代办与登录账号关联，添加待办将输入框内容、时间和账号密码一起保存
时间即创建待办的时间datetime.datetime.now()，查询对应账号的待办返回。同样循环输出呈现。