-- Create statements for tables "developer_details", "devops_details" , "tester_details" and "pipeline_load_date".

CREATE TABLE `datapipeline_db`.`developer_details` (
  `Id` VARCHAR(20) NOT NULL,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(50) NOT NULL,
  `DOB` DATE NOT NULL,
  `CreatedDate` DATETIME DEFAULT NULL,
  `Salary` BIGINT,
  `WorkLocation` VARCHAR(50) DEFAULT NULL,
  `Designation` VARCHAR(50) DEFAULT NULL,
  `LastModifiedDate` DATETIME DEFAULT NULL,
  `insert_date` DATETIME DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `datapipeline_db`.`devops_details` (
  `Id` VARCHAR(20) NOT NULL,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(50) NOT NULL,
  `DOB` DATE NOT NULL,
  `CreatedDate` DATETIME DEFAULT NULL,
  `Salary` BIGINT,
  `WorkLocation` VARCHAR(50) DEFAULT NULL,
  `Designation` VARCHAR(50) DEFAULT NULL,
  `LastModifiedDate` DATETIME DEFAULT NULL,
  `insert_date` DATETIME DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `datapipeline_db`.`tester_details` (
  `Id` VARCHAR(20) NOT NULL,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(50) NOT NULL,
  `DOB` DATE NOT NULL,
  `CreatedDate` DATETIME DEFAULT NULL,
  `Salary` BIGINT,
  `WorkLocation` VARCHAR(50) DEFAULT NULL,
  `Designation` VARCHAR(50) DEFAULT NULL,
  `LastModifiedDate` DATETIME DEFAULT NULL,
  `insert_date` DATETIME DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `datapipeline_db`.`pipeline_load_date` (
  `id` int NOT NULL AUTO_INCREMENT,
  `table_name` VARCHAR(255) DEFAULT NULL,
  `max_date` DATETIME DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- INSERT query for modified date table
INSERT INTO `pipeline_load_date` (table_name) values('developer_details');
INSERT INTO `pipeline_load_date` (table_name) values('devops_details');
INSERT INTO `pipeline_load_date` (table_name) values('tester_details');
