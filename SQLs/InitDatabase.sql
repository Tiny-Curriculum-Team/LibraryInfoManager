create table Publisher (
    PublisherID int,
    publisher_name varchar(40) not null,
    PRIMARY KEY (PublisherID)
);

create table BookType (
    BookTypeID int,
    book_type_name varchar(40) not null,
    PRIMARY KEY (BookTypeID)
);

create table Book (
    ISBN varchar(20),
    book_name varchar(40) not null,
    book_type_id int not null,
    author varchar(40) not null,
    location varchar(80) not null,
    status varchar(7) default 'IN' not null CHECK (status in ('IN', 'OUT', 'LOST')),
    PublisherID int not null,
    PRIMARY KEY (ISBN),
    FOREIGN KEY (PublisherID) REFERENCES Publisher(PublisherID),
    FOREIGN KEY (book_type_id) REFERENCES BookType(BookTypeID)
);

create table Reader (
    ReaderID varchar(20),
    reader_name varchar(40) not null,
    user_name varchar(20) not null,
    password varchar(1024) not null,
    account_status varchar(20) default 'NORMAL' not null CHECK (account_status in ('NORMAL', 'DELETED')),
    tel varchar(11) not null,
    trustworthiness int default 100 not null CHECK (trustworthiness between 0 and 100),
    max_borrow_day int not null,
    max_borrow_count int not null,
    PRIMARY KEY (ReaderID)
);

create table Administrator (
    WorkID int,
    admin_name varchar(40) not null,
    user_name varchar(20) not null,
    password varchar(1024) not null,
    tel varchar(11) not null,
    PRIMARY KEY (WorkID)
);

create table Borrow (
    OperationID varchar(20),
    ReaderID varchar(20) not null,
    ISBN varchar(20) not null,
    borrow_time date not null,
    status varchar(7) not null CHECK (status in ('BORROWED', 'BACK')),
    give_back_time date,
    PRIMARY KEY (OperationID),
    FOREIGN KEY (ReaderID) REFERENCES Reader(ReaderID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

create table Manage (
    OperationID varchar(20),
    WorkID int not null,
    ISBN varchar(20) not null,
    operate_type varchar (20) not null,
    operate_time date not null,
    PRIMARY KEY (OperationID),
    FOREIGN KEY (WorkID) REFERENCES Administrator(WorkID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);