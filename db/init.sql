CREATE DATABASE IF NOT EXISTS `appmysql`;
USE `appmysql`;
CREATE TABLE IF NOT EXISTS `logs` (
    `id` int not null primary key auto_increment,
    `time` varchar(100),
    `ip` varchar(100)
);