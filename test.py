import send_email

d = [
    {
        "t": "plain",
        "s": "测试纯文本的 email",
        "c": """
                测试一下纯文本内容,为什么不让我过?
                •553 Requested action not taken: NULL sender is not allowed 不允许发件人为空，请使用真实发件人发送；
              　　•553 Requested action not taken: Local user only  SMTP类型的机器只允许发信人是本站用户；
                """,
        "a": None,
        "i": None
    },
    {
        "t": "html",
        "s": "测试 html 格式的 email",
        "c": """
                测试一下HTML格式的内容,为什么不让我过?<br/>
                •550 Requested mail action not taken: too much recipient  群发数量超过了限额；<br/>
                <hr/>
              　　•552 Requested mail action aborted: exceeded mailsize limit 发送的信件大小超过了网易邮箱允许接收的最大限制；<br/>
              　　•553 Requested action not taken: NULL sender is not allowed 不允许发件人为空，请使用真实发件人发送；<br/>
              　　•553 Requested action not taken: Local user only  SMTP类型的机器只允许发信人是本站用户；<br/>
              　　•553 Requested action not taken: no smtp MX only  MX类型的机器不允许发信人是本站用户；<br/>
                """,
        "a": None,
        "i": None
    },
    {
        "t": "html",
        "s": "测试 带图片的 email",
        "c": """
                测试一下带图片的内容<br/>
                •550 Requested mail action not taken: too much recipient  群发数量超过了限额；<br/>
                """,
        "a": ("python.png", "google.png"),
        "i": ("python.png", "google.png")
    },

]

login = {
    'smtpserver': 'smtp.163.com',
    'username': 'xxx@163.com',
    'password': 'xxx'
}

for i in d:
    mail = {
        'email_type': i["t"],
        'from': 'xxx@163.com',
        'to': ['xxx@126.com', 'xxx@163.com'],  # 单人用字符串,多人用列表
        'subject': i["s"],
        'content': i["c"]
    }
    send_email.send_email(login=login, mail=mail, attachments=i["a"], images=i["i"])

print("发送完毕!")
