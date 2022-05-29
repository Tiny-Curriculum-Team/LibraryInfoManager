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

 - Book(**ISBN**, name, type, author, location, status, _PublisherID_)
 - Reader(**ReaderID**, name, user_name, password, account_status, tel, trustworthiness, max_borrow_day, max_borrow_count)
 - Admin(**WorkID**, user_name, name, password)
 - Publisher(**PublisherID**, publisher_name)
 - Borrow(**OperationID**, _ReaderID_, _ISBN_, borrow_time, status, give_back_time)
 - Manage(**OperationID**, _WorkID_, _ISBN_, type, time)

## Usage

To use it, you shall run InitDBToolkit first. 

_**(On development so that the left are unconsidered.)**_