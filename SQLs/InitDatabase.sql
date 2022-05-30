drop database LIMS if exists LIMS;

create database LIMS CHARACTER SET utf8 COLLATE utf8_general_ci;

create table Publisher (
    PublisherID int,
    publisher_name varchar(40),
);

create table Book (
    ISBN varchar(20),
    name varchar(40),
    type varchar(20),
    author varchar(16),
    location varchar(80),
    status varchar(15),
    PublisherID int,
    PRIMARY KEY (ISBN),
    CONSTRAINT 'PublisherID' FOREIGN KEY (PublisherID) REFERENCES Publisher(PublisherID)
);

create table Reader (
    ReaderID varchar(20),
    user_name varchar(20),
    name varchar(40),
    password varchar(40),
    account_status varchar(20),
    tel varchar(11),
    trustworthiness float,
    max_borrow_day int,
    max_borrow_count int,
    PRIMARY KEY (ReaderID),
);

create table Admin (
    WorkID varchar(20),
    user_name varchar(20),
    name varchar(40),
    password varchar(40),
    tel varchar(11),
    PRIMARY KEY (WorkID),
);

create table Borrow (
    OperationID varchar(20),
    ReaderID varchar(20),
    ISBN varchar(20),
    borrow_time date,
    status varchar(80),
    give_back_time varchar(15),
    PRIMARY KEY (OperationID),
    CONSTRAINT 'ReaderID' FOREIGN KEY (ReaderID) REFERENCES Reader(ReaderID),
    CONSTRAINT 'BookID' FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

create table Manage (
    OperationID varchar(20),
    WorkID varchar(20),
    ISBN varchar(20),
    operate_type varchar (20),
    operate_time date,
    PRIMARY KEY (OperationID),
    CONSTRAINT 'AdminID' FOREIGN KEY (WorkID) REFERENCES Admin(WorkID),
    CONSTRAINT 'BookID' FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);