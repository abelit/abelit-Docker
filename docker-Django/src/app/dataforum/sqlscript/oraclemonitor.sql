1.数据库版本查询
select * from v$version where rownum<=1;

2.查看数据库基本信息及状态
select dbid,name,open_mode,log_mode from v$database;
判断数据库是否能登陆
select user from dual;
