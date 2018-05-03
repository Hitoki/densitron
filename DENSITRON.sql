-- MySQL dump 10.13  Distrib 5.6.27, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: densitron
-- ------------------------------------------------------
-- Server version	5.6.27-0ubuntu0.15.04.1

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
-- Table structure for table `address_address`
--

DROP TABLE IF EXISTS `address_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `line_1` varchar(128) NOT NULL,
  `line_2` varchar(128) NOT NULL,
  `phone` varchar(36) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address_address`
--

LOCK TABLES `address_address` WRITE;
/*!40000 ALTER TABLE `address_address` DISABLE KEYS */;
INSERT INTO `address_address` VALUES (1,'Test Address','Test Address, created from initial date','Head Office <br> (UK & Europe)','72 Cannon St','London EC4N 6 AE','+44 (0)20 7648 4200'),(2,'Test Address 2','Test Address 2, created from initial date','Head Office(US)','2330 Ponoma Rincon Road','Corona, CA 92880','+1 951-284-7600');
/*!40000 ALTER TABLE `address_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
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
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add content type',1,'add_contenttype'),(2,'Can change content type',1,'change_contenttype'),(3,'Can delete content type',1,'delete_contenttype'),(4,'Can add log entry',2,'add_logentry'),(5,'Can change log entry',2,'change_logentry'),(6,'Can delete log entry',2,'delete_logentry'),(7,'Can add permission',5,'add_permission'),(8,'Can change permission',5,'change_permission'),(9,'Can delete permission',5,'delete_permission'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add user',3,'add_user'),(14,'Can change user',3,'change_user'),(15,'Can delete user',3,'delete_user'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add page',31,'add_page'),(20,'Can change page',31,'change_page'),(21,'Can delete page',31,'delete_page'),(22,'Can add page header block',16,'add_pageheaderblock'),(23,'Can change page header block',16,'change_pageheaderblock'),(24,'Can delete page header block',16,'delete_pageheaderblock'),(25,'Can add page head soc link',12,'add_pageheadsoclink'),(26,'Can change page head soc link',12,'change_pageheadsoclink'),(27,'Can delete page head soc link',12,'delete_pageheadsoclink'),(28,'Can add page head drop menu',29,'add_pageheaddropmenu'),(29,'Can change page head drop menu',29,'change_pageheaddropmenu'),(30,'Can delete page head drop menu',29,'delete_pageheaddropmenu'),(31,'Can add page head drop menu element',7,'add_pageheaddropmenuelement'),(32,'Can change page head drop menu element',7,'change_pageheaddropmenuelement'),(33,'Can delete page head drop menu element',7,'delete_pageheaddropmenuelement'),(34,'Can add page help box block',8,'add_pagehelpboxblock'),(35,'Can change page help box block',8,'change_pagehelpboxblock'),(36,'Can delete page help box block',8,'delete_pagehelpboxblock'),(37,'Can add page button',26,'add_pagebutton'),(38,'Can change page button',26,'change_pagebutton'),(39,'Can delete page button',26,'delete_pagebutton'),(40,'Can add page main block',11,'add_pagemainblock'),(41,'Can change page main block',11,'change_pagemainblock'),(42,'Can delete page main block',11,'delete_pagemainblock'),(43,'Can add page footer block',25,'add_pagefooterblock'),(44,'Can change page footer block',25,'change_pagefooterblock'),(45,'Can delete page footer block',25,'delete_pagefooterblock'),(46,'Can add page what you need block',17,'add_pagewhatyouneedblock'),(47,'Can change page what you need block',17,'change_pagewhatyouneedblock'),(48,'Can delete page what you need block',17,'delete_pagewhatyouneedblock'),(49,'Can add page world pay screen block',15,'add_pageworldpayscreenblock'),(50,'Can change page world pay screen block',15,'change_pageworldpayscreenblock'),(51,'Can delete page world pay screen block',15,'delete_pageworldpayscreenblock'),(52,'Can add slide element',20,'add_slideelement'),(53,'Can change slide element',20,'change_slideelement'),(54,'Can delete slide element',20,'delete_slideelement'),(55,'Can add posts gallery block',28,'add_postsgalleryblock'),(56,'Can change posts gallery block',28,'change_postsgalleryblock'),(57,'Can delete posts gallery block',28,'delete_postsgalleryblock'),(58,'Can add bespoke screen block',19,'add_bespokescreenblock'),(59,'Can change bespoke screen block',19,'change_bespokescreenblock'),(60,'Can delete bespoke screen block',19,'delete_bespokescreenblock'),(61,'Can add latest block',9,'add_latestblock'),(62,'Can change latest block',9,'change_latestblock'),(63,'Can delete latest block',9,'delete_latestblock'),(64,'Can add video block',23,'add_videoblock'),(65,'Can change video block',23,'change_videoblock'),(66,'Can delete video block',23,'delete_videoblock'),(67,'Can add text photo block',27,'add_textphotoblock'),(68,'Can change text photo block',27,'change_textphotoblock'),(69,'Can delete text photo block',27,'delete_textphotoblock'),(70,'Can add text block',24,'add_textblock'),(71,'Can change text block',24,'change_textblock'),(72,'Can delete text block',24,'delete_textblock'),(73,'Can add text element',33,'add_textelement'),(74,'Can change text element',33,'change_textelement'),(75,'Can delete text element',33,'delete_textelement'),(76,'Can add expandable section block',32,'add_expandablesectionblock'),(77,'Can change expandable section block',32,'change_expandablesectionblock'),(78,'Can delete expandable section block',32,'delete_expandablesectionblock'),(79,'Can add expandable section',22,'add_expandablesection'),(80,'Can change expandable section',22,'change_expandablesection'),(81,'Can delete expandable section',22,'delete_expandablesection'),(82,'Can add bullet',13,'add_bullet'),(83,'Can change bullet',13,'change_bullet'),(84,'Can delete bullet',13,'delete_bullet'),(85,'Can add wizard product found block',21,'add_wizardproductfoundblock'),(86,'Can change wizard product found block',21,'change_wizardproductfoundblock'),(87,'Can delete wizard product found block',21,'delete_wizardproductfoundblock'),(88,'Can add product detail block',35,'add_productdetailblock'),(89,'Can change product detail block',35,'change_productdetailblock'),(90,'Can delete product detail block',35,'delete_productdetailblock'),(91,'Can add page category block',18,'add_pagecategoryblock'),(92,'Can change page category block',18,'change_pagecategoryblock'),(93,'Can delete page category block',18,'delete_pagecategoryblock'),(94,'Can add page sub category block',10,'add_pagesubcategoryblock'),(95,'Can change page sub category block',10,'change_pagesubcategoryblock'),(96,'Can delete page sub category block',10,'delete_pagesubcategoryblock'),(97,'Can add bespoke orders block',14,'add_bespokeordersblock'),(98,'Can change bespoke orders block',14,'change_bespokeordersblock'),(99,'Can delete bespoke orders block',14,'delete_bespokeordersblock'),(100,'Can add our people block',30,'add_ourpeopleblock'),(101,'Can change our people block',30,'change_ourpeopleblock'),(102,'Can delete our people block',30,'delete_ourpeopleblock'),(103,'Can add video object',34,'add_videoobject'),(104,'Can change video object',34,'change_videoobject'),(105,'Can delete video object',34,'delete_videoobject'),(106,'Can add product',46,'add_product'),(107,'Can change product',46,'change_product'),(108,'Can delete product',46,'delete_product'),(109,'Can add product image',49,'add_productimage'),(110,'Can change product image',49,'change_productimage'),(111,'Can delete product image',49,'delete_productimage'),(112,'Can add tft product',38,'add_tftproduct'),(113,'Can change tft product',38,'change_tftproduct'),(114,'Can delete tft product',38,'delete_tftproduct'),(115,'Can add touch panel product',42,'add_touchpanelproduct'),(116,'Can change touch panel product',42,'change_touchpanelproduct'),(117,'Can delete touch panel product',42,'delete_touchpanelproduct'),(118,'Can add oled product',36,'add_oledproduct'),(119,'Can change oled product',36,'change_oledproduct'),(120,'Can delete oled product',36,'delete_oledproduct'),(121,'Can add monochrome product',44,'add_monochromeproduct'),(122,'Can change monochrome product',44,'change_monochromeproduct'),(123,'Can delete monochrome product',44,'delete_monochromeproduct'),(124,'Can add low power product',37,'add_lowpowerproduct'),(125,'Can change low power product',37,'change_lowpowerproduct'),(126,'Can delete low power product',37,'delete_lowpowerproduct'),(127,'Can add technology',40,'add_technology'),(128,'Can change technology',40,'change_technology'),(129,'Can delete technology',40,'delete_technology'),(130,'Can add category',43,'add_category'),(131,'Can change category',43,'change_category'),(132,'Can delete category',43,'delete_category'),(133,'Can add tft if',51,'add_tftif'),(134,'Can change tft if',51,'change_tftif'),(135,'Can delete tft if',51,'delete_tftif'),(136,'Can add structure',48,'add_structure'),(137,'Can change structure',48,'change_structure'),(138,'Can delete structure',48,'delete_structure'),(139,'Can add controller',39,'add_controller'),(140,'Can change controller',39,'change_controller'),(141,'Can delete controller',39,'delete_controller'),(142,'Can add interface',50,'add_interface'),(143,'Can change interface',50,'change_interface'),(144,'Can delete interface',50,'delete_interface'),(145,'Can add os',45,'add_os'),(146,'Can change os',45,'change_os'),(147,'Can delete os',45,'delete_os'),(148,'Can add touch',47,'add_touch'),(149,'Can change touch',47,'change_touch'),(150,'Can delete touch',47,'delete_touch'),(151,'Can add feature',41,'add_feature'),(152,'Can change feature',41,'change_feature'),(153,'Can delete feature',41,'delete_feature'),(154,'Can add address',52,'add_address'),(155,'Can change address',52,'change_address'),(156,'Can delete address',52,'delete_address'),(157,'Can add people',55,'add_people'),(158,'Can change people',55,'change_people'),(159,'Can delete people',55,'delete_people'),(160,'Can add team',54,'add_team'),(161,'Can change team',54,'change_team'),(162,'Can delete team',54,'delete_team'),(163,'Can add job',53,'add_job'),(164,'Can change job',53,'change_job'),(165,'Can delete job',53,'delete_job');
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
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$FtXrrsBI9jhq$GM4tJexMKYZqTbRWSTqaCS1966my01Vvhdj3pURlMMU=','2016-01-28 09:37:55.707864',1,'anvil8','','','anvil8@anvil8.com',1,1,'2016-01-28 09:22:38.266380');
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
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
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
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_job`
--

DROP TABLE IF EXISTS `company_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_job`
--

LOCK TABLES `company_job` WRITE;
/*!40000 ALTER TABLE `company_job` DISABLE KEYS */;
INSERT INTO `company_job` VALUES (1,'Test Job Title','Test Job Description');
/*!40000 ALTER TABLE `company_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_people`
--

DROP TABLE IF EXISTS `company_people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `phone` varchar(32) NOT NULL,
  `email` varchar(254) NOT NULL,
  `description` longtext NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `job_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `company_people_job_id_785ac4c0_fk_company_job_id` (`job_id`),
  KEY `company_people_f6a7ca40` (`team_id`),
  CONSTRAINT `company_people_job_id_785ac4c0_fk_company_job_id` FOREIGN KEY (`job_id`) REFERENCES `company_job` (`id`),
  CONSTRAINT `company_people_team_id_952465aa_fk_company_team_id` FOREIGN KEY (`team_id`) REFERENCES `company_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_people`
--

LOCK TABLES `company_people` WRITE;
/*!40000 ALTER TABLE `company_people` DISABLE KEYS */;
INSERT INTO `company_people` VALUES (1,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(2,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(3,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(4,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(5,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(6,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(7,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(8,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,1),(9,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(10,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(11,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(12,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(13,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(14,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(15,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2),(16,'Jo','Blogs','0181 811 8181','jo.blocgs@densitron.com','People Test Description','',1,2);
/*!40000 ALTER TABLE `company_people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_team`
--

DROP TABLE IF EXISTS `company_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_team`
--

LOCK TABLES `company_team` WRITE;
/*!40000 ALTER TABLE `company_team` DISABLE KEYS */;
INSERT INTO `company_team` VALUES (1,'Board Members','Test Team Description'),(2,'Management Team','Test Team Description');
/*!40000 ALTER TABLE `company_team` ENABLE KEYS */;
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
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-01-28 09:38:28.707366','1','Nashe',1,'Added.',34,1),(2,'2016-01-28 09:39:18.231713','2','Vimeo',1,'Added.',34,1),(3,'2016-01-28 09:40:04.851833','3','Youtube',1,'Added.',34,1),(4,'2016-01-28 09:40:10.365367','1','Test Latest Block',2,'Changed video_main, video_second and video_third.',9,1),(5,'2016-01-28 10:12:37.923568','3','Youtube',2,'Changed embed_video.',34,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (52,'address','address'),(2,'admin','logentry'),(4,'auth','group'),(5,'auth','permission'),(3,'auth','user'),(53,'company','job'),(55,'company','people'),(54,'company','team'),(1,'contenttypes','contenttype'),(14,'elastic_pages','bespokeordersblock'),(19,'elastic_pages','bespokescreenblock'),(13,'elastic_pages','bullet'),(22,'elastic_pages','expandablesection'),(32,'elastic_pages','expandablesectionblock'),(9,'elastic_pages','latestblock'),(30,'elastic_pages','ourpeopleblock'),(31,'elastic_pages','page'),(26,'elastic_pages','pagebutton'),(18,'elastic_pages','pagecategoryblock'),(25,'elastic_pages','pagefooterblock'),(29,'elastic_pages','pageheaddropmenu'),(7,'elastic_pages','pageheaddropmenuelement'),(16,'elastic_pages','pageheaderblock'),(12,'elastic_pages','pageheadsoclink'),(8,'elastic_pages','pagehelpboxblock'),(11,'elastic_pages','pagemainblock'),(10,'elastic_pages','pagesubcategoryblock'),(17,'elastic_pages','pagewhatyouneedblock'),(15,'elastic_pages','pageworldpayscreenblock'),(28,'elastic_pages','postsgalleryblock'),(35,'elastic_pages','productdetailblock'),(20,'elastic_pages','slideelement'),(24,'elastic_pages','textblock'),(33,'elastic_pages','textelement'),(27,'elastic_pages','textphotoblock'),(23,'elastic_pages','videoblock'),(34,'elastic_pages','videoobject'),(21,'elastic_pages','wizardproductfoundblock'),(43,'products','category'),(39,'products','controller'),(41,'products','feature'),(50,'products','interface'),(37,'products','lowpowerproduct'),(44,'products','monochromeproduct'),(36,'products','oledproduct'),(45,'products','os'),(46,'products','product'),(49,'products','productimage'),(48,'products','structure'),(40,'products','technology'),(51,'products','tftif'),(38,'products','tftproduct'),(47,'products','touch'),(42,'products','touchpanelproduct'),(6,'sessions','session');
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
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'address','0001_initial','2016-01-28 09:20:35.129195'),(2,'contenttypes','0001_initial','2016-01-28 09:20:35.744898'),(3,'auth','0001_initial','2016-01-28 09:20:44.640230'),(4,'admin','0001_initial','2016-01-28 09:20:46.496961'),(5,'admin','0002_logentry_remove_auto_add','2016-01-28 09:20:46.689941'),(6,'contenttypes','0002_remove_content_type_name','2016-01-28 09:20:48.012970'),(7,'auth','0002_alter_permission_name_max_length','2016-01-28 09:20:49.024161'),(8,'auth','0003_alter_user_email_max_length','2016-01-28 09:20:49.868038'),(9,'auth','0004_alter_user_username_opts','2016-01-28 09:20:49.926639'),(10,'auth','0005_alter_user_last_login_null','2016-01-28 09:20:50.714020'),(11,'auth','0006_require_contenttypes_0002','2016-01-28 09:20:50.755378'),(12,'auth','0007_alter_validators_add_error_messages','2016-01-28 09:20:50.813297'),(13,'company','0001_initial','2016-01-28 09:20:55.582467'),(14,'company','0002_load_people','2016-01-28 09:20:55.890847'),(15,'company','0003_auto_20160127_1206','2016-01-28 09:20:56.604330'),(16,'elastic_pages','0001_initial','2016-01-28 09:21:27.282532'),(17,'elastic_pages','0002_whatyouneedblock','2016-01-28 09:21:27.751068'),(18,'elastic_pages','0003_auto_20160108_0913','2016-01-28 09:22:22.131230'),(19,'elastic_pages','0004_auto_20160115_1519','2016-01-28 09:22:38.211411'),(20,'elastic_pages','0005_load_elastic_pages','2016-01-28 09:22:41.301660'),(21,'elastic_pages','0006_auto_20160118_0752','2016-01-28 09:22:45.622260'),(22,'elastic_pages','0007_auto_20160119_1414','2016-01-28 09:22:53.223160'),(23,'elastic_pages','0008_load_new_pages','2016-01-28 09:22:53.599297'),(24,'elastic_pages','0009_auto_20160127_0913','2016-01-28 09:23:01.025314'),(25,'elastic_pages','0010_load_new_pages2','2016-01-28 09:23:01.218374'),(26,'elastic_pages','0011_auto_20160127_1206','2016-01-28 09:23:01.503882'),(27,'elastic_pages','0012_auto_20160127_1235','2016-01-28 09:23:09.726887'),(28,'elastic_pages','0013_auto_20160128_0920','2016-01-28 09:23:12.203849'),(29,'products','0001_initial','2016-01-28 09:23:17.422230'),(30,'products','0002_auto_20160107_1545','2016-01-28 09:23:45.310791'),(31,'products','0003_auto_20160113_1610','2016-01-28 09:23:48.454580'),(32,'products','0004_load_products','2016-01-28 09:23:50.065820'),(33,'sessions','0001_initial','2016-01-28 09:23:50.826006'),(34,'elastic_pages','0014_auto_20160128_1056','2016-01-28 10:56:40.290196');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('e6ao4kcwajwgxi7bezwrxbtphu3tx5pv','ZTQ2N2Q2Yzg2MTY1N2ZkOTA3MzU3NWJjY2UwMDlmZDZlYmU1Y2VmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNmYzYjQ0YTY3ZGVlYWY5NzMzZTRjNjc0ZDhhYjMwMWVhYTlhNGRlZiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-02-11 09:37:55.769702');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_bespokeordersblock`
--

DROP TABLE IF EXISTS `elastic_pages_bespokeordersblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_bespokeordersblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_bespokeordersblock`
--

LOCK TABLES `elastic_pages_bespokeordersblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_bespokeordersblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_bespokeordersblock` VALUES (1,'Test Bespoke Orders Block','Test Bespoke Orders Block, created from initial date');
/*!40000 ALTER TABLE `elastic_pages_bespokeordersblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_bespokescreenblock`
--

DROP TABLE IF EXISTS `elastic_pages_bespokescreenblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_bespokescreenblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title_top` varchar(64) NOT NULL,
  `title_bottom` varchar(64) NOT NULL,
  `background` varchar(100) NOT NULL,
  `button_id` int(11),
  PRIMARY KEY (`id`),
  KEY `elastic_pages_bespokescreenblock_2e479f87` (`button_id`),
  CONSTRAINT `elastic_pages__button_id_5d9e56dc_fk_elastic_pages_pagebutton_id` FOREIGN KEY (`button_id`) REFERENCES `elastic_pages_pagebutton` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_bespokescreenblock`
--

LOCK TABLES `elastic_pages_bespokescreenblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_bespokescreenblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_bespokescreenblock` VALUES (1,'Test Bespoke Screen Block','Test Bespoke Screen Block, created from initial date','Bespoke Screen','& Manufacturing','/static/test_images/bespoke-image.jpeg',NULL);
/*!40000 ALTER TABLE `elastic_pages_bespokescreenblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_bullet`
--

DROP TABLE IF EXISTS `elastic_pages_bullet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_bullet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `style` varchar(8) NOT NULL,
  `title` varchar(128) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_bullet`
--

LOCK TABLES `elastic_pages_bullet` WRITE;
/*!40000 ALTER TABLE `elastic_pages_bullet` DISABLE KEYS */;
INSERT INTO `elastic_pages_bullet` VALUES (1,'Test Bullet Block','Test Bullet Block, created from initial date','G-Ok','Bullet 0','Curabitor dolor eros, gravida et, hendrerit ac, cursus non, massa.'),(2,'Test Bullet Block','Test Bullet Block, created from initial date','G-Ok','Bullet 1','Curabitor dolor eros, gravida et, hendrerit ac, cursus non, massa.'),(3,'Test Bullet Block','Test Bullet Block, created from initial date','G-Ok','Bullet 2','Curabitor dolor eros, gravida et, hendrerit ac, cursus non, massa.'),(4,'Test Bullet Block','Test Bullet Block, created from initial date','G-Ok','Bullet 3','Curabitor dolor eros, gravida et, hendrerit ac, cursus non, massa.');
/*!40000 ALTER TABLE `elastic_pages_bullet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_expandablesection`
--

DROP TABLE IF EXISTS `elastic_pages_expandablesection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_expandablesection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `sub_title` varchar(128) NOT NULL,
  `sub_sub_title` varchar(128) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_expandablesection`
--

LOCK TABLES `elastic_pages_expandablesection` WRITE;
/*!40000 ALTER TABLE `elastic_pages_expandablesection` DISABLE KEYS */;
INSERT INTO `elastic_pages_expandablesection` VALUES (1,'Test Expandable Section Block','Test Expandable Section Block, created from initial date','Expandable Section','Sub Heading','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.'),(2,'Test Expandable Section Block','Test Expandable Section Block, created from initial date','Expandable Section','Sub Heading','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.'),(3,'Test Expandable Section Block','Test Expandable Section Block, created from initial date','Expandable Section','Sub Heading','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.'),(4,'Test Expandable Section Block','Test Expandable Section Block, created from initial date','Expandable Section','Sub Heading','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.'),(5,'Test Expandable Section Block','Test Expandable Section Block, created from initial date','Expandable Section','Sub Heading','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.');
/*!40000 ALTER TABLE `elastic_pages_expandablesection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_expandablesection_bullet`
--

DROP TABLE IF EXISTS `elastic_pages_expandablesection_bullet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_expandablesection_bullet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `expandablesection_id` int(11) NOT NULL,
  `bullet_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_expandablesecti_expandablesection_id_6b9fba38_uniq` (`expandablesection_id`,`bullet_id`),
  KEY `elastic_pages_expa_bullet_id_d30b8e92_fk_elastic_pages_bullet_id` (`bullet_id`),
  CONSTRAINT `be30505afd0a95afc0962fed35284872` FOREIGN KEY (`expandablesection_id`) REFERENCES `elastic_pages_expandablesection` (`id`),
  CONSTRAINT `elastic_pages_expa_bullet_id_d30b8e92_fk_elastic_pages_bullet_id` FOREIGN KEY (`bullet_id`) REFERENCES `elastic_pages_bullet` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_expandablesection_bullet`
--

LOCK TABLES `elastic_pages_expandablesection_bullet` WRITE;
/*!40000 ALTER TABLE `elastic_pages_expandablesection_bullet` DISABLE KEYS */;
INSERT INTO `elastic_pages_expandablesection_bullet` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,2,1),(6,2,2),(7,2,3),(8,2,4),(9,3,1),(10,3,2),(11,3,3),(12,3,4),(13,4,1),(14,4,2),(15,4,3),(16,4,4),(17,5,1),(18,5,2),(19,5,3),(20,5,4);
/*!40000 ALTER TABLE `elastic_pages_expandablesection_bullet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_expandablesectionblock`
--

DROP TABLE IF EXISTS `elastic_pages_expandablesectionblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_expandablesectionblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_expandablesectionblock`
--

LOCK TABLES `elastic_pages_expandablesectionblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_expandablesectionblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_expandablesectionblock` VALUES (1,'Test Expandable Section Block','Test Expandable Section Block, created from initial date','Expandable / Collapsable Sections');
/*!40000 ALTER TABLE `elastic_pages_expandablesectionblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_expandablesectionblock_section`
--

DROP TABLE IF EXISTS `elastic_pages_expandablesectionblock_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_expandablesectionblock_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `expandablesectionblock_id` int(11) NOT NULL,
  `expandablesection_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_expandable_expandablesectionblock_id_d1701598_uniq` (`expandablesectionblock_id`,`expandablesection_id`),
  KEY `D614395c1530dd2e9eb3ba7d32eb7609` (`expandablesection_id`),
  CONSTRAINT `D614395c1530dd2e9eb3ba7d32eb7609` FOREIGN KEY (`expandablesection_id`) REFERENCES `elastic_pages_expandablesection` (`id`),
  CONSTRAINT `de151253915febcfd281109400134fb9` FOREIGN KEY (`expandablesectionblock_id`) REFERENCES `elastic_pages_expandablesectionblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_expandablesectionblock_section`
--

LOCK TABLES `elastic_pages_expandablesectionblock_section` WRITE;
/*!40000 ALTER TABLE `elastic_pages_expandablesectionblock_section` DISABLE KEYS */;
INSERT INTO `elastic_pages_expandablesectionblock_section` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5);
/*!40000 ALTER TABLE `elastic_pages_expandablesectionblock_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_latestblock`
--

DROP TABLE IF EXISTS `elastic_pages_latestblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_latestblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `video_main_id` int(11),
  `video_second_id` int(11),
  `video_third_id` int(11),
  PRIMARY KEY (`id`),
  KEY `elastic_pages_latestblock_47eea5bc` (`video_main_id`),
  KEY `elastic_pages_latestblock_b41f967f` (`video_second_id`),
  KEY `elastic_pages_latestblock_5df5b0c0` (`video_third_id`),
  CONSTRAINT `elastic__video_third_id_eec4324d_fk_elastic_pages_videoobject_id` FOREIGN KEY (`video_third_id`) REFERENCES `elastic_pages_videoobject` (`id`),
  CONSTRAINT `elastic_p_video_main_id_ee5a9a65_fk_elastic_pages_videoobject_id` FOREIGN KEY (`video_main_id`) REFERENCES `elastic_pages_videoobject` (`id`),
  CONSTRAINT `elastic_video_second_id_74afa2c0_fk_elastic_pages_videoobject_id` FOREIGN KEY (`video_second_id`) REFERENCES `elastic_pages_videoobject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_latestblock`
--

LOCK TABLES `elastic_pages_latestblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_latestblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_latestblock` VALUES (1,'Test Latest Block','Test Latest Block, created from initial date',3,2,1);
/*!40000 ALTER TABLE `elastic_pages_latestblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_ourpeopleblock`
--

DROP TABLE IF EXISTS `elastic_pages_ourpeopleblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_ourpeopleblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `head_text` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_ourpeopleblock`
--

LOCK TABLES `elastic_pages_ourpeopleblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_ourpeopleblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_ourpeopleblock` VALUES (1,'Test Our People Block','Test Our People Block, created from initial date','Meet the Team');
/*!40000 ALTER TABLE `elastic_pages_ourpeopleblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_page`
--

DROP TABLE IF EXISTS `elastic_pages_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `page_type` varchar(32) NOT NULL,
  `title` varchar(64) NOT NULL,
  `footer_block_id` int(11),
  `header_block_id` int(11),
  `help_box_block_id` int(11),
  `main_block_id` int(11),
  `bespoke_screen_block_id` int(11),
  `expandable_section_block_id` int(11),
  `latest_block_id` int(11),
  `posts_gallery_block_id` int(11),
  `product_detail_block_id` int(11),
  `text_block_id` int(11),
  `text_photo_block_id` int(11),
  `video_block_id` int(11),
  `what_you_need_block_id` int(11),
  `wizard_product_found_block_id` int(11),
  `worldpay_slide_block_id` int(11),
  `product_category_block_id` int(11),
  `product_subcategory_block_id` int(11),
  `bespoke_orders_block_id` int(11),
  `our_people_block_id` int(11),
  PRIMARY KEY (`id`),
  KEY `elastic_pages_page_5e23a50f` (`footer_block_id`),
  KEY `elastic_pages_page_d6970f6e` (`header_block_id`),
  KEY `elastic_pages_page_a39b36af` (`help_box_block_id`),
  KEY `elastic_pages_page_f8de8658` (`main_block_id`),
  KEY `elastic_pages_page_d3768c1a` (`bespoke_screen_block_id`),
  KEY `elastic_pages_page_4c72fd2e` (`expandable_section_block_id`),
  KEY `elastic_pages_page_35605b98` (`latest_block_id`),
  KEY `elastic_pages_page_01622d51` (`posts_gallery_block_id`),
  KEY `elastic_pages_page_8f953be6` (`product_detail_block_id`),
  KEY `elastic_pages_page_3b8403b1` (`text_block_id`),
  KEY `elastic_pages_page_e435e880` (`text_photo_block_id`),
  KEY `elastic_pages_page_5648083f` (`video_block_id`),
  KEY `elastic_pages_page_0ca94ff1` (`what_you_need_block_id`),
  KEY `elastic_pages_page_3e4b89b3` (`wizard_product_found_block_id`),
  KEY `elastic_pages_page_3abd5471` (`worldpay_slide_block_id`),
  KEY `elastic_pages_page_dfa0fc50` (`product_category_block_id`),
  KEY `elastic_pages_page_7f3be506` (`product_subcategory_block_id`),
  KEY `elastic_pages_page_29440b7a` (`bespoke_orders_block_id`),
  KEY `elastic_pages_page_aca3eecf` (`our_people_block_id`),
  CONSTRAINT `D28fb1bf40a7fc066012d11176698871` FOREIGN KEY (`product_subcategory_block_id`) REFERENCES `elastic_pages_pagesubcategoryblock` (`id`),
  CONSTRAINT `D5f49e0d0589012cb7a5a82b348b5b52` FOREIGN KEY (`what_you_need_block_id`) REFERENCES `elastic_pages_pagewhatyouneedblock` (`id`),
  CONSTRAINT `D75829d800549317f0ba6d8d54eabe60` FOREIGN KEY (`bespoke_screen_block_id`) REFERENCES `elastic_pages_bespokescreenblock` (`id`),
  CONSTRAINT `D83046a03925532af4de5d1d97e77349` FOREIGN KEY (`posts_gallery_block_id`) REFERENCES `elastic_pages_postsgalleryblock` (`id`),
  CONSTRAINT `c5c2daf7663cf26c11c38e144f9f7788` FOREIGN KEY (`product_category_block_id`) REFERENCES `elastic_pages_pagecategoryblock` (`id`),
  CONSTRAINT `ccd201fd8d080f97a5316b4cf2f71387` FOREIGN KEY (`product_detail_block_id`) REFERENCES `elastic_pages_productdetailblock` (`id`),
  CONSTRAINT `d3620ddbbab217e32dca5f83d2b65dca` FOREIGN KEY (`expandable_section_block_id`) REFERENCES `elastic_pages_expandablesectionblock` (`id`),
  CONSTRAINT `eefe7eb9e2bdec3fa107b67b783d4985` FOREIGN KEY (`wizard_product_found_block_id`) REFERENCES `elastic_pages_wizardproductfoundblock` (`id`),
  CONSTRAINT `ela_footer_block_id_51ae53b5_fk_elastic_pages_pagefooterblock_id` FOREIGN KEY (`footer_block_id`) REFERENCES `elastic_pages_pagefooterblock` (`id`),
  CONSTRAINT `ela_header_block_id_3b756698_fk_elastic_pages_pageheaderblock_id` FOREIGN KEY (`header_block_id`) REFERENCES `elastic_pages_pageheaderblock` (`id`),
  CONSTRAINT `elastic_latest_block_id_9df250ce_fk_elastic_pages_latestblock_id` FOREIGN KEY (`latest_block_id`) REFERENCES `elastic_pages_latestblock` (`id`),
  CONSTRAINT `elastic_main_block_id_d487b31c_fk_elastic_pages_pagemainblock_id` FOREIGN KEY (`main_block_id`) REFERENCES `elastic_pages_pagemainblock` (`id`),
  CONSTRAINT `elastic_p_video_block_id_c45a81be_fk_elastic_pages_videoblock_id` FOREIGN KEY (`video_block_id`) REFERENCES `elastic_pages_videoblock` (`id`),
  CONSTRAINT `elastic_pag_text_block_id_90d770ec_fk_elastic_pages_textblock_id` FOREIGN KEY (`text_block_id`) REFERENCES `elastic_pages_textblock` (`id`),
  CONSTRAINT `f654e7d843684a3962aebd6fe11500d1` FOREIGN KEY (`worldpay_slide_block_id`) REFERENCES `elastic_pages_pageworldpayscreenblock` (`id`),
  CONSTRAINT `fd0d55f876db1fa153dfd3beb17e22ef` FOREIGN KEY (`bespoke_orders_block_id`) REFERENCES `elastic_pages_bespokeordersblock` (`id`),
  CONSTRAINT `help_box_block_id_f7f72947_fk_elastic_pages_pagehelpboxblock_id` FOREIGN KEY (`help_box_block_id`) REFERENCES `elastic_pages_pagehelpboxblock` (`id`),
  CONSTRAINT `our_people_block_id_9fb3529c_fk_elastic_pages_ourpeopleblock_id` FOREIGN KEY (`our_people_block_id`) REFERENCES `elastic_pages_ourpeopleblock` (`id`),
  CONSTRAINT `text_photo_block_id_ae1f9693_fk_elastic_pages_textphotoblock_id` FOREIGN KEY (`text_photo_block_id`) REFERENCES `elastic_pages_textphotoblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_page`
--

LOCK TABLES `elastic_pages_page` WRITE;
/*!40000 ALTER TABLE `elastic_pages_page` DISABLE KEYS */;
INSERT INTO `elastic_pages_page` VALUES (1,'Test Page Not Found','Test Page Not Found, created from initial date','page_not_found','Page Not Found',1,1,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'Test Home Page','Test Home Page, created from initial date','home','Home',1,1,1,NULL,1,NULL,1,1,NULL,NULL,NULL,NULL,1,NULL,1,NULL,NULL,NULL,NULL),(3,'Test About Us Page','Test About Us Page, created from initial date','about_us','About Us',1,1,1,1,NULL,1,1,NULL,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'Test Promo Page','Test Promo Page, created from initial date','promotion','Promo',1,1,1,1,NULL,1,1,NULL,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'Test Terms & Conditions Page','Test Terms & Conditions Page, created from initial date','terms_&_conditions','Terms & Conditions',1,1,1,1,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,'Test Wizard Product Found','Test Wizard Product Found, created from initial date','product_found','Products found',1,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL),(7,'Test Product Detail Page','Test Product Detail Page, created from initial date','product-product_detail','Product Detail',1,1,1,NULL,1,NULL,1,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,'Test Product Category Page','Test Product Category Page, created from initial date','product-technology','Product Category',1,1,1,1,1,NULL,1,1,NULL,NULL,NULL,NULL,1,NULL,NULL,1,NULL,NULL,NULL),(9,'Test Product SubCategory Page','Test Product SubCategory Page, created from initial date','product-technology_detail','Product SubCategory',1,1,1,1,1,NULL,1,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,1,NULL,NULL),(10,'Test Bespoke Orders','Test Bespoke Orders Page, created from initial date','products-bespoke_orders','Bespoke Orders',1,1,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL),(11,'Test Our People','Test Our People, created from initial date','company-our_people','Our People',1,1,1,1,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `elastic_pages_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagebutton`
--

DROP TABLE IF EXISTS `elastic_pages_pagebutton`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagebutton` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `title` varchar(32) NOT NULL,
  `color` varchar(32) NOT NULL,
  `glyphicon` varchar(1) NOT NULL,
  `glyphicon_position` varchar(1) NOT NULL,
  `external_link` varchar(255) DEFAULT NULL,
  `is_target_link` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagebutton`
--

LOCK TABLES `elastic_pages_pagebutton` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagebutton` DISABLE KEYS */;
/*!40000 ALTER TABLE `elastic_pages_pagebutton` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagecategoryblock`
--

DROP TABLE IF EXISTS `elastic_pages_pagecategoryblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagecategoryblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagecategoryblock`
--

LOCK TABLES `elastic_pages_pagecategoryblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagecategoryblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagecategoryblock` VALUES (1,'Test Product Category Block','Test Product Category Block, created from initial date');
/*!40000 ALTER TABLE `elastic_pages_pagecategoryblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagefooterblock`
--

DROP TABLE IF EXISTS `elastic_pages_pagefooterblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagefooterblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `contact` varchar(128) DEFAULT NULL,
  `t_copy_right` varchar(255) NOT NULL,
  `a_back_top` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagefooterblock`
--

LOCK TABLES `elastic_pages_pagefooterblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagefooterblock` VALUES (1,'Test Footer','Test Footer, created from initial date','Contact','<strong>© 2015 Densitron Technologies.</strong> A <strong>Quixant</strong> Company.',1);
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagefooterblock_a_link`
--

DROP TABLE IF EXISTS `elastic_pages_pagefooterblock_a_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagefooterblock_a_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pagefooterblock_id` int(11) NOT NULL,
  `pageheaddropmenuelement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pagefooterblock_a_pagefooterblock_id_3253e621_uniq` (`pagefooterblock_id`,`pageheaddropmenuelement_id`),
  KEY `D9f7c07acc69877eb79f34aafec2ad47` (`pageheaddropmenuelement_id`),
  CONSTRAINT `D9f7c07acc69877eb79f34aafec2ad47` FOREIGN KEY (`pageheaddropmenuelement_id`) REFERENCES `elastic_pages_pageheaddropmenuelement` (`id`),
  CONSTRAINT `pagefooterblock_id_32bf7665_fk_elastic_pages_pagefooterblock_id` FOREIGN KEY (`pagefooterblock_id`) REFERENCES `elastic_pages_pagefooterblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagefooterblock_a_link`
--

LOCK TABLES `elastic_pages_pagefooterblock_a_link` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock_a_link` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagefooterblock_a_link` VALUES (1,1,23),(2,1,24);
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock_a_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagefooterblock_contact_address`
--

DROP TABLE IF EXISTS `elastic_pages_pagefooterblock_contact_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagefooterblock_contact_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pagefooterblock_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pagefooterblock_c_pagefooterblock_id_b227d5ad_uniq` (`pagefooterblock_id`,`address_id`),
  KEY `elastic_pages_pagefoot_address_id_2c0a3a5e_fk_address_address_id` (`address_id`),
  CONSTRAINT `elastic_pages_pagefoot_address_id_2c0a3a5e_fk_address_address_id` FOREIGN KEY (`address_id`) REFERENCES `address_address` (`id`),
  CONSTRAINT `pagefooterblock_id_bd19cdd5_fk_elastic_pages_pagefooterblock_id` FOREIGN KEY (`pagefooterblock_id`) REFERENCES `elastic_pages_pagefooterblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagefooterblock_contact_address`
--

LOCK TABLES `elastic_pages_pagefooterblock_contact_address` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock_contact_address` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagefooterblock_contact_address` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock_contact_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagefooterblock_top_links`
--

DROP TABLE IF EXISTS `elastic_pages_pagefooterblock_top_links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagefooterblock_top_links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pagefooterblock_id` int(11) NOT NULL,
  `pageheaddropmenu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pagefooterblock_t_pagefooterblock_id_2421242c_uniq` (`pagefooterblock_id`,`pageheaddropmenu_id`),
  KEY `e6f7e4f47c9f640de9a8682111fc19a7` (`pageheaddropmenu_id`),
  CONSTRAINT `e6f7e4f47c9f640de9a8682111fc19a7` FOREIGN KEY (`pageheaddropmenu_id`) REFERENCES `elastic_pages_pageheaddropmenu` (`id`),
  CONSTRAINT `pagefooterblock_id_46876926_fk_elastic_pages_pagefooterblock_id` FOREIGN KEY (`pagefooterblock_id`) REFERENCES `elastic_pages_pagefooterblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagefooterblock_top_links`
--

LOCK TABLES `elastic_pages_pagefooterblock_top_links` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock_top_links` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagefooterblock_top_links` VALUES (1,1,2),(2,1,3),(3,1,4),(4,1,5);
/*!40000 ALTER TABLE `elastic_pages_pagefooterblock_top_links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheaddropmenu`
--

DROP TABLE IF EXISTS `elastic_pages_pageheaddropmenu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheaddropmenu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `title` varchar(64) NOT NULL,
  `external_link` varchar(255) DEFAULT NULL,
  `priority` smallint(6) NOT NULL,
  `is_target_link` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheaddropmenu`
--

LOCK TABLES `elastic_pages_pageheaddropmenu` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheaddropmenu` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheaddropmenu` VALUES (1,'Test Home','Home','/',1,0),(2,'Test Products','Products','/products/',1,0),(3,'Test Services','Services','/services/',1,0),(4,'Test Knowledge Base','Knowledge Base','/knowledge-base/',1,0),(5,'Test Company','Company','/company/',1,0),(6,'Test Contact','Contact','/contact/',1,0);
/*!40000 ALTER TABLE `elastic_pages_pageheaddropmenu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheaddropmenu_drop_links`
--

DROP TABLE IF EXISTS `elastic_pages_pageheaddropmenu_drop_links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheaddropmenu_drop_links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pageheaddropmenu_id` int(11) NOT NULL,
  `pageheaddropmenuelement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pageheaddropmenu_pageheaddropmenu_id_291e2404_uniq` (`pageheaddropmenu_id`,`pageheaddropmenuelement_id`),
  KEY `f637f0a257dcc16ae5c320b64d31efcb` (`pageheaddropmenuelement_id`),
  CONSTRAINT `D26f5f94ec9d851886f6da8d1b802163` FOREIGN KEY (`pageheaddropmenu_id`) REFERENCES `elastic_pages_pageheaddropmenu` (`id`),
  CONSTRAINT `f637f0a257dcc16ae5c320b64d31efcb` FOREIGN KEY (`pageheaddropmenuelement_id`) REFERENCES `elastic_pages_pageheaddropmenuelement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheaddropmenu_drop_links`
--

LOCK TABLES `elastic_pages_pageheaddropmenu_drop_links` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheaddropmenu_drop_links` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheaddropmenu_drop_links` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(8,3,8),(9,3,9),(10,3,10),(11,3,11),(12,3,12),(13,5,13),(14,5,14),(15,5,15),(16,5,16),(17,5,17),(18,5,18),(19,5,19),(20,5,20),(21,5,21),(22,5,22);
/*!40000 ALTER TABLE `elastic_pages_pageheaddropmenu_drop_links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheaddropmenuelement`
--

DROP TABLE IF EXISTS `elastic_pages_pageheaddropmenuelement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheaddropmenuelement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `title` varchar(64) NOT NULL,
  `external_link` varchar(255) DEFAULT NULL,
  `priority` smallint(6) NOT NULL,
  `is_target_link` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheaddropmenuelement`
--

LOCK TABLES `elastic_pages_pageheaddropmenuelement` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheaddropmenuelement` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheaddropmenuelement` VALUES (1,'Test OLEDs','OLEDs','/products/oleds/',1,0),(2,'Test TFTs','TFTs','/products/tfts/',1,0),(3,'Test Monochrome','Monochrome','/products/monochrome/',1,0),(4,'Test Touch Panels','Touch Panels','/products/touch-panels/',1,0),(5,'Test Low Power','Low Power','/products/low-power/',1,0),(6,'Test Densipaper','Densipaper','/products/densipaper/',1,0),(7,'Test Bespoke Orders','Bespoke Orders','/products/bespoke-orders/',1,0),(8,'Test Optical Bonding','Optical Bonding','/services/optical-bonding/',1,0),(9,'Test GUI Design Tools','GUI Design Tools','/services/gui-design-tools/',1,0),(10,'Test RipDraw','RipDraw','/services/ripdraw/',1,0),(11,'Test EDS','EDS','/services/eds/',1,0),(12,'Test Engineering Design','Engineering Design','/services/engineering-design/',1,0),(13,'Test Global reach','Global reach','/company/global-reach/',1,0),(14,'Test Our people','Our people','/company/our-people/',1,0),(15,'Test Investor Relations','Investor Relations','/company/investor-relations/',1,0),(16,'Test Key contacts (AIM)','Key contacts (AIM)','/company/key-contacts-aim/',1,0),(17,'Test Press Releases','Press Releases','/company/press-releases/',1,0),(18,'Test News','News','/company/news/',1,0),(19,'Test About Us','About Us','/company/about-us/',1,0),(20,'Test Events','Events','/company/events/',1,0),(21,'Test Case studies','Case studies','/company/case-studies/',1,0),(22,'Test Career Opportunities','Career Opportunities','/company/career-opportunities/',1,0),(23,'Test Privacy','Privacy','privacy',1,0),(24,'Test Terms & Conditions','Terms & Conditions','terms-conditions',1,0);
/*!40000 ALTER TABLE `elastic_pages_pageheaddropmenuelement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheaderblock`
--

DROP TABLE IF EXISTS `elastic_pages_pageheaderblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheaderblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `is_auth_menu` tinyint(1) NOT NULL,
  `logo_image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheaderblock`
--

LOCK TABLES `elastic_pages_pageheaderblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheaderblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheaderblock` VALUES (1,'Test Header','Test Header, created from initial date',1,'/static/test_images/logo-v2.jpeg');
/*!40000 ALTER TABLE `elastic_pages_pageheaderblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheaderblock_main_menus_elements`
--

DROP TABLE IF EXISTS `elastic_pages_pageheaderblock_main_menus_elements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheaderblock_main_menus_elements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pageheaderblock_id` int(11) NOT NULL,
  `pageheaddropmenu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pageheaderblock_m_pageheaderblock_id_6ef54a29_uniq` (`pageheaderblock_id`,`pageheaddropmenu_id`),
  KEY `D20d8e271246d1894aa13b737722af30` (`pageheaddropmenu_id`),
  CONSTRAINT `D20d8e271246d1894aa13b737722af30` FOREIGN KEY (`pageheaddropmenu_id`) REFERENCES `elastic_pages_pageheaddropmenu` (`id`),
  CONSTRAINT `pageheaderblock_id_d146e940_fk_elastic_pages_pageheaderblock_id` FOREIGN KEY (`pageheaderblock_id`) REFERENCES `elastic_pages_pageheaderblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheaderblock_main_menus_elements`
--

LOCK TABLES `elastic_pages_pageheaderblock_main_menus_elements` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheaderblock_main_menus_elements` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheaderblock_main_menus_elements` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6);
/*!40000 ALTER TABLE `elastic_pages_pageheaderblock_main_menus_elements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheaderblock_soc_links`
--

DROP TABLE IF EXISTS `elastic_pages_pageheaderblock_soc_links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheaderblock_soc_links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pageheaderblock_id` int(11) NOT NULL,
  `pageheadsoclink_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pageheaderblock_s_pageheaderblock_id_b9d74be5_uniq` (`pageheaderblock_id`,`pageheadsoclink_id`),
  KEY `pageheadsoclink_id_b8d1e2e8_fk_elastic_pages_pageheadsoclink_id` (`pageheadsoclink_id`),
  CONSTRAINT `pageheaderblock_id_179350b6_fk_elastic_pages_pageheaderblock_id` FOREIGN KEY (`pageheaderblock_id`) REFERENCES `elastic_pages_pageheaderblock` (`id`),
  CONSTRAINT `pageheadsoclink_id_b8d1e2e8_fk_elastic_pages_pageheadsoclink_id` FOREIGN KEY (`pageheadsoclink_id`) REFERENCES `elastic_pages_pageheadsoclink` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheaderblock_soc_links`
--

LOCK TABLES `elastic_pages_pageheaderblock_soc_links` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheaderblock_soc_links` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheaderblock_soc_links` VALUES (1,1,1),(2,1,2),(3,1,3);
/*!40000 ALTER TABLE `elastic_pages_pageheaderblock_soc_links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageheadsoclink`
--

DROP TABLE IF EXISTS `elastic_pages_pageheadsoclink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageheadsoclink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `soc_image` varchar(100) NOT NULL,
  `external_link` varchar(255) NOT NULL,
  `priority` smallint(6) NOT NULL,
  `is_target_link` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageheadsoclink`
--

LOCK TABLES `elastic_pages_pageheadsoclink` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageheadsoclink` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageheadsoclink` VALUES (1,'Test Twitter Link','/static/test_images/twitter.jpeg','https://twitter.com/',1,0),(2,'Test ShareThis Link','/static/test_images/sharethis.jpeg','http://www.sharethis.com',1,0),(3,'Test LinkedIn Link','/static/test_images/linkedin.jpeg','https://ua.linkedin.com',1,0);
/*!40000 ALTER TABLE `elastic_pages_pageheadsoclink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagehelpboxblock`
--

DROP TABLE IF EXISTS `elastic_pages_pagehelpboxblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagehelpboxblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `text` longtext NOT NULL,
  `button_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `elastic_pages__button_id_78750aba_fk_elastic_pages_pagebutton_id` (`button_id`),
  CONSTRAINT `elastic_pages__button_id_78750aba_fk_elastic_pages_pagebutton_id` FOREIGN KEY (`button_id`) REFERENCES `elastic_pages_pagebutton` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagehelpboxblock`
--

LOCK TABLES `elastic_pages_pagehelpboxblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagehelpboxblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagehelpboxblock` VALUES (1,'Test Help Box','Test Help Box, created from initial date','<span>Densitron Technologles</span> is a world leading designer and manufacturer of information display systems.',NULL);
/*!40000 ALTER TABLE `elastic_pages_pagehelpboxblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagemainblock`
--

DROP TABLE IF EXISTS `elastic_pages_pagemainblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagemainblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `background_image` varchar(100) NOT NULL,
  `title` varchar(128) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagemainblock`
--

LOCK TABLES `elastic_pages_pagemainblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagemainblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagemainblock` VALUES (1,'Test Main Box','Test Main Box, created from initial date','/static/test_images/densitron-image.jpeg','Test Main Box','Nulla dui purus, eleifend vel, consequat non, dictuma porta, nulla. Duis ante mi, laoreet ut, commodo eleifend, crsus nec, lorem. Aenean eu est. Etiam imperdient tupis. Praesent nec augue.');
/*!40000 ALTER TABLE `elastic_pages_pagemainblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagesubcategoryblock`
--

DROP TABLE IF EXISTS `elastic_pages_pagesubcategoryblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagesubcategoryblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagesubcategoryblock`
--

LOCK TABLES `elastic_pages_pagesubcategoryblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagesubcategoryblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagesubcategoryblock` VALUES (1,'Test Product SubCategory Block','Test Product SubCategory Block, created from initial date');
/*!40000 ALTER TABLE `elastic_pages_pagesubcategoryblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pagewhatyouneedblock`
--

DROP TABLE IF EXISTS `elastic_pages_pagewhatyouneedblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pagewhatyouneedblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `left_column_title` varchar(64) NOT NULL,
  `is_touch` tinyint(1) NOT NULL,
  `is_colour` tinyint(1) NOT NULL,
  `middle_column_title` varchar(64) NOT NULL,
  `middle_column_label` varchar(64) NOT NULL,
  `middle_column_caption` varchar(64) NOT NULL,
  `right_column_title` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pagewhatyouneedblock`
--

LOCK TABLES `elastic_pages_pagewhatyouneedblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pagewhatyouneedblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pagewhatyouneedblock` VALUES (1,'Test What You Need Block','Test What You Need Block, created from initial date','Tell us what you need...','Custom',1,1,'Existing','Enter product # or keyword','Eg. lorem ipsum dolor amet','Popular');
/*!40000 ALTER TABLE `elastic_pages_pagewhatyouneedblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageworldpayscreenblock`
--

DROP TABLE IF EXISTS `elastic_pages_pageworldpayscreenblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageworldpayscreenblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `auto_slide` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageworldpayscreenblock`
--

LOCK TABLES `elastic_pages_pageworldpayscreenblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageworldpayscreenblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageworldpayscreenblock` VALUES (1,'Test World Pay Screen Block','Test World Pay Screen Block, created from initial date',1);
/*!40000 ALTER TABLE `elastic_pages_pageworldpayscreenblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_pageworldpayscreenblock_slide_elem`
--

DROP TABLE IF EXISTS `elastic_pages_pageworldpayscreenblock_slide_elem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_pageworldpayscreenblock_slide_elem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pageworldpayscreenblock_id` int(11) NOT NULL,
  `slideelement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_pageworld_pageworldpayscreenblock_id_f085ec3c_uniq` (`pageworldpayscreenblock_id`,`slideelement_id`),
  KEY `elasti_slideelement_id_4455a0b1_fk_elastic_pages_slideelement_id` (`slideelement_id`),
  CONSTRAINT `D0cbc20635e6789deaf5a1957dd7eedb` FOREIGN KEY (`pageworldpayscreenblock_id`) REFERENCES `elastic_pages_pageworldpayscreenblock` (`id`),
  CONSTRAINT `elasti_slideelement_id_4455a0b1_fk_elastic_pages_slideelement_id` FOREIGN KEY (`slideelement_id`) REFERENCES `elastic_pages_slideelement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_pageworldpayscreenblock_slide_elem`
--

LOCK TABLES `elastic_pages_pageworldpayscreenblock_slide_elem` WRITE;
/*!40000 ALTER TABLE `elastic_pages_pageworldpayscreenblock_slide_elem` DISABLE KEYS */;
INSERT INTO `elastic_pages_pageworldpayscreenblock_slide_elem` VALUES (1,1,1),(2,1,2),(3,1,3);
/*!40000 ALTER TABLE `elastic_pages_pageworldpayscreenblock_slide_elem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_postsgalleryblock`
--

DROP TABLE IF EXISTS `elastic_pages_postsgalleryblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_postsgalleryblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title_left` varchar(128) NOT NULL,
  `text_left` longtext NOT NULL,
  `image_left` varchar(100) NOT NULL,
  `title_middle` varchar(128) NOT NULL,
  `text_middle` longtext NOT NULL,
  `image_middle` varchar(100) NOT NULL,
  `title_right` varchar(128) NOT NULL,
  `text_right` longtext NOT NULL,
  `image_right` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_postsgalleryblock`
--

LOCK TABLES `elastic_pages_postsgalleryblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_postsgalleryblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_postsgalleryblock` VALUES (1,'Test Gallery Block','Test Gallery Block, created from initial date','TFT in Action','Nulla dui purus, eleifend vel, consequat non, dictuma porta, nulla. Duis ante mi, laoreet ut, commodo eleifend, crsus nec, lorem. Aenean eu est.','/static/test_images/post-image-4.jpeg','OLED in Action','Nulla dui purus, eleifend vel, consequat non, dictuma porta, nulla. Duis ante mi, laoreet ut, commodo eleifend, crsus nec, lorem. Aenean eu est.','/static/test_images/post-image-5.jpeg','Product Wishlist Tool','Nulla dui purus, eleifend vel, consequat non, dictuma porta, nulla. Duis ante mi, laoreet ut, commodo eleifend, crsus nec, lorem. Aenean eu est.','/static/test_images/post-image-6.jpeg');
/*!40000 ALTER TABLE `elastic_pages_postsgalleryblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_productdetailblock`
--

DROP TABLE IF EXISTS `elastic_pages_productdetailblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_productdetailblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_productdetailblock`
--

LOCK TABLES `elastic_pages_productdetailblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_productdetailblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_productdetailblock` VALUES (1,'Test Product Detail Block','Test Product Detail Block, created from initial date');
/*!40000 ALTER TABLE `elastic_pages_productdetailblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_slideelement`
--

DROP TABLE IF EXISTS `elastic_pages_slideelement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_slideelement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `text` longtext NOT NULL,
  `background` varchar(100) NOT NULL,
  `button_id` int(11),
  PRIMARY KEY (`id`),
  KEY `elastic_pages_slideelement_2e479f87` (`button_id`),
  CONSTRAINT `elastic_pages__button_id_c6e84dce_fk_elastic_pages_pagebutton_id` FOREIGN KEY (`button_id`) REFERENCES `elastic_pages_pagebutton` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_slideelement`
--

LOCK TABLES `elastic_pages_slideelement` WRITE;
/*!40000 ALTER TABLE `elastic_pages_slideelement` DISABLE KEYS */;
INSERT INTO `elastic_pages_slideelement` VALUES (1,'Test Slide Element Block','Test Slide Element for World Pay Screen Block, created from initial date','Worldpay Screen Design','8 channel noise suppression system for live events eliminating background noise from preformances','/static/test_images/worldpay-image.jpeg',NULL),(2,'Test Slide Element Block','Test Slide Element for World Pay Screen Block, created from initial date','Worldpay Screen Design','8 channel noise suppression system for live events eliminating background noise from preformances','/static/test_images/worldpay-image.jpeg',NULL),(3,'Test Slide Element Block','Test Slide Element for World Pay Screen Block, created from initial date','Worldpay Screen Design','8 channel noise suppression system for live events eliminating background noise from preformances','/static/test_images/worldpay-image.jpeg',NULL);
/*!40000 ALTER TABLE `elastic_pages_slideelement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_textblock`
--

DROP TABLE IF EXISTS `elastic_pages_textblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_textblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `sub_title` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_textblock`
--

LOCK TABLES `elastic_pages_textblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_textblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_textblock` VALUES (1,'Test Text Block','Test Text Block, created from initial date','Main Heading','Sub Heading');
/*!40000 ALTER TABLE `elastic_pages_textblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_textblock_text_element`
--

DROP TABLE IF EXISTS `elastic_pages_textblock_text_element`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_textblock_text_element` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `textblock_id` int(11) NOT NULL,
  `textelement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elastic_pages_textblock_text_element_textblock_id_b3213653_uniq` (`textblock_id`,`textelement_id`),
  KEY `elastic__textelement_id_f26dbffb_fk_elastic_pages_textelement_id` (`textelement_id`),
  CONSTRAINT `elastic__textelement_id_f26dbffb_fk_elastic_pages_textelement_id` FOREIGN KEY (`textelement_id`) REFERENCES `elastic_pages_textelement` (`id`),
  CONSTRAINT `elastic_page_textblock_id_d128f9fb_fk_elastic_pages_textblock_id` FOREIGN KEY (`textblock_id`) REFERENCES `elastic_pages_textblock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_textblock_text_element`
--

LOCK TABLES `elastic_pages_textblock_text_element` WRITE;
/*!40000 ALTER TABLE `elastic_pages_textblock_text_element` DISABLE KEYS */;
INSERT INTO `elastic_pages_textblock_text_element` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `elastic_pages_textblock_text_element` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_textelement`
--

DROP TABLE IF EXISTS `elastic_pages_textelement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_textelement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `sub_sub_title` varchar(128) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_textelement`
--

LOCK TABLES `elastic_pages_textelement` WRITE;
/*!40000 ALTER TABLE `elastic_pages_textelement` DISABLE KEYS */;
INSERT INTO `elastic_pages_textelement` VALUES (1,'Test Text Block','Test Text Block, created from initial date','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.</br></br> Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.</br></br> Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Fusce oris wisi, ornare id, mollis vel, lacinia vel, massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'),(2,'Test Text Block','Test Text Block, created from initial date','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>.</br></br> Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.</br></br> Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Fusce oris wisi, ornare id, mollis vel, lacinia vel, massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.');
/*!40000 ALTER TABLE `elastic_pages_textelement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_textphotoblock`
--

DROP TABLE IF EXISTS `elastic_pages_textphotoblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_textphotoblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `sub_title` varchar(128) NOT NULL,
  `sub_sub_title` varchar(128) NOT NULL,
  `top_text` longtext NOT NULL,
  `left_photo` varchar(100) NOT NULL,
  `left_photo_caption` varchar(128) NOT NULL,
  `right_text` longtext NOT NULL,
  `middle_text` longtext,
  `right_photo` varchar(100) NOT NULL,
  `right_photo_caption` varchar(128) NOT NULL,
  `left_text` longtext NOT NULL,
  `bottom_text` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_textphotoblock`
--

LOCK TABLES `elastic_pages_textphotoblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_textphotoblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_textphotoblock` VALUES (1,'Test Text Photo Block','Test Text Photo Block, created from initial date','Main Heading','Sub Heading','Sub Sub Heading','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Fusce oris wisi, ornare id, mollis vel, lacinia vel, massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.','/static/test_images/test-photo.jpeg','Image caption','Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.','Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.','/static/test_images/test-photo.jpeg','Image caption','Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit.','');
/*!40000 ALTER TABLE `elastic_pages_textphotoblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_videoblock`
--

DROP TABLE IF EXISTS `elastic_pages_videoblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_videoblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `title` varchar(128) NOT NULL,
  `sub_title` varchar(128) NOT NULL,
  `summary` varchar(128) NOT NULL,
  `text` longtext NOT NULL,
  `video_obj_id` int(11),
  PRIMARY KEY (`id`),
  KEY `elastic_pages_videoblock_756eab30` (`video_obj_id`),
  CONSTRAINT `elastic_pa_video_obj_id_a689e832_fk_elastic_pages_videoobject_id` FOREIGN KEY (`video_obj_id`) REFERENCES `elastic_pages_videoobject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_videoblock`
--

LOCK TABLES `elastic_pages_videoblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_videoblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_videoblock` VALUES (1,'Test Video Block','Test Video Block, created from initial date','Video Title','Video Sub title','Summary','Paragraph copy eleifend vel, <b>highlighted text</b>, dictuma porta, nulla. Duis ante mi, laoreet ut cursus nec, lorem. Aeneat eu est. Etiam imperdiet turpis <a href=\"#\">link within test</a>. Paragraph copy maecenas ut turpis. In vitae ac orci dignissim eleifend. Nunc quis justo. Sed vel ipsum in purus tincidunt pharetra. Sed pulvinar, felis id consectetuer maiesuda, enim nisl mattis elit, a facilisis tortor nibh quis leo. Sed augue lacus, pretium vitae, molestie eget, rhoncus quis, elit. Donec in augue. Fusce oris wisi, ornare id, mollis vel, lacinia vel, massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.',NULL);
/*!40000 ALTER TABLE `elastic_pages_videoblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_videoobject`
--

DROP TABLE IF EXISTS `elastic_pages_videoobject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_videoobject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `video` varchar(100) DEFAULT NULL,
  `embed_video` longtext,
  `sub_name` varchar(128),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_videoobject`
--

LOCK TABLES `elastic_pages_videoobject` WRITE;
/*!40000 ALTER TABLE `elastic_pages_videoobject` DISABLE KEYS */;
INSERT INTO `elastic_pages_videoobject` VALUES (1,'Nashe','Description Description Description  Description Description','videos/SampleVideo_720x480_1mb_rGF9tKC.mp4','','Videp'),(2,'Vimeo','Description Description Description Description v','','<iframe src=\"https://player.vimeo.com/video/152336237?title=0&byline=0\" width=\"500\" height=\"279\" frameborder=\"0\" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>','video'),(3,'Youtube','Description Description Description Description Description','','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/TG_ZEovDDKk\" frameborder=\"0\" allowfullscreen></iframe>','video');
/*!40000 ALTER TABLE `elastic_pages_videoobject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elastic_pages_wizardproductfoundblock`
--

DROP TABLE IF EXISTS `elastic_pages_wizardproductfoundblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elastic_pages_wizardproductfoundblock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elastic_pages_wizardproductfoundblock`
--

LOCK TABLES `elastic_pages_wizardproductfoundblock` WRITE;
/*!40000 ALTER TABLE `elastic_pages_wizardproductfoundblock` DISABLE KEYS */;
INSERT INTO `elastic_pages_wizardproductfoundblock` VALUES (1,'Test Wizard Product Found Block','Test Wizard Product Found Block, created from initial date');
/*!40000 ALTER TABLE `elastic_pages_wizardproductfoundblock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_category`
--

DROP TABLE IF EXISTS `products_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `technology_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_catego_technology_id_3b60af46_fk_products_technology_id` (`technology_id`),
  CONSTRAINT `products_catego_technology_id_3b60af46_fk_products_technology_id` FOREIGN KEY (`technology_id`) REFERENCES `products_technology` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_category`
--

LOCK TABLES `products_category` WRITE;
/*!40000 ALTER TABLE `products_category` DISABLE KEYS */;
INSERT INTO `products_category` VALUES (1,'Full Colour OLED','Test Full Colour OLED',1,'/static/test_images/test-product-bar-image-2.jpeg'),(2,'Mono PMOLED','Test Mono PMOLED',1,'/static/test_images/test-product-bar-image-2.jpeg'),(3,'Alphanumeric PLOMED','Test Alphanumeric PLOMED',1,'/static/test_images/test-product-bar-image-2.jpeg'),(4,'Custom OLED','Test Custom OLED',1,'/static/test_images/test-product-bar-image-2.jpeg'),(5,'TFT','Test TFT',2,'/static/test_images/test-product-bar-image-2.jpeg'),(6,'Touch TFT','Test Touch TFT',2,'/static/test_images/test-product-bar-image-2.jpeg'),(7,'Smart TFT','Test Smart TFT',2,'/static/test_images/test-product-bar-image-2.jpeg'),(8,'Sun View TFT','Test Sun View TFT',2,'/static/test_images/test-product-bar-image-2.jpeg'),(9,'TFT Kits','Test TFT Kits',2,'/static/test_images/test-product-bar-image-2.jpeg'),(10,'TFT Projects','Test TFT Projects',2,'/static/test_images/test-product-bar-image-2.jpeg'),(11,'1U/2U Format LCD','Test 1U/2U Format LCD',3,'/static/test_images/test-product-bar-image-2.jpeg'),(12,'Mono Graphic LCD','Test Mono Graphic LCD',3,'/static/test_images/test-product-bar-image-2.jpeg'),(13,'Custom Modules','Test Custom Modules',3,'/static/test_images/test-product-bar-image-2.jpeg'),(14,'1U/2U Eval Kits','Test 1U/2U Eval Kits',3,'/static/test_images/test-product-bar-image-2.jpeg'),(15,'Multi-Touch PCT','Test Multi-Touch PCT',4,'/static/test_images/test-product-bar-image-2.jpeg'),(16,'5-Wire Resistive','Test 5-Wire Resistive',4,'/static/test_images/test-product-bar-image-2.jpeg'),(17,'4-Wire Resistive','Test 4-Wire Resistive',4,'/static/test_images/test-product-bar-image-2.jpeg'),(18,'Glass Resistive','Test Glass Resistive',4,'/static/test_images/test-product-bar-image-2.jpeg'),(19,'Haptic Touch','Test Haptic Touch',4,'/static/test_images/test-product-bar-image-2.jpeg'),(20,'Screens','Test Screens',4,'/static/test_images/test-product-bar-image-2.jpeg'),(21,'Touch Controllers','Test Touch Controllers',4,'/static/test_images/test-product-bar-image-2.jpeg'),(22,'E-Paper Displays','Test E-Paper Displays',5,'/static/test_images/test-product-bar-image-2.jpeg'),(23,'E-Paper Extension Kits','Test E-Paper Extension Kits',5,'/static/test_images/test-product-bar-image-2.jpeg'),(24,'E-Paper Developer Kits','Test E-Paper Developer Kits',5,'/static/test_images/test-product-bar-image-2.jpeg'),(25,'AdapTag Wireless Kit','Test AdapTag Wireless Kit',5,'/static/test_images/test-product-bar-image-2.jpeg'),(26,'DensiPaper Products','Test DensiPaper Products',5,'/static/test_images/test-product-bar-image-2.jpeg'),(27,'E-Paper Shop','Test E-Paper Shop',5,'/static/test_images/test-product-bar-image-2.jpeg');
/*!40000 ALTER TABLE `products_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_controller`
--

DROP TABLE IF EXISTS `products_controller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_controller` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_controller`
--

LOCK TABLES `products_controller` WRITE;
/*!40000 ALTER TABLE `products_controller` DISABLE KEYS */;
INSERT INTO `products_controller` VALUES (1,'ILI2839');
/*!40000 ALTER TABLE `products_controller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_feature`
--

DROP TABLE IF EXISTS `products_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_feature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_feature`
--

LOCK TABLES `products_feature` WRITE;
/*!40000 ALTER TABLE `products_feature` DISABLE KEYS */;
INSERT INTO `products_feature` VALUES (1,'IPS'),(2,'Slim profile'),(3,'MVA'),(4,'Sunlight Readable'),(5,'CPU I/F'),(6,'High Brightness'),(7,'UWV Polarizer');
/*!40000 ALTER TABLE `products_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_interface`
--

DROP TABLE IF EXISTS `products_interface`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_interface` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_interface`
--

LOCK TABLES `products_interface` WRITE;
/*!40000 ALTER TABLE `products_interface` DISABLE KEYS */;
INSERT INTO `products_interface` VALUES (1,'I2C');
/*!40000 ALTER TABLE `products_interface` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_lowpowerproduct`
--

DROP TABLE IF EXISTS `products_lowpowerproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_lowpowerproduct` (
  `product_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`product_ptr_id`),
  CONSTRAINT `products_lowpower_product_ptr_id_892e0f2e_fk_products_product_id` FOREIGN KEY (`product_ptr_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_lowpowerproduct`
--

LOCK TABLES `products_lowpowerproduct` WRITE;
/*!40000 ALTER TABLE `products_lowpowerproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_lowpowerproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_monochromeproduct`
--

DROP TABLE IF EXISTS `products_monochromeproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_monochromeproduct` (
  `product_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`product_ptr_id`),
  CONSTRAINT `products_monochro_product_ptr_id_5d1eb056_fk_products_product_id` FOREIGN KEY (`product_ptr_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_monochromeproduct`
--

LOCK TABLES `products_monochromeproduct` WRITE;
/*!40000 ALTER TABLE `products_monochromeproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_monochromeproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_oledproduct`
--

DROP TABLE IF EXISTS `products_oledproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_oledproduct` (
  `product_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`product_ptr_id`),
  CONSTRAINT `products_oledprod_product_ptr_id_ba43e21b_fk_products_product_id` FOREIGN KEY (`product_ptr_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_oledproduct`
--

LOCK TABLES `products_oledproduct` WRITE;
/*!40000 ALTER TABLE `products_oledproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_oledproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_os`
--

DROP TABLE IF EXISTS `products_os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_os` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_os`
--

LOCK TABLES `products_os` WRITE;
/*!40000 ALTER TABLE `products_os` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `dimension_w` decimal(6,2) NOT NULL,
  `dimension_h` decimal(6,2) NOT NULL,
  `dimension_d` decimal(6,2) NOT NULL,
  `size` decimal(4,2) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_product_b583a629` (`category_id`),
  CONSTRAINT `products_product_category_id_9b594869_fk_products_category_id` FOREIGN KEY (`category_id`) REFERENCES `products_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (1,'MZEEaVgsdp',12.68,96.96,75.58,4.30,5),(2,'nphCoHXcOL',56.90,4.51,12.18,4.30,5),(3,'SuYeGsiYXP',3.80,22.77,102.60,4.20,5),(4,'FRvLRVLMMb',57.22,79.25,111.16,4.20,5),(5,'uuRQHiRUDV',71.96,40.66,29.75,4.30,5),(6,'MJDFalNQaK',76.40,114.29,86.50,4.20,5),(7,'FoybzqQVIe',107.16,20.42,8.90,4.30,5),(8,'RqRyahEjkj',86.84,19.35,58.16,4.20,5),(9,'LpmKPjuXuB',31.73,33.41,75.29,4.20,5),(10,'kogmThAaBq',116.60,89.23,53.93,4.30,5),(11,'lVpMPKYFwC',88.77,28.41,32.20,4.20,5),(12,'KGaNRXumqZ',49.11,4.10,35.90,4.30,5),(13,'hLHiuElrIY',123.33,121.91,2.95,4.20,5),(14,'pgSDdwbFoN',78.93,89.93,5.56,4.20,5),(15,'tdbQyssFBA',60.26,10.30,70.40,4.30,5),(16,'CrLyBCmxmf',92.71,68.23,52.77,4.30,5),(17,'TByQFugUXP',32.97,20.80,123.39,4.20,5),(18,'CHLiryMyfU',37.18,63.35,59.86,4.20,5),(19,'LjvxxWfYyR',95.85,95.78,112.47,4.20,5),(20,'UtsNJLfYWV',18.17,116.23,94.40,4.30,5),(21,'Kw test JVb',60.85,106.86,18.22,4.30,5),(22,'Kw test QbG',53.34,55.18,94.56,4.30,5),(23,'Kw test lvu',64.27,16.60,68.87,4.30,5),(24,'GxnotokHoq',25.93,8.85,122.78,4.30,15),(25,'SsUBCfpCsR',13.32,8.91,98.29,4.30,15),(26,'KoKaWTckom',65.20,24.90,2.42,4.30,15),(27,'FWHdnYtDVL',51.77,71.31,85.23,4.30,15),(28,'YFpFSsYdjA',44.91,101.40,56.10,4.30,15),(29,'WFGxfnzEEN',10.31,9.47,27.68,4.30,15),(30,'KTSgwcjQGQ',83.89,37.30,109.69,4.30,15),(31,'dZRjLkKvQC',67.96,108.96,113.88,4.30,15),(32,'xDCSymwJGI',84.50,73.27,33.60,4.30,15),(33,'zGfugOzWtq',86.64,25.49,43.78,4.30,15),(34,'zMOxpzYbbb',68.39,10.21,30.85,4.30,15),(35,'mVVWFZthUK',55.21,57.70,58.64,4.30,15),(36,'gIfBpphITF',72.38,91.97,48.22,4.30,15),(37,'gTbxeeEHQI',103.70,20.14,120.19,4.30,15),(38,'VhzXalrwIV',117.80,19.50,37.68,4.30,15),(39,'WZwnvjcDso',22.19,122.70,108.41,4.30,15),(40,'UzBMfMaFbq',5.97,77.93,113.40,4.30,15),(41,'FVGQAulPLN',21.99,113.46,31.12,4.30,15),(42,'YPPzcIuCre',11.70,62.95,67.43,4.30,15),(43,'tOyJMPZWRs',6.63,19.00,68.70,4.30,15);
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productimage`
--

DROP TABLE IF EXISTS `products_productimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `image` varchar(100) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productimage_product_id_e747596a_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_productimage_product_id_e747596a_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productimage`
--

LOCK TABLES `products_productimage` WRITE;
/*!40000 ALTER TABLE `products_productimage` DISABLE KEYS */;
INSERT INTO `products_productimage` VALUES (1,'Test product image','/static/test-product-image.jpeg',1),(2,'Test product image','/static/test-product-image.jpeg',2),(3,'Test product image','/static/test-product-image.jpeg',3),(4,'Test product image','/static/test-product-image.jpeg',4),(5,'Test product image','/static/test-product-image.jpeg',5),(6,'Test product image','/static/test-product-image.jpeg',6),(7,'Test product image','/static/test-product-image.jpeg',7),(8,'Test product image','/static/test-product-image.jpeg',8),(9,'Test product image','/static/test-product-image.jpeg',9),(10,'Test product image','/static/test-product-image.jpeg',10),(11,'Test product image','/static/test-product-image.jpeg',11),(12,'Test product image','/static/test-product-image.jpeg',12),(13,'Test product image','/static/test-product-image.jpeg',13),(14,'Test product image','/static/test-product-image.jpeg',14),(15,'Test product image','/static/test-product-image.jpeg',15),(16,'Test product image','/static/test-product-image.jpeg',16),(17,'Test product image','/static/test-product-image.jpeg',17),(18,'Test product image','/static/test-product-image.jpeg',18),(19,'Test product image','/static/test-product-image.jpeg',19),(20,'Test product image','/static/test-product-image.jpeg',20),(21,'Test product image','/static/test-product-image.jpeg',21),(22,'Test product image','/static/test-product-image.jpeg',22),(23,'Test product image','/static/test-product-image.jpeg',23),(24,'Test product image','/static/test-product-image.jpeg',24),(25,'Test product image','/static/test-product-image.jpeg',25),(26,'Test product image','/static/test-product-image.jpeg',26),(27,'Test product image','/static/test-product-image.jpeg',27),(28,'Test product image','/static/test-product-image.jpeg',28),(29,'Test product image','/static/test-product-image.jpeg',29),(30,'Test product image','/static/test-product-image.jpeg',30),(31,'Test product image','/static/test-product-image.jpeg',31),(32,'Test product image','/static/test-product-image.jpeg',32),(33,'Test product image','/static/test-product-image.jpeg',33),(34,'Test product image','/static/test-product-image.jpeg',34),(35,'Test product image','/static/test-product-image.jpeg',35),(36,'Test product image','/static/test-product-image.jpeg',36),(37,'Test product image','/static/test-product-image.jpeg',37),(38,'Test product image','/static/test-product-image.jpeg',38),(39,'Test product image','/static/test-product-image.jpeg',39),(40,'Test product image','/static/test-product-image.jpeg',40),(41,'Test product image','/static/test-product-image.jpeg',41),(42,'Test product image','/static/test-product-image.jpeg',42),(43,'Test product image','/static/test-product-image.jpeg',43);
/*!40000 ALTER TABLE `products_productimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_structure`
--

DROP TABLE IF EXISTS `products_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_structure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_structure`
--

LOCK TABLES `products_structure` WRITE;
/*!40000 ALTER TABLE `products_structure` DISABLE KEYS */;
INSERT INTO `products_structure` VALUES (1,'OGS');
/*!40000 ALTER TABLE `products_structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_technology`
--

DROP TABLE IF EXISTS `products_technology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_technology` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_technology`
--

LOCK TABLES `products_technology` WRITE;
/*!40000 ALTER TABLE `products_technology` DISABLE KEYS */;
INSERT INTO `products_technology` VALUES (1,'OLEDs','Test OLEDs','/static/test_images/test-product-bar-image.jpeg'),(2,'TFTs','Test TFTs','/static/test_images/test-product-bar-image.jpeg'),(3,'Monochrome','Test Monochrome','/static/test_images/test-product-bar-image.jpeg'),(4,'Touch Panels','Test Touch Panels','/static/test_images/test-product-bar-image.jpeg'),(5,'Low Power','Test Low Power','/static/test_images/test-product-bar-image.jpeg');
/*!40000 ALTER TABLE `products_technology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_tftif`
--

DROP TABLE IF EXISTS `products_tftif`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_tftif` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_tftif`
--

LOCK TABLES `products_tftif` WRITE;
/*!40000 ALTER TABLE `products_tftif` DISABLE KEYS */;
INSERT INTO `products_tftif` VALUES (1,'24-bit RGB'),(2,'SPI/RGB'),(3,'8 bit CPU');
/*!40000 ALTER TABLE `products_tftif` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_tftproduct`
--

DROP TABLE IF EXISTS `products_tftproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_tftproduct` (
  `product_ptr_id` int(11) NOT NULL,
  `colour` tinyint(1) NOT NULL,
  `resolution` varchar(12) NOT NULL,
  `brightness` int(11) NOT NULL,
  `viewing_angle` varchar(15) NOT NULL,
  `tft_i_f_id` int(11) NOT NULL,
  `touch_id` int(11),
  PRIMARY KEY (`product_ptr_id`),
  KEY `products_tftproduct_tft_i_f_id_2a7318d1_fk_products_tftif_id` (`tft_i_f_id`),
  KEY `products_tftproduct_656db455` (`touch_id`),
  CONSTRAINT `products_tftprodu_product_ptr_id_b07cb729_fk_products_product_id` FOREIGN KEY (`product_ptr_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_tftproduct_tft_i_f_id_2a7318d1_fk_products_tftif_id` FOREIGN KEY (`tft_i_f_id`) REFERENCES `products_tftif` (`id`),
  CONSTRAINT `products_tftproduct_touch_id_f148d5c3_fk_products_touch_id` FOREIGN KEY (`touch_id`) REFERENCES `products_touch` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_tftproduct`
--

LOCK TABLES `products_tftproduct` WRITE;
/*!40000 ALTER TABLE `products_tftproduct` DISABLE KEYS */;
INSERT INTO `products_tftproduct` VALUES (1,1,'191x948',895,'19/77/75/1',1,NULL),(2,1,'370x493',713,'68/12/21/75',2,2),(3,1,'158x3',994,'24/70/36/21',3,1),(4,1,'268x518',46,'66/23/88/50',3,NULL),(5,1,'45x893',681,'98/84/80/16',2,2),(6,1,'230x19',407,'88/26/44/53',2,2),(7,0,'211x203',985,'22/70/29/1',2,1),(8,1,'431x296',594,'95/7/81/44',1,NULL),(9,1,'397x626',554,'51/54/34/99',2,NULL),(10,0,'197x170',895,'63/92/96/38',3,2),(11,0,'192x76',320,'47/71/86/49',1,1),(12,1,'281x41',921,'55/26/66/10',1,NULL),(13,1,'203x411',352,'23/55/75/87',2,NULL),(14,1,'164x630',351,'68/20/24/7',3,NULL),(15,1,'94x763',746,'94/38/53/47',1,NULL),(16,1,'253x756',783,'62/0/93/36',2,NULL),(17,1,'108x931',59,'81/26/65/8',3,NULL),(18,0,'454x454',68,'64/13/27/97',1,2),(19,1,'395x475',123,'65/22/80/79',1,1),(20,0,'45x232',265,'81/3/26/69',2,NULL),(21,0,'453x762',56,'89/82/77/30',3,NULL),(22,1,'363x323',547,'50/81/92/50',2,NULL),(23,1,'423x431',929,'10/27/72/61',2,NULL);
/*!40000 ALTER TABLE `products_tftproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_tftproduct_features`
--

DROP TABLE IF EXISTS `products_tftproduct_features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_tftproduct_features` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tftproduct_id` int(11) NOT NULL,
  `feature_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_tftproduct_features_tftproduct_id_203ed18f_uniq` (`tftproduct_id`,`feature_id`),
  KEY `products_tftproduct_f_feature_id_d026c465_fk_products_feature_id` (`feature_id`),
  CONSTRAINT `pro_tftproduct_id_1c41345e_fk_products_tftproduct_product_ptr_id` FOREIGN KEY (`tftproduct_id`) REFERENCES `products_tftproduct` (`product_ptr_id`),
  CONSTRAINT `products_tftproduct_f_feature_id_d026c465_fk_products_feature_id` FOREIGN KEY (`feature_id`) REFERENCES `products_feature` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_tftproduct_features`
--

LOCK TABLES `products_tftproduct_features` WRITE;
/*!40000 ALTER TABLE `products_tftproduct_features` DISABLE KEYS */;
INSERT INTO `products_tftproduct_features` VALUES (1,1,2),(2,2,1),(3,3,4),(4,4,5),(5,5,6),(6,6,4),(7,7,3),(8,8,6),(9,9,2),(10,10,5),(11,11,2),(12,12,3),(13,13,2),(14,14,1),(15,15,4),(16,16,4),(17,17,4),(18,18,2),(19,19,7),(20,20,6),(21,21,1),(22,22,1),(23,23,3);
/*!40000 ALTER TABLE `products_tftproduct_features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_touch`
--

DROP TABLE IF EXISTS `products_touch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_touch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(128) NOT NULL,
  `i_f` varchar(32) DEFAULT NULL,
  `points` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_touch`
--

LOCK TABLES `products_touch` WRITE;
/*!40000 ALTER TABLE `products_touch` DISABLE KEYS */;
INSERT INTO `products_touch` VALUES (1,'4WR','-',1),(2,'PCT','I2C',2);
/*!40000 ALTER TABLE `products_touch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_touchpanelproduct`
--

DROP TABLE IF EXISTS `products_touchpanelproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_touchpanelproduct` (
  `product_ptr_id` int(11) NOT NULL,
  `active_area_w` decimal(6,2) NOT NULL,
  `active_area_h` decimal(6,2) NOT NULL,
  `touch_points` smallint(6) NOT NULL,
  `controller_id` int(11) NOT NULL,
  `interface_id` int(11) NOT NULL,
  `structure_id` int(11) NOT NULL,
  PRIMARY KEY (`product_ptr_id`),
  KEY `products_touchp_controller_id_2c01c660_fk_products_controller_id` (`controller_id`),
  KEY `products_touchpan_interface_id_e0f3b79d_fk_products_interface_id` (`interface_id`),
  KEY `products_touchpan_structure_id_cf1aeaf3_fk_products_structure_id` (`structure_id`),
  CONSTRAINT `products_touchp_controller_id_2c01c660_fk_products_controller_id` FOREIGN KEY (`controller_id`) REFERENCES `products_controller` (`id`),
  CONSTRAINT `products_touchpan_interface_id_e0f3b79d_fk_products_interface_id` FOREIGN KEY (`interface_id`) REFERENCES `products_interface` (`id`),
  CONSTRAINT `products_touchpan_product_ptr_id_e36aba24_fk_products_product_id` FOREIGN KEY (`product_ptr_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_touchpan_structure_id_cf1aeaf3_fk_products_structure_id` FOREIGN KEY (`structure_id`) REFERENCES `products_structure` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_touchpanelproduct`
--

LOCK TABLES `products_touchpanelproduct` WRITE;
/*!40000 ALTER TABLE `products_touchpanelproduct` DISABLE KEYS */;
INSERT INTO `products_touchpanelproduct` VALUES (24,31.57,86.19,9,1,1,1),(25,69.25,99.15,8,1,1,1),(26,1.60,62.10,8,1,1,1),(27,9.73,44.20,10,1,1,1),(28,76.30,60.34,4,1,1,1),(29,60.60,10.58,4,1,1,1),(30,65.10,73.71,3,1,1,1),(31,82.68,53.97,15,1,1,1),(32,43.37,34.21,15,1,1,1),(33,3.13,4.66,7,1,1,1),(34,80.43,94.50,4,1,1,1),(35,75.69,80.59,3,1,1,1),(36,18.40,15.71,2,1,1,1),(37,45.56,27.72,13,1,1,1),(38,6.20,49.66,9,1,1,1),(39,96.53,87.13,3,1,1,1),(40,57.77,74.98,2,1,1,1),(41,43.50,72.55,7,1,1,1),(42,21.22,35.29,10,1,1,1),(43,22.17,15.96,4,1,1,1);
/*!40000 ALTER TABLE `products_touchpanelproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_touchpanelproduct_supported_os`
--

DROP TABLE IF EXISTS `products_touchpanelproduct_supported_os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_touchpanelproduct_supported_os` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `touchpanelproduct_id` int(11) NOT NULL,
  `os_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `products_touchpanelproduct_su_touchpanelproduct_id_f282be67_uniq` (`touchpanelproduct_id`,`os_id`),
  KEY `products_touchpanelproduct_supp_os_id_5c867ec8_fk_products_os_id` (`os_id`),
  CONSTRAINT `f02c505fcb87fe0ff316a01a1b1458a0` FOREIGN KEY (`touchpanelproduct_id`) REFERENCES `products_touchpanelproduct` (`product_ptr_id`),
  CONSTRAINT `products_touchpanelproduct_supp_os_id_5c867ec8_fk_products_os_id` FOREIGN KEY (`os_id`) REFERENCES `products_os` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_touchpanelproduct_supported_os`
--

LOCK TABLES `products_touchpanelproduct_supported_os` WRITE;
/*!40000 ALTER TABLE `products_touchpanelproduct_supported_os` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_touchpanelproduct_supported_os` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-28 13:00:32
