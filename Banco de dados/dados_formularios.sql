-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dados_formularios
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dados`
--

DROP TABLE IF EXISTS `dados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dados` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cliente` varchar(455) DEFAULT NULL,
  `sip` varchar(150) DEFAULT NULL,
  `ddr` varchar(150) DEFAULT NULL,
  `lp` varchar(150) DEFAULT NULL,
  `atposx` varchar(150) DEFAULT NULL,
  `cabo` varchar(150) DEFAULT NULL,
  `fibras` varchar(150) DEFAULT NULL,
  `enlace` varchar(50) DEFAULT NULL,
  `porta` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dados`
--

LOCK TABLES `dados` WRITE;
/*!40000 ALTER TABLE `dados` DISABLE KEYS */;
INSERT INTO `dados` VALUES (1,'QUIMIS APARELHOS CIENTIFICOS LIMITADA','nan','nan','111854091030890.0',' 0827/18','5','55/56','3649','nan'),(2,'ESTORIL DISTRIBUIDORA DE VEICULOS LTDA','nan','115923229180053.0','nan','7178/24 ','A008','33/34','1334','nan'),(3,'FUST','nan','nan','111823361108390.0','B703/24','A006','33/34','7500','nan'),(4,'ARCOS DOURADOS COMERCIO DE ALIMENTOS AS','nan','nan','110005686362593.0','Manobrado','3','69/70','3081','nan'),(5,'SINDICATO DOS PETROLEIROS DO LITORAL PAULISTA','nan','115923202110054.0','nan','3377/24','A008','15/16','2663','nan'),(6,'RAIA DROGASIL SA','nan','nan','113863448019691.0','4897/24','A004','17/18','1470','nan'),(7,'CEMA HOSPITAL ESPECIALIZADO LIMITADA','nan','nan','116334990165390.0','OSX-01923175','2','31/32','2100','nan'),(8,'LOJAS RIACHUELO SA','nan','nan','110005058031099.0','6252/24','1','19/20','2901','nan'),(9,'PERTO S/A PERIFÉRICOS PARA AUTOMAÇÃO','nan','nan','110002954013497.0','0942/25','4','55/56','?','nan'),(10,'PEREZ DE REZENDE - ADVOGADOS','7529675.0','nan','nan','OSX-01893152','9','75/76','?','nan'),(11,'TELEFONICA BRASIL SA','nan','nan','110002671161797.0','3210/23','ANEL 213','69/70','4762','nan'),(12,'GRUPO CASAS BAHIA S.A.','nan','nan','118922304500194.0','B830/24','A#293','67/68','445','nan'),(13,'COMPANHIA DE SANEAMENTO BASICO DO ESTADO DE SAO PAULO','nan','nan','118704823906298.0','2863/24','3','11 e 12','404','nan'),(14,'SIMPAR AS','','nan','113814722300196.0','0204/25','A#001','77/78','3331',''),(18,'Q','Q','Q','QQ','Q','Q','Q','Q','Q');
/*!40000 ALTER TABLE `dados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `permissao` enum('admin','user') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Maria Oliveira','maria','senha123','admin','2025-06-11 14:15:52'),(2,'Jose','jose123','12345','user','2025-06-11 14:47:22'),(3,'teste','teste','12345','user','2025-06-11 14:50:34'),(4,'testeadmin','testeadmin','teste1234','admin','2025-06-11 16:53:47'),(5,'Admin','Admin','admin1234','admin','2025-06-16 18:31:11'),(6,'User','User','user1234','user','2025-06-16 18:31:34');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-17 13:35:05
