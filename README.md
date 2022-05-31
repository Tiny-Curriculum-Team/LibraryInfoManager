# Tiny Library Information Management System

## Introduction

**Now it's on development.**

The repository is a Database Curriculum Design.

It's based on _**Python**_, _**Django**_ and _**MySQL**_.

## File Structure
```
LibraryInfoManager
├── ConnectionTemplate.py
├── InitDBToolkit.py
├── lib
│   └── utils.py
├── LICENSE
├── README.md
├── requirements.txt
└── SQLs
    └── InitDatabase.sql

2 directories, 7 files
```

## Table Structure

> The Bold properties are primary keys. And the Italic properties are foreign keys.

- Publisher(**PublisherID**, publisher_name)
- Book(**ISBN**, book_name, book_type, author, location, status, _PublisherID_)
- Reader(**ReaderID**, reader_name, user_name, password, account_status, tel, trustworthiness, max_borrow_day, max_borrow_count)
- Admin(**WorkID**, admin_name, user_name, password, tel)
- Borrow(**OperationID**, _ReaderID_, _ISBN_, borrow_time, status, give_back_time)
- Manage(**OperationID**, _WorkID_, _ISBN_, operate_type, operate_time)

<details>

```sql
mysql> desc Publisher;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| PublisherID    | int         | NO   | PRI | NULL    |       |
| publisher_name | varchar(40) | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> desc Book;
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| ISBN          | varchar(20) | NO   | PRI | NULL    |       |
| book_name     | varchar(40) | YES  |     | NULL    |       |
| book_type     | varchar(20) | YES  |     | NULL    |       |
| book_author   | varchar(16) | YES  |     | NULL    |       |
| book_location | varchar(80) | YES  |     | NULL    |       |
| book_status   | varchar(15) | YES  |     | NULL    |       |
| PublisherID   | int         | YES  | MUL | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> desc Reader;
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ReaderID         | varchar(20) | NO   | PRI | NULL    |       |
| reader_name      | varchar(40) | YES  |     | NULL    |       |
| user_name        | varchar(20) | YES  |     | NULL    |       |
| password         | varchar(40) | YES  |     | NULL    |       |
| account_status   | varchar(20) | YES  |     | NULL    |       |
| tel              | varchar(11) | YES  |     | NULL    |       |
| trustworthiness  | float       | YES  |     | NULL    |       |
| max_borrow_day   | int         | YES  |     | NULL    |       |
| max_borrow_count | int         | YES  |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> desc Admin;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| WorkID     | varchar(20) | NO   | PRI | NULL    |       |
| admin_name | varchar(40) | YES  |     | NULL    |       |
| user_name  | varchar(20) | YES  |     | NULL    |       |
| password   | varchar(40) | YES  |     | NULL    |       |
| tel        | varchar(11) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> desc Borrow;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| OperationID    | varchar(20) | NO   | PRI | NULL    |       |
| ReaderID       | varchar(20) | YES  | MUL | NULL    |       |
| ISBN           | varchar(20) | YES  | MUL | NULL    |       |
| borrow_time    | date        | YES  |     | NULL    |       |
| status         | varchar(80) | YES  |     | NULL    |       |
| give_back_time | varchar(15) | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> desc Manage;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| OperationID  | varchar(20) | NO   | PRI | NULL    |       |
| WorkID       | varchar(20) | YES  | MUL | NULL    |       |
| ISBN         | varchar(20) | YES  | MUL | NULL    |       |
| operate_type | varchar(20) | YES  |     | NULL    |       |
| operate_time | date        | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)
```

<summary>The Structure of each tables</summary>
</details>

## Credit System

> The max value of the credit is 100, and the min value is 0.

- When the book(s) got damaged, the user would lose 25. 
- When the book(s) got lost, the user have to compensate for the book. If not, he/she will get 0 credit. 
- When the book(s) got back late, the user would lose 10. And of course, if he/she didn't give back for too long, this scene would be seen as the book(s) got lost. 
- Only when the book(s) got back, the user could get 1.

**What's the Credit used for?**:

The credit can effect the max count of book(s) you can borrow and the longest time you can borrow book(s) for as well.

$$
\begin{aligned}
UserMaxCount &= \lfloor \frac{credit}{100} \times MaxCount \rfloor \\
UserLongestTime &= \lfloor \frac{credit}{100} \times LongestTime \rfloor
\end{aligned}
$$


## Usage

To use it, you shall run InitDBToolkit first. 

_**(On development so that the left are unconsidered.)**_