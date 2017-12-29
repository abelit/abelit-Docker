from django import forms
from report.models import Host, Oracle


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'

    name = forms.CharField(label='服务器名称(*)', widget=forms.TextInput(attrs={'class': 'validate form-control'}), max_length=50, required=True,error_messages={'required': u'请填写服务器名称'})
    ipaddress = forms.CharField(label='IP地址(*)', widget=forms.TextInput(attrs={'class': 'validate form-control'}), max_length=50, error_messages={'required': '请填写服务器IP地址'})
    username = forms.CharField(label='服务器用户名(*)', widget=forms.TextInput(attrs={'class': 'validate form-control'}), max_length=50, error_messages={'required': '请填写服务器用户名'})
    password = forms.CharField(label='服务器密码(*)', widget=forms.PasswordInput(attrs={'class': 'validate form-control'}), error_messages={'required': '请填写服务器密码'})
    ssh_port = forms.CharField(label='SSH端口(*)', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, error_messages={'required': '请填写服务器ssh端口号'})
    remark = forms.CharField(label='备注', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), max_length=50,required=False)

class HostMetricForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'

    name = forms.CharField(label='服务器名称(*)', widget=forms.TextInput(attrs={'class': 'validate form-control'}), max_length=50, required=True,error_messages={'required': u'请填写服务器名称'})
    ipaddress = forms.CharField(label='IP地址(*)', widget=forms.TextInput(attrs={'class': 'validate form-control'}), max_length=50, error_messages={'required': '请填写服务器IP地址'})
    username = forms.CharField(label='服务器用户名(*)', widget=forms.TextInput(attrs={'class': 'validate form-control'}), max_length=50, error_messages={'required': '请填写服务器用户名'})
    password = forms.CharField(label='服务器密码(*)', widget=forms.PasswordInput(attrs={'class': 'validate form-control'}), error_messages={'required': '请填写服务器密码'})
    ssh_port = forms.CharField(label='SSH端口(*)', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, error_messages={'required': '请填写服务器ssh端口号'})
    hostname = forms.CharField(label='主机名', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    cpu = forms.CharField(label='处理器', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    memory = forms.CharField(label='内存', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    disk = forms.CharField(label='磁盘', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    system = forms.CharField(label='系统', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    application = forms.CharField(label='应用', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    status = forms.CharField(label='状态', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50,required=False)
    remark = forms.CharField(label='备注', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), max_length=50,required=False)


class OracleForm(forms.Form):
    service_name = forms.CharField(label='服务名', widget=forms.TextInput(attrs={'class': 'validate'}), max_length=50, required=True,error_messages={'required': u'请填写Oracle数据库服务名'})
    db_user = forms.CharField(label='用户', max_length=50, error_messages={'required': '请填写Oracle用户名'})
    db_password = forms.CharField(label='密码', widget=forms.PasswordInput, error_messages={'required': '请填写Oracle密码'})
    db_port = forms.CharField(label='端口', max_length=50, error_messages={'required': '请填写Oracle端口号'})

class OracleMetricForm(forms.Form):
    service_name = forms.CharField(label='服务名', widget=forms.TextInput(attrs={'class': 'validate'}), max_length=50, required=True,error_messages={'required': u'请填写Oracle数据库服务名'})
    db_user = forms.CharField(label='用户', max_length=50, error_messages={'required': '请填写Oracle用户名'})
    db_password = forms.CharField(label='密码', widget=forms.PasswordInput, error_messages={'required': '请填写Oracle密码'})
    db_port = forms.CharField(label='端口', max_length=50, error_messages={'required': '请填写Oracle端口号'})
