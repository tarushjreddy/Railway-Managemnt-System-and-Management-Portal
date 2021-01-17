
 
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;



CREATE TABLE `book_ticket` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `starting_point` varchar(200) DEFAULT NULL,
  `end_point` varchar(200) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `book_date` varchar(200) DEFAULT NULL,
  `j_date` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `enq` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,

  `starting_point` varchar(200) DEFAULT NULL,
  `end_point` varchar(200) DEFAULT NULL,
  `driverBatch` varchar(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `male_seats` int(11) NOT NULL,
  `female_seats` int(11) NOT NULL,
  `availability` int(11) NOT NULL,
  `currentDestination` varchar(200) DEFAULT NULL,
  `age` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
insert into enq 
values(1, "raajdhani", "del", "blr", "1", 1, 700, 400, 300, 700, "dep", 13);


CREATE TABLE `report` (
  `id` int(11) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `report` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `user_info` (
  `id` int(11) NOT NULL,
  `username` varchar(200) DEFAULT NULL,
  `pass` varchar(200) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE `book_ticket`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `report`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `user_info`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `book_ticket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `user_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
mysql> insert into enq  values(1, "MUM-->BLR", "MUM", "BLR", "1", 1, 700, 400, 300, 700, "MUM", 10);


mysql> insert into enq  values(1, "MUM<-->BLR(EXPRESS)", "MUM", "BLR", "1", 1, 700, 400, 300, 700, "MUM", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "MUM<-->KOL(EXPRESS)", "MUM", "KOL", "1", 1, 700, 400, 300, 700, "MUM", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "MUM<-->DEL(EXPRESS)", "MUM", "DEL", "1", 1, 700, 400, 300, 700, "MUM", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "MUM<-->DEL(EXPRESS)", "BLR", "DEL", "1", 1, 700, 400, 300, 700, "BLR", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "BLR<-->DEL(EXPRESS)", "BLR", "DEL", "1", 1, 700, 400, 300, 700, "BLR", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "BLR<-->DEL(EXPRESS)", "BLR", "MUM", "1", 1, 700, 400, 300, 700, "BLR", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "BLR<-->MUM(EXPRESS)", "BLR", "MUM", "1", 1, 700, 400, 300, 700, "BLR", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "BLR<-->KOL(EXPRESS)", "BLR", "KOL", "1", 1, 700, 400, 300, 700, "BLR", 10);
Query OK, 1 row affected (0.00 sec)

mysql> insert into enq  values(1, "DEL<-->KOL(EXPRESS)", "DEL", "KOL", "1", 1, 700, 400, 300, 700, "KOL", 10);