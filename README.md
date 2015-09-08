# send_email

python2.7.10下正常.

###发送带附件的邮件基本思路如下：
* 构造MIMEMultipart对象做为根容器
* 构造MIMEText对象做为邮件显示内容并附加到根容器
* 构造MIMEImage对象做为图片附件并附加到根容器
* 构造MIMEBase对象做为文件附件内容并附加到根容器
  *  a. 读入文件内容并格式化
  *  b. 设置判断MIME类型并设置附件头
* 设置根容器属性
* 得到格式化后的完整文本
* 用smtp发送邮件

###参数
* login 是登录信息,包括smtp服务器地址,帐号,密码
* mail 是邮件内容,应该是个字典,包含邮件类型,发送人,收件人(多人的话要使用列表),标题,内容.
* images 和 attachments 是要发送的图片和附件,要用本地系统的路径.
* use_ssl 表示是否使用 ssl.    
    
```python    
login = {
    'smtpserver' : 'smtp.163.com',
    'username' : 'xxx@163.com',
    'password' : 'xxx'
}
mail = {
    'email_type' : "html",      # email_type可以是:plain/html
    'from' : 'xxx@163.com',
    'to' : 'xxx@126.com',        # 单人用字符串,多人用列表              
    'subject' : "标题",
    'content' : "正文"
}
```