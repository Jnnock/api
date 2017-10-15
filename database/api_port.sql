/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50620
 Source Host           : localhost
 Source Database       : api_port

 Target Server Type    : MySQL
 Target Server Version : 50620
 File Encoding         : utf-8

 Date: 10/15/2017 21:47:00 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `api_argv`
-- ----------------------------
DROP TABLE IF EXISTS `api_argv`;
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

-- ----------------------------
--  Table structure for `api_commit`
-- ----------------------------
DROP TABLE IF EXISTS `api_commit`;
CREATE TABLE `api_commit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '修改API者ID',
  `project_id` int(11) NOT NULL COMMENT '所属API模块ID',
  `api_id` int(11) NOT NULL COMMENT '具体的API ID',
  `commit` text COMMENT '修改说明',
  `time` int(11) DEFAULT NULL COMMENT '提交时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `api_info`
-- ----------------------------
DROP TABLE IF EXISTS `api_info`;
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

-- ----------------------------
--  Table structure for `api_model`
-- ----------------------------
DROP TABLE IF EXISTS `api_model`;
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

-- ----------------------------
--  Table structure for `project_list`
-- ----------------------------
DROP TABLE IF EXISTS `project_list`;
CREATE TABLE `project_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '项目名',
  `head` varchar(255) DEFAULT NULL COMMENT '项目头像',
  `desc` text COMMENT '项目描述',
  `status` tinyint(4) DEFAULT NULL COMMENT '项目状态 1=>正常，0=>已删除',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `project_model`
-- ----------------------------
DROP TABLE IF EXISTS `project_model`;
CREATE TABLE `project_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL COMMENT '项目ID',
  `name` varchar(255) DEFAULT NULL COMMENT '项目模块名',
  `desc` text COMMENT '项目模块说明',
  `status` tinyint(4) DEFAULT NULL COMMENT '项目模块状态，1=>正常，0=>已删除',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `project_model_user_relation`
-- ----------------------------
DROP TABLE IF EXISTS `project_model_user_relation`;
CREATE TABLE `project_model_user_relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_model_id` int(11) NOT NULL COMMENT '项目模块ID',
  `user_id` varchar(255) DEFAULT NULL COMMENT '用户ID',
  `status` tinyint(4) DEFAULT NULL COMMENT '当前状态，1=>正常，0=>已删除',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `user_info`
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '用户名',
  `head` varchar(255) DEFAULT NULL COMMENT '用户头像',
  `status` tinyint(4) DEFAULT NULL COMMENT '用户状态，1=>正常，0=>未登入，2=>已删除',
  `lasttime` int(11) DEFAULT NULL COMMENT '上次登入时间',
  `time` int(11) DEFAULT NULL COMMENT '创建时间',
  `passwd` varchar(199) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
