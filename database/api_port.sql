-- MySQL dump 10.13  Distrib 5.7.9, for linux-glibc2.5 (x86_64)
--
-- Host: localhost    Database: api_port
-- ------------------------------------------------------
-- Server version	5.7.9-log

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
-- Table structure for table `api_argv`
--

DROP TABLE IF EXISTS `api_argv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_argv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `api_id` int(11) NOT NULL COMMENT 'API接口ID',
  `name` varchar(255) DEFAULT NULL COMMENT 'API 参数名称',
  `desc` text COMMENT 'API参数描述',
  `necessary` tinyint(4) DEFAULT NULL COMMENT 'API参数必填与否',
  `status` tinyint(4) DEFAULT NULL COMMENT 'API当前状态，1=>有效，0=>已删除',
  `default` varchar(255) DEFAULT NULL COMMENT 'API调试时默认值',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_argv`
--

LOCK TABLES `api_argv` WRITE;
/*!40000 ALTER TABLE `api_argv` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_argv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_commit`
--

DROP TABLE IF EXISTS `api_commit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_commit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '修改API者ID',
  `project_id` int(11) NOT NULL COMMENT '所属API模块ID',
  `api_id` int(11) NOT NULL COMMENT '具体的API ID',
  `commit` text COMMENT '修改说明',
  `time` int(11) DEFAULT NULL COMMENT '提交时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_commit`
--

LOCK TABLES `api_commit` WRITE;
/*!40000 ALTER TABLE `api_commit` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_commit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_info`
--

DROP TABLE IF EXISTS `api_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT 'API 名称',
  `desc` text COMMENT 'API 说明',
  `return` text COMMENT 'API 返回值',
  `status` tinyint(4) DEFAULT NULL COMMENT 'API 当前状态 1=>正常，0=>已删除',
  `last` int(11) DEFAULT NULL COMMENT '上次更新的commit ID',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  `create_id` int(11) DEFAULT NULL COMMENT '创建者ID',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_info`
--

LOCK TABLES `api_info` WRITE;
/*!40000 ALTER TABLE `api_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_model`
--

DROP TABLE IF EXISTS `api_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT 'API 模块名',
  `head` varchar(255) DEFAULT NULL COMMENT 'API 模块头像',
  `desc` text COMMENT 'API 模块描述',
  `status` tinyint(4) DEFAULT NULL COMMENT 'API 模块状态 1=>正常，2=>已删除',
  `last` int(11) DEFAULT NULL COMMENT '上次更新的commit ID',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_model`
--

LOCK TABLES `api_model` WRITE;
/*!40000 ALTER TABLE `api_model` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_list`
--

DROP TABLE IF EXISTS `project_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '项目名',
  `head` varchar(255) DEFAULT NULL COMMENT '项目头像',
  `desc` text COMMENT '项目描述',
  `status` tinyint(4) DEFAULT NULL COMMENT '项目状态 1=>正常，0=>已删除',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_list`
--

LOCK TABLES `project_list` WRITE;
/*!40000 ALTER TABLE `project_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_model`
--

DROP TABLE IF EXISTS `project_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL COMMENT '项目ID',
  `name` varchar(255) DEFAULT NULL COMMENT '项目模块名',
  `desc` text COMMENT '项目模块说明',
  `status` tinyint(4) DEFAULT NULL COMMENT '项目模块状态，1=>正常，0=>已删除',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_model`
--

LOCK TABLES `project_model` WRITE;
/*!40000 ALTER TABLE `project_model` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_model_user_relation`
--

DROP TABLE IF EXISTS `project_model_user_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_model_user_relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_model_id` int(11) NOT NULL COMMENT '项目模块ID',
  `user_id` varchar(255) DEFAULT NULL COMMENT '用户ID',
  `status` tinyint(4) DEFAULT NULL COMMENT '当前状态，1=>正常，0=>已删除',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_model_user_relation`
--

LOCK TABLES `project_model_user_relation` WRITE;
/*!40000 ALTER TABLE `project_model_user_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_model_user_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '用户名',
  `head` varchar(255) DEFAULT NULL COMMENT '用户头像',
  `status` tinyint(4) DEFAULT NULL COMMENT '用户状态，1=>正常，0=>未登入，2=>已删除',
  `lasttime` int(11) DEFAULT NULL COMMENT '上次登入时间',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-12 16:15:50
