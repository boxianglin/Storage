# 基础查询

/*
语法:
Select 查询列表
from 表名；

特点:
1. 查询的列表可以是: 表中的字段, 常量值, 表达式, 函数
2. 查询的结果一个虚拟的表格
*/

#需要先选取对应的表
USE employees;

#查询表中的单个字段, 多个字段则逗号隔开
SELECT last_name FROM employees;

#查询表中全部信息
SELECT * FROM employees;

#可查询常量值
SELECT 100;
SELECT 'john';

#可查询表达式
SELECT 100%98;

#可查询函数
SELECT VERSION();

#可添加别名 (AS keyword can be deleted)
SELECT last_name AS 姓, first_name AS 名 FROM employees;

# 去重
# 查询总员工涉及的部门编号 (distinct keyword)
SELECT DISTINCT department_id FROM employees;

#+号的作用(只能做运算)(会转换string到integer)

# CoNCAT函数用来string拼接
SELECT CONCAT ('a','b') AS 结果;


SELECT CONCAT(last_name,first_name) AS 姓名 FROM employees;


#显示departments中的结构
DESC departments;



# 因为concat的参数如果有null, 即全为null, 如果要拼接需要对null进行判断
# if null, then 0
SELECT IFNULL (commission_pct,0) AS 奖金率, commission_pct FROM employees;

SELECT CONCAT (`first_name`,',',IFNULL(`commission_pct`,0))AS out_put FROM employees;

