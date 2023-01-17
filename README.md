# 简介

Apache Tomcat默认安装包含"/examples"目录，该目录包含许多示例servlet和JSP。其中一些示例存在安全风险，不应部署在生产服务器上。
http://localhost:8080/examples/servlets/servlet/SessionExample 示例允许会话操作。因为会话是全局的，所以这个示例会带来很大的安全风险，因为攻击者可用通过操纵其会话来有效的成为管理员。

当然 多半没用，一般安服人员会交到这种垃圾洞-+



# 使用方法

```
python3 apache-example.py urls.txt
```

将`url`放在`urls.txt`中，输出结果就在`result.txt` 



祝你好运
w
