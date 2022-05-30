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
│   ├── SQLs.py
│   └── utils.py
├── LICENSE
├── README.md
└── requirements.txt

1 directory, 7 files
```

## Table Structure

> The Bold properties are primary keys. And the Italic properties are foreign keys.

 - Book(**ISBN**, name, type, author, location, status, _PublisherID_)
 - Reader(**ReaderID**, name, user_name, password, account_status, tel, trustworthiness, max_borrow_day, max_borrow_count)
 - Admin(**WorkID**, user_name, name, password)
 - Publisher(**PublisherID**, publisher_name)
 - Borrow(**OperationID**, _ReaderID_, _ISBN_, borrow_time, status, give_back_time)
 - Manage(**OperationID**, _WorkID_, _ISBN_, type, time)

## Credit System

> The max value of the credit is 100, and the min value is 0.

 - When the book(s) got damaged, the user would lose 25. 
 - When the book(s) got lost, the user have to compensate for the book. If not, he/she will get 0 credit. 
 - When the book(s) got back late, the user would lose 10. And of course, if he/she didn't give back for too long, this scene would be seen as the book(s) got lost. 
 - Only when the book(s) got back, the user could get 1.

**What's the Credit used for?**:

The credit can effect the max count of book(s) you can borrow and the longest time you can borrow book(s) for as well.
$$
USER_MAX_COUNT = \lfloor \frac{credit}{100} \times MAX_COUNT \rfloor
USER_LONGEST_TIME = \lfloor \frac{credit}{100} \times LONGEST_TIME \rfloor
$$


## Usage

To use it, you shall run InitDBToolkit first. 

_**(On development so that the left are unconsidered.)**_