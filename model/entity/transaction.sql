create table mft.transaction_tbl
(
    id                  int primary key auto_increment,
    status              varchar(30),
    amount              float(12),
    datetime           datetime(6),
    source_account      varchar(30),
    destination_account varchar(30)
);

