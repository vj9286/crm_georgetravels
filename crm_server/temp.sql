-- MySQL dump 10.13  Distrib 5.7.26, for osx10.14 (x86_64)
--
-- Host: localhost    Database: crm
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'Accounts'),(5,'Admin'),(3,'Agent'),(8,'Documentation'),(7,'Payment'),(4,'SuperAdmin'),(1,'Ticketing'),(6,'Tour');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add booking',7,'add_booking'),(26,'Can change booking',7,'change_booking'),(27,'Can delete booking',7,'delete_booking'),(28,'Can view booking',7,'view_booking'),(29,'Can add notes',8,'add_notes'),(30,'Can change notes',8,'change_notes'),(31,'Can delete notes',8,'delete_notes'),(32,'Can view notes',8,'view_notes'),(33,'Can add Car Booking',9,'add_carbookingproxy'),(34,'Can change Car Booking',9,'change_carbookingproxy'),(35,'Can delete Car Booking',9,'delete_carbookingproxy'),(36,'Can view Car Booking',9,'view_carbookingproxy'),(37,'Can add history',10,'add_history'),(38,'Can change history',10,'change_history'),(39,'Can delete history',10,'delete_history'),(40,'Can view history',10,'view_history'),(41,'Can add flight',11,'add_flight'),(42,'Can change flight',11,'change_flight'),(43,'Can delete flight',11,'delete_flight'),(44,'Can view flight',11,'view_flight'),(45,'Can add passenger',12,'add_passenger'),(46,'Can change passenger',12,'change_passenger'),(47,'Can delete passenger',12,'delete_passenger'),(48,'Can view passenger',12,'view_passenger'),(49,'Can add airline',13,'add_airline'),(50,'Can change airline',13,'change_airline'),(51,'Can delete airline',13,'delete_airline'),(52,'Can view airline',13,'view_airline'),(53,'Can add car booking',14,'add_carbooking'),(54,'Can change car booking',14,'change_carbooking'),(55,'Can delete car booking',14,'delete_carbooking'),(56,'Can view car booking',14,'view_carbooking'),(57,'Can add hotel',15,'add_hotel'),(58,'Can change hotel',15,'change_hotel'),(59,'Can delete hotel',15,'delete_hotel'),(60,'Can view hotel',15,'view_hotel'),(61,'Can add cruise hire',16,'add_cruisehire'),(62,'Can change cruise hire',16,'change_cruisehire'),(63,'Can delete cruise hire',16,'delete_cruisehire'),(64,'Can view cruise hire',16,'view_cruisehire'),(65,'Can add tour booking',17,'add_tourbooking'),(66,'Can change tour booking',17,'change_tourbooking'),(67,'Can delete tour booking',17,'delete_tourbooking'),(68,'Can view tour booking',17,'view_tourbooking'),(69,'Can add package',18,'add_package'),(70,'Can change package',18,'change_package'),(71,'Can delete package',18,'delete_package'),(72,'Can view package',18,'view_package'),(73,'Can add payments',19,'add_payments'),(74,'Can change payments',19,'change_payments'),(75,'Can delete payments',19,'delete_payments'),(76,'Can view payments',19,'view_payments'),(77,'Can add payments made',20,'add_paymentsmade'),(78,'Can change payments made',20,'change_paymentsmade'),(79,'Can delete payments made',20,'delete_paymentsmade'),(80,'Can view payments made',20,'view_paymentsmade'),(81,'Can add payment received',21,'add_paymentreceived'),(82,'Can change payment received',21,'change_paymentreceived'),(83,'Can delete payment received',21,'delete_paymentreceived'),(84,'Can view payment received',21,'view_paymentreceived');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$GLhVc1GVQ0Lj$+yYjO+LJxMBP7bQ1yLUeVAI73cWuuRYKXobjgrGkUEU=','2019-09-10 15:45:46.038862',1,'abhi','','','',1,1,'2019-07-07 07:53:15.000000'),(2,'pbkdf2_sha256$150000$8w5AgcftzUjy$HLA6vVT87S0PpjP7VHKpPEHB5dwmwtlCQoTAMcE5qPk=','2019-09-10 16:40:52.069885',0,'agent_test1','','','',1,1,'2019-07-21 14:55:11.000000'),(3,'pbkdf2_sha256$150000$Wfo1zXSXOpNE$f5p7hasSIVSyICPc/dunBhfVmQkK0JetdIfCSbiH49g=','2019-09-10 16:32:57.450371',0,'abhi_tour','','','',1,1,'2019-09-10 14:47:15.000000'),(4,'pbkdf2_sha256$150000$GcNwXNj6H7sR$8wxVKtTPqmzqG8iHmHDbERyf0ObuAqJK1r6kryst8pI=',NULL,0,'abhi_payment','','','',1,1,'2019-09-10 14:48:02.000000'),(5,'pbkdf2_sha256$150000$K4iNJVzU1NrI$eO/ZHHxag05ECTPOADlzKp67Cw+SREg+RvWwEB1A+NE=',NULL,0,'abhi_accounts','','','',1,1,'2019-09-10 14:49:25.000000'),(6,'pbkdf2_sha256$150000$KG7OwQTgx59e$oFOJu8n6PJDjeC6rsGzVBNJIa3ZCNRy9x01JXq3/56Y=',NULL,0,'abhi_ticketing','','','',1,1,'2019-09-10 14:50:03.000000'),(7,'pbkdf2_sha256$150000$kpVVgcSRXAIb$dO8Fng+rHfoxw5wbb5qdmpk0XdNpofnsM2uoTA+/zcg=','2019-09-10 14:54:17.586806',0,'abhi_documentation','','','',1,1,'2019-09-10 14:50:28.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (3,1,1),(4,1,2),(5,1,3),(2,1,4),(6,1,5),(7,1,6),(8,1,7),(9,1,8),(1,2,3),(11,3,6),(10,4,7),(12,5,2),(13,6,1),(14,7,8);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,2,11),(12,2,12),(13,2,13),(14,2,14),(15,2,15),(16,2,16),(17,2,17),(18,2,18),(19,2,19),(20,2,20),(21,2,21),(22,2,22),(23,2,23),(24,2,24),(25,2,25),(26,2,26),(27,2,27),(28,2,28),(29,2,29),(30,2,30),(31,2,31),(32,2,32),(33,2,33),(34,2,34),(35,2,35),(36,2,36),(37,2,37),(38,2,38),(39,2,39),(40,2,40),(41,2,41),(42,2,42),(43,2,43),(44,2,44),(45,2,45),(46,2,46),(47,2,47),(48,2,48),(49,2,49),(50,2,50),(51,2,51),(52,2,52),(53,2,53),(54,2,54),(55,2,55),(56,2,56),(57,2,57),(58,2,58),(59,2,59),(60,2,60),(61,2,61),(62,2,62),(63,2,63),(64,2,64),(65,2,65),(66,2,66),(67,2,67),(68,2,68),(69,2,69),(70,2,70),(71,2,71),(72,2,72),(73,2,73),(74,2,74),(75,2,75),(76,2,76),(77,2,77),(78,2,78),(79,2,79),(80,2,80),(81,2,81),(82,2,82),(83,2,83),(84,2,84),(86,3,45),(87,3,46),(88,3,47),(85,3,48);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings_booking`
--

DROP TABLE IF EXISTS `bookings_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookings_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `booking_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `added_date` datetime(6) NOT NULL,
  `booking_agent_id` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bookings_booking_booking_agent_id_d155543c_fk_auth_user_id` (`booking_agent_id`),
  CONSTRAINT `bookings_booking_booking_agent_id_d155543c_fk_auth_user_id` FOREIGN KEY (`booking_agent_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings_booking`
--

LOCK TABLES `bookings_booking` WRITE;
/*!40000 ALTER TABLE `bookings_booking` DISABLE KEYS */;
INSERT INTO `bookings_booking` VALUES (1,'GT-ABH07190172','ABhiTest','2019-07-07 08:45:04.161787',1,1),(2,'GT-ABH07190230','Abhisharma','2019-07-13 08:08:22.312892',1,2),(3,'GT-ABH07190389','AbhiSharmaTest','2019-07-13 12:58:42.599010',1,1),(4,'GT-VZV07190478','vzvff','2019-07-13 16:43:39.626365',1,1),(5,'GT-ABH07190530','ABhiTest','2019-07-21 15:24:35.196918',2,1);
/*!40000 ALTER TABLE `bookings_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings_history`
--

DROP TABLE IF EXISTS `bookings_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookings_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(10) unsigned NOT NULL,
  `remarks` varchar(10000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `operation` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `added_timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bookings_history_content_type_id_c0a06574_fk_django_co` (`content_type_id`),
  KEY `bookings_history_user_id_e70163e2_fk_auth_user_id` (`user_id`),
  CONSTRAINT `bookings_history_content_type_id_c0a06574_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `bookings_history_user_id_e70163e2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings_history`
--

LOCK TABLES `bookings_history` WRITE;
/*!40000 ALTER TABLE `bookings_history` DISABLE KEYS */;
INSERT INTO `bookings_history` VALUES (1,1,'Created',11,1,1,'2019-07-07 08:45:04.176564'),(2,1,'Created',11,1,1,'2019-07-07 08:45:04.181983'),(3,1,'Created',11,1,1,'2019-07-07 08:45:04.184271'),(4,1,'Created',15,1,1,'2019-07-07 08:46:14.415015'),(5,1,'Created',17,1,1,'2019-07-08 15:38:08.759771'),(6,1,'arr_airport:Old Value:1332, New Value: DNN',13,2,1,'2019-07-13 06:03:31.279258'),(7,2,'Created',17,1,1,'2019-07-13 07:59:32.873441'),(8,3,'Created',17,1,1,'2019-07-13 07:59:42.211001'),(9,1,'date:Old Value:2019-07-23, New Value: None',17,2,1,'2019-07-13 08:02:14.186247'),(10,2,'total_net:Old Value:0.0, New Value: 100.0total_gross:Old Value:0.0, New Value: 100.0',17,2,1,'2019-07-13 08:02:53.550109'),(11,1,'no_of_nights:Old Value:2.0, New Value: 22.0star_cat:Old Value:3 Star, New Value: 3 Star selectedno_rooms:Old Value:2.0, New Value: 12.0net_per_stay:Old Value:24.0, New Value: 264.0gross_per_stay:Old Value:24.0, New Value: 264.0total_net:Old Value:48.0, New Value: 3168.0total_gross:Old Value:48.0, New Value: 3168.0',15,2,1,'2019-07-13 08:05:31.805168'),(12,2,'Created',11,1,1,'2019-07-13 08:08:22.352840'),(13,2,'Created',11,1,1,'2019-07-13 08:08:22.358418'),(14,2,'Created',11,1,1,'2019-07-13 08:08:22.361148'),(15,2,'arr_airport:Old Value:1332, New Value: 312312',13,2,1,'2019-07-13 08:08:43.569254'),(16,3,'flight_net_other:Old Value:0.0, New Value: 100.0',18,2,1,'2019-07-13 08:33:46.746939'),(17,3,'hotel_net_other:Old Value:0.0, New Value: 100.0',18,2,1,'2019-07-13 08:33:53.709723'),(18,3,'hotel_net_other:Old Value:100.0, New Value: 140.0',18,2,1,'2019-07-13 08:35:21.298602'),(19,3,'hotel_net_other:Old Value:140.0, New Value: 10.0',18,2,1,'2019-07-13 08:35:27.323006'),(20,3,'hotel_net_other:Old Value:10.0, New Value: 100.0',18,2,1,'2019-07-13 08:35:33.123714'),(21,1,'Created',19,1,1,'2019-07-13 11:20:52.028480'),(22,1,'address:Old Value:39/17 (9-A), Muir Road, Prayagraj, New Value: expiry_year:Old Value:2018, New Value: 01due_date:Old Value:None, New Value: 2019-07-24',19,2,1,'2019-07-13 11:21:59.486873'),(23,2,'Created',19,1,1,'2019-07-13 11:22:53.368998'),(24,1,'expiry_month:Old Value:01, New Value: 07expiry_year:Old Value:01, New Value: 2024due_date:Old Value:2019-07-24, New Value: None',19,2,1,'2019-07-13 11:23:23.782701'),(25,1,'expiry_month:Old Value:07, New Value: 02expiry_year:Old Value:2024, New Value: 2023',19,2,1,'2019-07-13 11:23:35.006135'),(26,1,'address:Old Value:, New Value: dkasdlkamsdkasexpiry_month:Old Value:02, New Value: 01expiry_year:Old Value:2023, New Value: 02',19,2,1,'2019-07-13 11:23:49.839071'),(27,1,'address:Old Value:dkasdlkamsdkas, New Value: expiry_year:Old Value:02, New Value: 2022',19,2,1,'2019-07-13 11:24:43.935781'),(28,1,'expiry_month:Old Value:01, New Value: 05expiry_year:Old Value:2022, New Value: 2026',19,2,1,'2019-07-13 11:24:50.849186'),(29,1,'address:Old Value:, New Value: sadasdas',19,2,1,'2019-07-13 11:26:07.489778'),(30,1,'name_on_card:Old Value:None, New Value: asdasdas',19,2,1,'2019-07-13 11:28:41.860354'),(31,1,'amount:Old Value:, New Value: 12surcharge:Old Value:, New Value: 12',19,2,1,'2019-07-13 11:29:16.427744'),(32,1,'security_code:Old Value:None, New Value: 12',19,2,1,'2019-07-13 11:29:46.239649'),(33,1,'first_four:Old Value:, New Value: 1211second_four:Old Value:, New Value: 1212third_four:Old Value:, New Value: 1312fourth_four:Old Value:, New Value: 3123',19,2,1,'2019-07-13 11:29:53.153192'),(34,2,'name_on_card:Old Value:None, New Value: Onkar security_code:Old Value:None, New Value: Nonedue_date:Old Value:2019-07-31, New Value: None',19,2,1,'2019-07-13 11:30:04.231562'),(35,2,'Created',15,1,1,'2019-07-13 11:33:04.719199'),(36,3,'Created',11,1,1,'2019-07-13 12:58:42.653080'),(37,3,'Created',11,1,1,'2019-07-13 12:58:42.655967'),(38,3,'Created',11,1,1,'2019-07-13 12:58:42.659303'),(39,3,'adult_total:Old Value:24.0, New Value: 48.0adult_gross_total:Old Value:24.0, New Value: 48.0net:Old Value:24.0, New Value: 48.0gross:Old Value:24.0, New Value: 48.0',11,2,1,'2019-07-13 13:51:39.468037'),(40,3,'arr_airport:Old Value:1332, New Value: 312312',13,2,1,'2019-07-13 13:51:39.478721'),(41,4,'Created',12,1,1,'2019-07-13 13:51:39.494526'),(42,4,'Created',11,1,1,'2019-07-13 16:43:39.653441'),(43,4,'Created',11,1,1,'2019-07-13 16:43:39.655652'),(44,4,'Created',11,1,1,'2019-07-13 16:43:39.658022'),(45,4,'arr_airport:Old Value:sfa, New Value: dd',13,2,1,'2019-07-13 16:44:36.947086'),(46,5,'Created',13,1,1,'2019-07-13 16:44:36.949415'),(50,5,'arr_airport:Old Value:sdgs, New Value: ggsg',13,2,1,'2019-07-13 16:49:57.037698'),(59,3,'Created',15,1,1,'2019-07-13 16:55:39.473779'),(60,4,'Created',15,1,1,'2019-07-13 16:56:57.964659'),(61,10,'Created',11,1,1,'2019-07-13 16:57:19.124287'),(62,12,'Created',13,1,1,'2019-07-13 16:57:19.128779'),(63,6,'Created',12,1,1,'2019-07-13 16:57:19.134458'),(64,1,'Created',14,1,1,'2019-07-13 16:59:24.656682'),(65,1,'dob:Old Value:2019-07-23, New Value: Nonebooking_date:Old Value:2019-07-29, New Value: Nonecancellation_date:Old Value:2019-07-31, New Value: Nonebalance_due_date:Old Value:2019-07-22, New Value: Nonevat_id:Old Value:None, New Value: None',14,2,1,'2019-07-16 17:33:20.845385'),(66,1,'vat_id:Old Value:None, New Value: abcd',14,2,1,'2019-07-16 17:33:26.268635'),(67,5,'atol:Old Value:0.0, New Value: 12.0',18,2,1,'2019-07-21 09:33:47.956575'),(68,5,'insurance:Old Value:0.0, New Value: 12.0',18,2,1,'2019-07-21 09:34:40.507647'),(69,5,'commission:Old Value:0.0, New Value: 19.0',18,2,1,'2019-07-21 09:34:46.586355'),(70,5,'admin_charges:Old Value:0.0, New Value: 10.0',18,2,1,'2019-07-21 09:39:15.334580'),(71,11,'Created',11,1,2,'2019-07-21 15:24:35.264116'),(72,11,'Created',11,1,2,'2019-07-21 15:24:35.266688'),(73,11,'Created',11,1,2,'2019-07-21 15:24:35.268901'),(74,11,'adult_total:Old Value:24.0, New Value: 0.0adult_gross_total:Old Value:24.0, New Value: 0.0net:Old Value:24.0, New Value: 0.0gross:Old Value:24.0, New Value: 0.0',11,2,1,'2019-07-22 14:50:52.337628'),(75,13,'arr_airport:Old Value:1332, New Value: 312312',13,2,1,'2019-07-22 14:50:52.354635'),(76,7,'dob:Old Value:2019-07-30, New Value: 2016-07-04age_group:Old Value:Adult, New Value: Infant',12,2,1,'2019-07-22 14:50:52.365233'),(77,5,'Created',15,1,1,'2019-07-22 15:01:39.632343'),(78,5,'star_cat:Old Value:3 Star, New Value: 3 Star selectedbooking_date:Old Value:2019-07-22, New Value: Nonecancellation_date:Old Value:2019-07-26, New Value: Nonebalance_due_date:Old Value:2019-07-27, New Value: None',15,2,1,'2019-07-22 15:01:48.551508'),(79,2,'Created',14,1,1,'2019-07-22 15:04:34.130013'),(80,3,'Created',19,1,1,'2019-07-22 15:06:41.607465'),(81,6,'flight_net_other:Old Value:0.0, New Value: 15.0hotel_net_other:Old Value:0.0, New Value: 350.0cruise_net_other:Old Value:0.0, New Value: 50.0admin_charges:Old Value:0.0, New Value: 10.0',18,2,1,'2019-07-22 17:04:21.060863'),(82,2,'star_cat:Old Value:3 Star, New Value: 3 Star selectedbalance_due_date:Old Value:None, New Value: 2019-07-25',15,2,1,'2019-07-24 17:08:51.382675'),(83,2,'star_cat:Old Value:3 Star selected, New Value: 3 Star selected selectedbalance_due_date:Old Value:2019-07-25, New Value: 2019-07-24',15,2,1,'2019-07-24 17:19:07.087262'),(84,5,'room_cat:Old Value:, New Value: kmlknboard_basis:Old Value:Full Board, New Value: All Exclusivestar_cat:Old Value:3 Star selected, New Value: 3 Star selected selected',15,2,1,'2019-08-13 13:57:36.815681'),(85,1,'security_code:Old Value:12, New Value: 124',19,2,1,'2019-09-09 20:59:29.553703'),(86,2,'security_code:Old Value:None, New Value: 123amount:Old Value:sda, New Value: 1321surcharge:Old Value:3123, New Value: 312',19,2,1,'2019-09-09 20:59:44.377414');
/*!40000 ALTER TABLE `bookings_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings_notes`
--

DROP TABLE IF EXISTS `bookings_notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookings_notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) NOT NULL,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bookings_notes_booking_id_88d9bea0_fk_bookings_booking_id` (`booking_id`),
  CONSTRAINT `bookings_notes_booking_id_88d9bea0_fk_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings_notes`
--

LOCK TABLES `bookings_notes` WRITE;
/*!40000 ALTER TABLE `bookings_notes` DISABLE KEYS */;
INSERT INTO `bookings_notes` VALUES (1,4,'jnsdkjnasd'),(2,4,'THis is a test\r\n'),(3,4,'this is a test\r\n'),(4,4,'testing if notes work'),(5,4,'testing if notes work'),(6,5,'payment received'),(7,5,'call back needed on 29 aug');
/*!40000 ALTER TABLE `bookings_notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings_paymentreceived`
--

DROP TABLE IF EXISTS `bookings_paymentreceived`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookings_paymentreceived` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_fund_received` date DEFAULT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `transaction_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gross_amount` double NOT NULL,
  `surcharge` double NOT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bookings_paymentrece_booking_id_2bd93d5e_fk_bookings_` (`booking_id`),
  CONSTRAINT `bookings_paymentrece_booking_id_2bd93d5e_fk_bookings_` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings_paymentreceived`
--

LOCK TABLES `bookings_paymentreceived` WRITE;
/*!40000 ALTER TABLE `bookings_paymentreceived` DISABLE KEYS */;
INSERT INTO `bookings_paymentreceived` VALUES (1,'2019-07-15','Testing','abhijeet',123,3123,4),(2,'2019-07-15','Testing','abhi test',12312321,3123,4),(3,'2019-07-01','Testing','sdjaasdnajsn',1312,3123,4),(4,'2019-07-16','Testing','sdjaasdnajsn',1312,3123,4),(5,'2019-07-27','Testing','sdjaasdnajsn',1312,3123,4),(6,'2019-07-29','Testing','sdjaasdnajsn',1312,3123,4),(7,'2019-07-30','Testing','sdjaasdnajsn',11,123,4),(8,'2019-07-09','500','fff2132566',450,2,3);
/*!40000 ALTER TABLE `bookings_paymentreceived` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings_paymentsmade`
--

DROP TABLE IF EXISTS `bookings_paymentsmade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookings_paymentsmade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier_reference` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `supplier_amount` double NOT NULL,
  `supplier_paid` double NOT NULL,
  `supplier_balance` double NOT NULL,
  `supplier_balance_date` date DEFAULT NULL,
  `cancellation_date` date DEFAULT NULL,
  `vat_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bookings_paymentsmade_booking_id_737bb362_fk_bookings_booking_id` (`booking_id`),
  CONSTRAINT `bookings_paymentsmade_booking_id_737bb362_fk_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings_paymentsmade`
--

LOCK TABLES `bookings_paymentsmade` WRITE;
/*!40000 ALTER TABLE `bookings_paymentsmade` DISABLE KEYS */;
INSERT INTO `bookings_paymentsmade` VALUES (1,'asdas','dasdas','Testing','2019-08-05',13,3123,312,'2019-07-30','2019-08-05','',4),(2,'asdas','dasdas','Testing','2019-08-05',13,3123,312,'2019-07-30','2019-08-05','',4),(3,'asdas','dasdas','Testing','2019-07-30',13,3123,312,'2019-07-02','2019-07-29','abcd',4),(4,'Holiday team','12333555','taps','2019-07-22',200,100,100,'2019-07-27','2019-07-27','1',3);
/*!40000 ALTER TABLE `bookings_paymentsmade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_booking_carbooking`
--

DROP TABLE IF EXISTS `car_booking_carbooking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car_booking_carbooking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `car_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pickup_time` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `drop_off_time` date DEFAULT NULL,
  `num_days` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `car_category` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `insurance_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `num_cars` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `net_per_night` double DEFAULT NULL,
  `total_net` double DEFAULT NULL,
  `gross_per_night` double DEFAULT NULL,
  `total_gross` double DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `balance_due_date` date DEFAULT NULL,
  `booked_by` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `cancellation_date` date DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `contact_number` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `country` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `deposit_paid` double NOT NULL,
  `dob` date DEFAULT NULL,
  `drop_off_location` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `lead_driver` double DEFAULT NULL,
  `payment_due` double NOT NULL,
  `pickup_location` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `rental_company` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier_ref` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `total_car_rental_gross` double DEFAULT NULL,
  `total_car_rental_net` double DEFAULT NULL,
  `vat_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `drop_off_date` date DEFAULT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pickup_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `car_booking_carbooki_booking_id_72b3c889_fk_bookings_` (`booking_id`),
  CONSTRAINT `car_booking_carbooki_booking_id_72b3c889_fk_bookings_` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_booking_carbooking`
--

LOCK TABLES `car_booking_carbooking` WRITE;
/*!40000 ALTER TABLE `car_booking_carbooking` DISABLE KEYS */;
INSERT INTO `car_booking_carbooking` VALUES (1,'bxcbxb','bbbc',NULL,'1','bxbbx','bfdfdb','3663',364636,364636,666236,666236,4,'sdggsdgs',NULL,'4636',NULL,NULL,'cxcxbx','532636','dhdh',55,NULL,'dbb',0,55,'xcbbcb','fddfh','dfhfdh','dhdhd',2440422468,1335661668,'abcd','2019-07-23','dbdsh','2019-07-24'),(2,'stnd','12',NULL,'12','stana','fully insurance','2',125,1500,150,1800,5,'123 smmm',NULL,'dee','2019-07-24','2019-07-24','mco','77777','usa',50,'2019-07-17','mco',0,0,'mco','alamo','alamo','1222ddd',3600,3000,'','2019-07-24','','2019-07-12');
/*!40000 ALTER TABLE `car_booking_carbooking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cruisebooking_cruisehire`
--

DROP TABLE IF EXISTS `cruisebooking_cruisehire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cruisebooking_cruisehire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cruise_line` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `country` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cruise_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `departure_port` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email_contact` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dep_date` date DEFAULT NULL,
  `dep_time` date DEFAULT NULL,
  `telephone_contact` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `return_time` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `return_port` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `duration` double DEFAULT NULL,
  `num_rooms` double DEFAULT NULL,
  `state_room` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `meal_plan` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `num_guests` double DEFAULT NULL,
  `net_per_night` double DEFAULT NULL,
  `net_per_stay` double DEFAULT NULL,
  `gross_per_night` double DEFAULT NULL,
  `gross_per_stay` double DEFAULT NULL,
  `notes` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier_ref` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `booked_by` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cancellation_date` date DEFAULT NULL,
  `deposit_paid` double NOT NULL,
  `payment_due` double NOT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `balance_due_date` date DEFAULT NULL,
  `vat_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cruisebooking_cruise_booking_id_52cdf9b8_fk_bookings_` (`booking_id`),
  CONSTRAINT `cruisebooking_cruise_booking_id_52cdf9b8_fk_bookings_` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cruisebooking_cruisehire`
--

LOCK TABLES `cruisebooking_cruisehire` WRITE;
/*!40000 ALTER TABLE `cruisebooking_cruisehire` DISABLE KEYS */;
/*!40000 ALTER TABLE `cruisebooking_cruisehire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-07-13 13:55:20.080442','4','',3,'',12,1),(2,'2019-07-13 16:33:55.230187','1','abhi',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(3,'2019-07-21 14:55:11.246479','2','agent_test1',1,'[{\"added\": {}}]',4,1),(4,'2019-07-21 14:55:21.164968','2','agent_test1',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(5,'2019-07-21 15:03:49.454562','1','abhi',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(6,'2019-07-21 15:11:08.369875','2','agent_test1',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(7,'2019-07-21 15:11:36.348840','2','agent_test1',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(8,'2019-07-21 15:12:47.139803','2','agent_test1',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1),(9,'2019-09-07 11:21:34.046455','6','Tour',1,'[{\"added\": {}}]',3,1),(10,'2019-09-07 11:21:46.402990','1','Ticketing',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',3,1),(11,'2019-09-07 11:22:11.665245','7','Payment',1,'[{\"added\": {}}]',3,1),(12,'2019-09-07 11:22:33.696011','8','Documentation',1,'[{\"added\": {}}]',3,1),(13,'2019-09-07 11:23:03.881288','2','agent_test1',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(14,'2019-09-07 11:23:35.857527','2','agent_test1',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',4,1),(15,'2019-09-07 11:24:26.401169','1','abhi',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(16,'2019-09-07 11:24:43.348896','2','agent_test1',2,'[]',4,1),(17,'2019-09-10 14:47:16.004081','3','abhi_tour',1,'[{\"added\": {}}]',4,1),(18,'2019-09-10 14:48:02.297838','4','abhi_payment',1,'[{\"added\": {}}]',4,1),(19,'2019-09-10 14:48:11.667259','4','abhi_payment',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(20,'2019-09-10 14:48:21.203310','3','abhi_tour',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(21,'2019-09-10 14:49:26.071154','5','abhi_accounts',1,'[{\"added\": {}}]',4,1),(22,'2019-09-10 14:49:43.758870','5','abhi_accounts',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(23,'2019-09-10 14:50:04.151317','6','abhi_ticketing',1,'[{\"added\": {}}]',4,1),(24,'2019-09-10 14:50:12.402595','6','abhi_ticketing',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(25,'2019-09-10 14:50:28.698007','7','abhi_documentation',1,'[{\"added\": {}}]',4,1),(26,'2019-09-10 14:50:36.488049','7','abhi_documentation',2,'[{\"changed\": {\"fields\": [\"groups\"]}}]',4,1),(27,'2019-09-10 14:50:51.935361','5','abhi_accounts',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(28,'2019-09-10 14:51:00.251304','7','abhi_documentation',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(29,'2019-09-10 14:51:08.275469','4','abhi_payment',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(30,'2019-09-10 14:51:16.308893','6','abhi_ticketing',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(31,'2019-09-10 14:51:23.886862','3','abhi_tour',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(32,'2019-09-10 14:57:56.297134','3','abhi_tour',2,'[{\"changed\": {\"fields\": [\"user_permissions\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'bookings','booking'),(9,'bookings','carbookingproxy'),(10,'bookings','history'),(8,'bookings','notes'),(21,'bookings','paymentreceived'),(20,'bookings','paymentsmade'),(14,'car_booking','carbooking'),(5,'contenttypes','contenttype'),(16,'cruisebooking','cruisehire'),(13,'flightbooking','airline'),(11,'flightbooking','flight'),(12,'flightbooking','passenger'),(15,'hotel_booking','hotel'),(18,'package','package'),(19,'payments','payments'),(6,'sessions','session'),(17,'tourbooking','tourbooking');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-07-07 07:50:36.198272'),(2,'auth','0001_initial','2019-07-07 07:50:36.404095'),(3,'admin','0001_initial','2019-07-07 07:50:36.884218'),(4,'admin','0002_logentry_remove_auto_add','2019-07-07 07:50:36.982450'),(5,'admin','0003_logentry_add_action_flag_choices','2019-07-07 07:50:36.998237'),(6,'contenttypes','0002_remove_content_type_name','2019-07-07 07:50:37.085051'),(7,'auth','0002_alter_permission_name_max_length','2019-07-07 07:50:37.140420'),(8,'auth','0003_alter_user_email_max_length','2019-07-07 07:50:37.177895'),(9,'auth','0004_alter_user_username_opts','2019-07-07 07:50:37.191891'),(10,'auth','0005_alter_user_last_login_null','2019-07-07 07:50:37.243310'),(11,'auth','0006_require_contenttypes_0002','2019-07-07 07:50:37.248294'),(12,'auth','0007_alter_validators_add_error_messages','2019-07-07 07:50:37.269924'),(13,'auth','0008_alter_user_username_max_length','2019-07-07 07:50:37.347887'),(14,'auth','0009_alter_user_last_name_max_length','2019-07-07 07:50:37.409629'),(15,'auth','0010_alter_group_name_max_length','2019-07-07 07:50:37.440686'),(16,'auth','0011_update_proxy_permissions','2019-07-07 07:50:37.454375'),(17,'bookings','0001_initial','2019-07-07 07:50:37.501737'),(18,'bookings','0002_booking_added_date','2019-07-07 07:50:37.564748'),(19,'bookings','0003_carbookingproxy','2019-07-07 07:50:37.570280'),(20,'bookings','0004_auto_20190615_1118','2019-07-07 07:50:37.578414'),(21,'bookings','0005_booking_booking_agent','2019-07-07 07:50:37.625820'),(22,'bookings','0006_remove_booking_booking_agent','2019-07-07 07:50:37.741493'),(23,'bookings','0007_booking_booking_agent','2019-07-07 07:50:37.791605'),(24,'bookings','0008_auto_20190630_0716','2019-07-07 07:50:37.861430'),(25,'bookings','0009_history','2019-07-07 07:50:37.905996'),(26,'bookings','0010_history_operation','2019-07-07 07:50:37.977879'),(27,'bookings','0011_history_user','2019-07-07 07:50:38.018862'),(28,'bookings','0012_history_added_timestamp','2019-07-07 07:50:38.093518'),(29,'car_booking','0001_initial','2019-07-07 07:50:38.148859'),(30,'car_booking','0002_auto_20190615_1118','2019-07-07 07:50:38.691046'),(31,'car_booking','0003_auto_20190625_1528','2019-07-07 07:50:38.765387'),(32,'car_booking','0004_auto_20190703_0658','2019-07-07 07:50:38.965832'),(33,'car_booking','0005_carbooking_issue_date','2019-07-07 07:50:38.998297'),(34,'cruisebooking','0001_initial','2019-07-07 07:50:39.080127'),(35,'cruisebooking','0002_remove_cruisehire_issue_date','2019-07-07 07:50:39.121616'),(36,'cruisebooking','0003_cruisehire_booking_id','2019-07-07 07:50:39.178763'),(37,'cruisebooking','0004_auto_20190704_1105','2019-07-07 07:50:39.336679'),(38,'cruisebooking','0005_auto_20190704_1133','2019-07-07 07:50:39.527040'),(39,'flightbooking','0001_initial','2019-07-07 07:50:39.603631'),(40,'flightbooking','0002_remove_passenger_booking','2019-07-07 07:50:39.793176'),(41,'flightbooking','0003_auto_20190613_1242','2019-07-07 07:50:40.018196'),(42,'flightbooking','0004_auto_20190614_1218','2019-07-07 07:50:40.183900'),(43,'flightbooking','0005_auto_20190614_1727','2019-07-07 07:50:40.198085'),(44,'flightbooking','0006_auto_20190614_1749','2019-07-07 07:50:40.212571'),(45,'flightbooking','0007_auto_20190615_0425','2019-07-07 07:50:40.852345'),(46,'flightbooking','0008_auto_20190615_0432','2019-07-07 07:50:41.457718'),(47,'flightbooking','0009_auto_20190615_0452','2019-07-07 07:50:41.600911'),(48,'flightbooking','0010_auto_20190615_0454','2019-07-07 07:50:41.671479'),(49,'flightbooking','0011_auto_20190615_1029','2019-07-07 07:50:41.763864'),(50,'flightbooking','0012_auto_20190625_1528','2019-07-07 07:50:41.844389'),(51,'flightbooking','0013_auto_20190625_1546','2019-07-07 07:50:42.191880'),(52,'flightbooking','0014_flight_added_date','2019-07-07 07:50:42.303833'),(53,'flightbooking','0015_auto_20190627_0939','2019-07-07 07:50:42.314674'),(54,'flightbooking','0016_auto_20190628_0856','2019-07-07 07:50:42.418718'),(55,'flightbooking','0017_auto_20190628_1021','2019-07-07 07:50:42.550706'),(56,'flightbooking','0018_passenger_middle_name','2019-07-07 07:50:42.583043'),(57,'flightbooking','0019_auto_20190629_0734','2019-07-07 07:50:42.674418'),(58,'hotel_booking','0001_initial','2019-07-07 07:50:42.759492'),(59,'hotel_booking','0002_hotel_hotel_name','2019-07-07 07:50:42.849391'),(60,'sessions','0001_initial','2019-07-07 07:50:42.872081'),(63,'tourbooking','0001_initial','2019-07-08 15:35:40.525885'),(64,'package','0001_initial','2019-07-08 18:23:15.231406'),(65,'package','0002_package_created_date','2019-07-13 07:50:54.504763'),(66,'payments','0001_initial','2019-07-13 08:38:59.304685'),(67,'payments','0002_payments_added_date','2019-07-13 10:45:21.815884'),(68,'payments','0003_auto_20190713_1045','2019-07-13 10:45:21.897514'),(69,'payments','0004_auto_20190713_1051','2019-07-13 10:51:30.521523'),(70,'car_booking','0006_remove_carbooking_issue_date','2019-07-16 17:33:11.524954'),(71,'bookings','0013_paymentreceived_paymentsmade','2019-07-20 11:55:07.909329'),(72,'bookings','0014_auto_20190720_2214','2019-07-20 16:44:57.248883'),(73,'bookings','0015_auto_20190720_2215','2019-07-20 16:48:07.428266'),(74,'package','0003_auto_20190721_1456','2019-07-21 09:26:25.083066'),(75,'package','0004_package_admin_charges','2019-07-21 09:39:07.321249'),(76,'bookings','0016_booking_status','2019-07-21 15:02:26.922552');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3k1djzbgc1qfjbm1869picu8kuzfnyhe','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-07-27 16:34:06.811801'),('7wdqvqw7mba9po21w9rhhjp6kwdxuycz','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-07-28 07:12:04.752826'),('9f44sixconjj4a3ywcejsbv3idkc1n24','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-08-22 13:04:10.037959'),('hgvi2z2zebi5zgek1ftm3908v06ugi7f','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-08-07 17:58:25.499234'),('l8sp9outwcnwnpyqnzmv5b4ds1dwz1vd','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-08-05 14:45:31.570820'),('m85g5cr74i0anz6k2hkls1deduq1adbd','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-07-27 16:34:02.026934'),('pcy40v80b564pomgme54kl7v1q343h0j','ZWJiNjAyZDA3NjFmOWY5YjM2YjZlZWNkMWU3M2Q2YWU3NWM5ZjAzNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5Y2M2MzAzMGU1NTE1MDdmNGRiODJhMmVjN2UwMDdkZTg2YWM3OGUwIn0=','2019-09-24 16:40:52.074297'),('ym9s90nk2oq9aavnvowu77ebzdxx2f0s','Yjg5NjQ0MDkwYTlkNjcyZTI3N2I5ZDM1YTU4ZGM3ZTJiODdkYWYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNGI2ZjFmNjBjY2M0ZDUwZmZjZjcwNGYyMDRmMjdhOWZkMzkwNTc4In0=','2019-08-04 05:31:23.768482');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightbooking_airline`
--

DROP TABLE IF EXISTS `flightbooking_airline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flightbooking_airline` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `airline_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `airline_number` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dep_airport` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dep_date` date DEFAULT NULL,
  `arr_airport` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `arr_date` date DEFAULT NULL,
  `airline_class` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `flight_id` int(11) NOT NULL,
  `arr_time` time(6) DEFAULT NULL,
  `dep_time` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `flightbooking_airlin_flight_id_588e2f23_fk_flightboo` (`flight_id`),
  CONSTRAINT `flightbooking_airlin_flight_id_588e2f23_fk_flightboo` FOREIGN KEY (`flight_id`) REFERENCES `flightbooking_flight` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightbooking_airline`
--

LOCK TABLES `flightbooking_airline` WRITE;
/*!40000 ALTER TABLE `flightbooking_airline` DISABLE KEYS */;
INSERT INTO `flightbooking_airline` VALUES (1,'abhi','12323','DNN','2018-05-01','DNN','2018-05-23','Economy',1,'14:13:00.000000','03:21:00.000000'),(2,'asdsa','23123','312312','2018-05-26','312312','2018-05-25','Economy',2,'14:13:00.000000','03:21:00.000000'),(3,'asdsa','23123','312312','2018-05-08','312312','2018-06-05','Economy',3,'14:13:00.000000','03:21:00.000000'),(4,'ab','122','dd','2019-07-19','dd','2019-07-13','ff',4,'23:44:00.000000','23:34:00.000000'),(5,'gfgdg','3553','ggsg','2019-07-19','ggsg','2019-07-19','sgd',4,NULL,NULL),(12,'asdsa','23123','312312','2018-05-16','1332','2018-05-07','321312',10,NULL,NULL),(13,'asdsa','23123','312312','2018-05-26','312312','2018-05-25','321312',11,'14:13:00.000000','03:21:00.000000');
/*!40000 ALTER TABLE `flightbooking_airline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightbooking_flight`
--

DROP TABLE IF EXISTS `flightbooking_flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flightbooking_flight` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) NOT NULL,
  `adult_net` double NOT NULL,
  `adult_tax` double NOT NULL,
  `adult_total` double NOT NULL,
  `child_net` double NOT NULL,
  `child_tax` double NOT NULL,
  `child_total` double NOT NULL,
  `gross` double NOT NULL,
  `infant_net` double NOT NULL,
  `infant_tax` double NOT NULL,
  `infant_total` double NOT NULL,
  `net` double NOT NULL,
  `youth_net` double NOT NULL,
  `youth_tax` double NOT NULL,
  `youth_total` double NOT NULL,
  `adult_gross` double NOT NULL,
  `adult_gross_tax` double NOT NULL,
  `adult_gross_total` double NOT NULL,
  `child_gross` double NOT NULL,
  `child_gross_tax` double NOT NULL,
  `child_gross_total` double NOT NULL,
  `infant_gross` double NOT NULL,
  `infant_gross_tax` double NOT NULL,
  `infant_gross_total` double NOT NULL,
  `youth_gross` double NOT NULL,
  `youth_gross_tax` double NOT NULL,
  `youth_gross_total` double NOT NULL,
  `baggage_allowance` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `e_ticket` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_company` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `added_date` datetime(6) NOT NULL,
  `airline_ref` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pnr` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `flightbooking_flight_booking_id_528315a8_fk_bookings_booking_id` (`booking_id`),
  CONSTRAINT `flightbooking_flight_booking_id_528315a8_fk_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightbooking_flight`
--

LOCK TABLES `flightbooking_flight` WRITE;
/*!40000 ALTER TABLE `flightbooking_flight` DISABLE KEYS */;
INSERT INTO `flightbooking_flight` VALUES (1,1,12,12,24,0,0,0,24,0,0,0,24,0,0,0,12,12,24,0,0,0,0,0,0,0,0,0,'','',NULL,'','WorldSpan','LiveBooking','2019-07-07 08:45:04.170004',NULL,''),(2,2,12,12,24,0,0,0,24,0,0,0,24,0,0,0,12,12,24,0,0,0,0,0,0,0,0,0,'','',NULL,'','WorldSpan','LiveBooking','2019-07-13 08:08:22.324787',NULL,''),(3,3,12,12,48,0,0,0,48,0,0,0,48,0,0,0,12,12,48,0,0,0,0,0,0,0,0,0,'','',NULL,'','WorldSpan','LiveBooking','2019-07-13 12:58:42.608127',NULL,''),(4,4,22,124114,124136,0,0,0,30615,232,0,0,158671,34535,0,34535,3555,23525,27080,0,0,0,55235,0,0,3535,0,3535,'hdhdhf','afsfasf','2019-07-26','gsdgdgs','WorldSpan','LiveBooking','2019-07-13 16:43:39.631346',NULL,'fsdfs'),(10,4,1,1,2,0,0,0,2,0,0,0,2,0,0,0,1,1,2,0,0,0,0,0,0,0,0,0,'','',NULL,'','WorldSpan','LiveBooking','2019-07-13 16:57:19.043399',NULL,''),(11,5,12,12,0,0,0,0,0,0,0,0,0,0,0,0,12,12,0,0,0,0,0,0,0,0,0,0,'','',NULL,'','WorldSpan','LiveBooking','2019-07-21 15:24:35.204219',NULL,'');
/*!40000 ALTER TABLE `flightbooking_flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flightbooking_passenger`
--

DROP TABLE IF EXISTS `flightbooking_passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flightbooking_passenger` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flight_id` int(11) NOT NULL,
  `age_group` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `first_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gender` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nationality` varchar(100) COLLATE utf8mb4_general_ci,
  `title` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `middle_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `flightbooking_passen_flight_id_823312cb_fk_flightboo` (`flight_id`),
  CONSTRAINT `flightbooking_passen_flight_id_823312cb_fk_flightboo` FOREIGN KEY (`flight_id`) REFERENCES `flightbooking_flight` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flightbooking_passenger`
--

LOCK TABLES `flightbooking_passenger` WRITE;
/*!40000 ALTER TABLE `flightbooking_passenger` DISABLE KEYS */;
INSERT INTO `flightbooking_passenger` VALUES (1,1,'Adult','2018-07-24','Abhi ','M','Sharma','India','Mr','Test'),(2,2,'Adult','2019-07-11','abhi','M','','','Mr',''),(3,3,'Adult','2018-06-27','Abhi','M','test','Indian','Mr','Sharma'),(5,4,'Adult','2019-07-24','sdfsfsaf','M','dgsg','gdgdsg','Miss','sggdsg'),(6,10,'Adult','2018-07-25','abhi','M','Tripathi','India','Mr','sadas'),(7,11,'Infant','2016-07-04','abhi','M','','India','Mr','');
/*!40000 ALTER TABLE `flightbooking_passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel_booking_hotel`
--

DROP TABLE IF EXISTS `hotel_booking_hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hotel_booking_hotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `check_in` date DEFAULT NULL,
  `check_out` date DEFAULT NULL,
  `room_cat` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `room_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `board_basis` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `no_of_nights` double DEFAULT NULL,
  `country` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `star_cat` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `hotel_add` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `contact` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `no_rooms` double DEFAULT NULL,
  `net_per_night` double DEFAULT NULL,
  `net_per_stay` double DEFAULT NULL,
  `gross_per_night` double DEFAULT NULL,
  `gross_per_stay` double DEFAULT NULL,
  `total_net` double DEFAULT NULL,
  `total_gross` double DEFAULT NULL,
  `special_offer` double DEFAULT NULL,
  `lead_guest` double DEFAULT NULL,
  `supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier_ref` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `booked_by` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cancellation_date` date DEFAULT NULL,
  `deposit_paid` double NOT NULL,
  `payment_due` double NOT NULL,
  `balance_due_date` date DEFAULT NULL,
  `vat_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  `hotel_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hotel_booking_hotel_booking_id_eda4a979_fk_bookings_booking_id` (`booking_id`),
  CONSTRAINT `hotel_booking_hotel_booking_id_eda4a979_fk_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel_booking_hotel`
--

LOCK TABLES `hotel_booking_hotel` WRITE;
/*!40000 ALTER TABLE `hotel_booking_hotel` DISABLE KEYS */;
INSERT INTO `hotel_booking_hotel` VALUES (1,'2019-07-17','2019-07-15','ansdkjasn','asn,dmaks','Half Board',22,'India','Gurgaon','3 Star selected','asdjnkas','','',12,12,264,12,264,3168,3168,0,0,'','',NULL,'',NULL,0,0,NULL,'','',1,'Nand'),(2,'2019-07-10','2019-07-15','ansdkjasn','asn,dmaks','Room Only',5,'Test','Allahabad','3 Star selected selected','39/17 (9-A), Muir Road, Prayagraj','312312312','abhisharma129@gmail.com',12,12,60,12,60,720,720,0,0,'','',NULL,'',NULL,0,0,'2019-07-24','','',2,'Nand'),(3,'2019-07-17','2019-07-23','hdhd','dfh','Bed & breakfast',6,'ddsgsdg','sggsd','4 Star','hrhdh','646363','ddhdhdh',45,3535325,21211950,636363,3818178,954537750,171818010,0,0,'dfhdf','dfhdhd','2019-07-26','bdfgdsgd','2019-07-24',34,34,'2019-07-17','3634','sggd',4,'dgsg'),(4,'2019-07-18','2019-07-23','fdhhdh','dhfhh','Half Board',5,'bddh','dshs','4 Star','dhdhd','ddgdh','sdhdh@jgj.hdh',44,44,220,55,275,9680,12100,0,0,'dsdssg','cnn','2019-07-23','hhsdh','2019-07-19',44,44,'2019-07-16','66','sdgdshs',4,'dhhdh'),(5,'2019-08-21','2019-08-19','kmlkn','standard','All Exclusive',4,'usa','florida','3 Star selected selected','123,smart street','70000211100','dee@',2,50,200,70,280,400,560,0,0,'ttttttt','ab231222',NULL,'deepak',NULL,50,0,NULL,'','taps',5,'avanti resort');
/*!40000 ALTER TABLE `hotel_booking_hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `package_package`
--

DROP TABLE IF EXISTS `package_package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `package_package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flight_net` double NOT NULL,
  `flight_net_other` double NOT NULL,
  `flight_gross` double NOT NULL,
  `hotel_net` double NOT NULL,
  `hotel_net_other` double NOT NULL,
  `hotel_gross` double NOT NULL,
  `car_net` double NOT NULL,
  `car_net_other` double NOT NULL,
  `car_gross` double NOT NULL,
  `cruise_net` double NOT NULL,
  `cruise_net_other` double NOT NULL,
  `cruise_gross` double NOT NULL,
  `tour_net` double NOT NULL,
  `tour_net_other` double NOT NULL,
  `tour_gross` double NOT NULL,
  `total` double NOT NULL,
  `booking_id` int(11) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `atol` double NOT NULL,
  `commission` double NOT NULL,
  `insurance` double NOT NULL,
  `sfc` double NOT NULL,
  `admin_charges` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `package_package_booking_id_7c57f7b8_fk_bookings_booking_id` (`booking_id`),
  CONSTRAINT `package_package_booking_id_7c57f7b8_fk_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package_package`
--

LOCK TABLES `package_package` WRITE;
/*!40000 ALTER TABLE `package_package` DISABLE KEYS */;
INSERT INTO `package_package` VALUES (2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,'2019-07-13 07:51:36.864372',0,0,0,0,0),(3,24,100,24,720,100,720,0,0,0,0,0,0,0,0,0,1688,2,'2019-07-13 08:08:22.330911',0,0,0,0,0),(4,48,0,48,0,0,0,0,0,0,0,0,0,0,0,0,96,3,'2019-07-13 12:58:42.616372',0,0,0,0,0),(5,158673,0,30617,954547430,0,171830110,364636,0,666236,0,0,0,0,0,0,1127597702,4,'2019-07-13 16:43:39.636020',12,19,12,0,10),(6,0,15,0,400,350,560,1500,0,1800,0,50,0,0,0,0,4675,5,'2019-07-21 15:24:35.220763',0,0,0,0,10);
/*!40000 ALTER TABLE `package_package` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments_payments`
--

DROP TABLE IF EXISTS `payments_payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments_payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `post_code` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `contact` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `name_on_card` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `expiry_month` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `security_code` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `amount` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `surcharge` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  `added_date` datetime(6) NOT NULL,
  `expiry_year` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `amount_due` double NOT NULL,
  `amount_paid` double NOT NULL,
  `due_date` date DEFAULT NULL,
  `first_four` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `fourth_four` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `second_four` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `third_four` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `payments_payments_booking_id_df5d8d54_fk_bookings_booking_id` (`booking_id`),
  CONSTRAINT `payments_payments_booking_id_df5d8d54_fk_bookings_booking_id` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments_payments`
--

LOCK TABLES `payments_payments` WRITE;
/*!40000 ALTER TABLE `payments_payments` DISABLE KEYS */;
INSERT INTO `payments_payments` VALUES (1,'sadasdas','211001','abhisharma129@gmail.com','871726262','Bank Payment','asdasdas','05','124','12','12',2,'2019-07-13 11:20:51.988546','2026',0,0,NULL,'1211','3123','1212','1312'),(2,'39/17 (9-A), Muir Road, Prayagraj','211001','asdklaslkdmas','','Credit Card','Onkar ','01','123','1321','312',2,'2019-07-13 11:22:53.332448','2018',3123,13123,NULL,'1231','1231','3123','3123'),(3,'','','','','Debit Card',NULL,'04',NULL,'450','',5,'2019-07-22 15:06:41.575746','2035',5000,450,'2019-09-20','5522','4234','6050','0034');
/*!40000 ALTER TABLE `payments_payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tourbooking_tourbooking`
--

DROP TABLE IF EXISTS `tourbooking_tourbooking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tourbooking_tourbooking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tour_type` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `country` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `attraction_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `city` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `duration` double DEFAULT NULL,
  `no_of_tickets` double DEFAULT NULL,
  `net_per_ticket` double NOT NULL,
  `total_net` double NOT NULL,
  `gross_per_ticket` double NOT NULL,
  `total_gross` double NOT NULL,
  `notes` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `lead_guest` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `supplier_ref` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `booked_by` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cancellation_date` date DEFAULT NULL,
  `deposit_paid` double NOT NULL,
  `payment_due` double NOT NULL,
  `payment_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `balance_due_date` date DEFAULT NULL,
  `vat_id` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tourbooking_tourbook_booking_id_12603bd8_fk_bookings_` (`booking_id`),
  CONSTRAINT `tourbooking_tourbook_booking_id_12603bd8_fk_bookings_` FOREIGN KEY (`booking_id`) REFERENCES `bookings_booking` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tourbooking_tourbooking`
--

LOCK TABLES `tourbooking_tourbooking` WRITE;
/*!40000 ALTER TABLE `tourbooking_tourbooking` DISABLE KEYS */;
INSERT INTO `tourbooking_tourbooking` VALUES (1,'One Way Transfers','','asmd ,as','',NULL,1,0,0,0,0,0,'','','','',NULL,'',NULL,0,0,'',NULL,NULL,1),(2,'One Way Transfers','','asmd ,as','',NULL,1,100,100,100,100,100,'','','','',NULL,'',NULL,0,0,'',NULL,NULL,1),(3,'One Way Transfers','','asmd ,as','',NULL,1,0,0,0,0,0,'','','','',NULL,'',NULL,0,0,'',NULL,NULL,1);
/*!40000 ALTER TABLE `tourbooking_tourbooking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-10 22:40:56
