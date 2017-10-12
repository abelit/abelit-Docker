from django import forms

class HostForm(forms.Form):
    name = forms.CharField(label='服务器名称', widget=forms.TextInput(attrs={'class': 'validate'}), max_length=50, required=True,
    error_messages={'required': u'请填写服务器名称'})

    ipaddress = forms.CharField(label='IP地址',max_length=50,error_messages={
        'required': '请填写服务器IP地址'
    })

    username = forms.CharField(label='用户名',max_length=50,error_messages={
        'required': '请填写服务器用户名'
    })

    password = forms.CharField(label='密码', widget=forms.PasswordInput, error_messages={
        'required': '请填写服务器密码'
    })

    ssh_port = forms.CharField(label='SSH端口',max_length=50,error_messages={
        'required': '请填写服务器ssh端口号'
    })

class OracleForm(forms.Form):
    service_name = forms.CharField(label='服务名', widget=forms.TextInput(attrs={'class': 'validate'}), max_length=50, required=True,
    error_messages={'required': u'请填写Oracle数据库服务名'})
    db_user = forms.CharField(label='用户',max_length=50,error_messages={
        'required': '请填写Oracle用户名'
    })

    db_password = forms.CharField(label='密码', widget=forms.PasswordInput, error_messages={
        'required': '请填写Oracle密码'
    })

    db_port = forms.CharField(label='端口',max_length=50,error_messages={
        'required': '请填写Oracle端口号'
    })
