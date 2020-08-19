create table books
(id int primary key auto_increment,bname varchar(30) not null,
writer varchar(25) not null,publisher varchar(50) comment"出版社",
price float unsigned,`comment` text);

insert into books(bname,writer,publisher,price,comment) values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","人民教育出版社",44,"你心中的围城是什么");

insert into books(bname,writer,publisher,price)
values
("林家铺子","茅盾","中国文学出版社",51),
("巨人传","忘了","人民教育出版社",47);
+----+--------------+-----------+-----------------------+-------+-----------------------------+
| id | bname        | writer    | publisher             | price | comment                     |
+----+--------------+-----------+-----------------------+-------+-----------------------------+
|  1 | 边城         | 沈从文    | 机械工业出版社        |    36 | 小城故事多                  |
|  2 | 骆驼祥子     | 老舍      | 机械工业出版社        |    43 | 你是祥子么                  |
|  3 | 茶馆         | 老舍      | 中国文学出版社        |    55 | 老北京                      |
|  4 | 呐喊         | 鲁迅      | 人民教育出版社        |    71 | 最后的声音                  |
|  5 | 朝花夕拾     | 鲁迅      | 中国文学出版社        |    53 | 好时光                      |
|  6 | 围城         | 钱钟书    | 人民教育出版社        |    44 | 你心中的围城是什么          |
|  7 | 林家铺子     | 茅盾      | 中国文学出版社        |    51 | NULL                        |
|  8 | 巨人传       | 忘了      | 人民教育出版社        |    47 | NULL                        |
+----+--------------+-----------+-----------------------+-------+-----------------------------+
--查找训练:
--查找30多元的图书
select * from books where price>=30 and price<40;
select * from books where price between 30 and 40;
--查找人民教育出版社出版的图书
select * from books where publisher="人民教育出版社";
--查找老舍写的,中国文学出版社出版的
select * from books where writer="老舍" and publisher="中国文学出版社";
--查找备注不为空的
select * from books where remark is not null;
--查找70多元的,只看书名和价格
select bname,price from books where price between 70 and 80;
--查找鲁迅写的或者茅盾写的图书
select * from books where writer="鲁迅" or writer="茅盾";


1. 将呐喊价格改为45
update books set price=45 where bname="呐喊";
2. 修改所有老舍的作品,增加5元
update books set price = price+5 where writer="老舍";
3. 修改价格字段数据类型为 decimal(5,2)
alter table books modify price decimal(5,2);
4. 增加一个字段,字段名为出版时间,类型为date 在价格后
alter table books add publication_date date after price;
5. 将所有老舍的作品出版时间改为 2016-10-1
update books set publication_date="2016-10-1" where writer="老舍";
6. 修改所有中国文学出版社图书出版时间为2018-10-1
   但是不要修改老舍的
   update books set publication_date="2018-10-1" where publisher="中国文学出版社"
   and writer !="老舍";
7. 修改所有出版时间为null的改为2020-1-1
update books set publication_date="2020-1-1" where publication_date is null;
8. 删除所有价格超过70元的图书
delete from books where price>70;
insert into books(bname,writer,publisher,price)
values
("平凡的世界","路遥","中国文学出版社",82),
("格列佛游记","忘了","人民教育出版社",90);



创建数据表  sanguo

id  name  gender  country  attack  defense

create table sanguo(
id int primary key auto_increment,
name varchar(30),
gender enum('男','女'),
country enum('魏','蜀','吴'),
attack smallint,
defense tinyint
);

insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);

1. 查找所有蜀国人信息,按照攻击力排名
select * from sanguo where country="蜀" order by attack;

2. 将赵云攻击力设为360 防御设为70
update sanguo set attack=360,defense=70 where name="赵云";
3. 将吴国英雄攻击力超过300的改为300,最多改2个
update sanguo set attack=300 where attack>300 and country="吴" limit 2;
4. 查找攻击力超过200的魏国英雄名字和攻击力,
   并且显示为姓名  攻击力
   select name as 名字,attack as 攻击力 from sanguo
   where attack>200 and country="魏";
5. 所有英雄按照攻击力降序排序,如果攻击力相同则
   按照防御降序排序
   select * from sanguo order by attack desc,defense desc;
6. 查找名字为3个字的英雄
select * from sanguo where name like "___";
7. 查找比魏国攻击力最高的人攻击力还要高的蜀国英雄
select * from sanguo where attack>(select attack from sanguo
where country="魏" order by attack desc limit 1) and country="蜀";
8. 找到魏国防御力排名前2的英雄
select * from sanguo where country="魏" order by defense desc limit 2;
9. 查找所有女性角色同时查找所有男性角色中攻击力少于
   250的
   select * from sanguo where gender="女" union
   select * from sanguo where attack < 250 and gender="男";

   select * from sanguo where gender="女" or gender="男" and attack<250;




练习1: 使用books 表完成
1. 统计每位作家图书的平均价格
select writer,avg(price) from books group by writer;

2. 统计每个出版社出版图书的数量
select publisher,count(*) from books group by publisher;

3. 查看总共有多少个出版社
select count(distinct publisher) from books;

4. 筛选出那些出版过超过50元的图书的出版社,并按照其
出版图书的平均价格降序排序
select publisher,avg(price) from books where price>50 group by publisher
order by avg(price) desc;

方法二:
select publisher,avg(price) from books
group by publisher
having max(price) >= 50
order by avg(price) desc;

5. 统计相同时间出版图书的最高价格和最低价格
select publication_date,max(price),min(price) from books group by publication_date;



