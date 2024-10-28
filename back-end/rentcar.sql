-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: rentcar
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carros`
--

DROP TABLE IF EXISTS `carros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carros` (
  `car_id` int NOT NULL AUTO_INCREMENT,
  `marca_id` int DEFAULT NULL,
  `precioxdia` decimal(10,2) NOT NULL,
  `fecha_auto` timestamp NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`car_id`),
  KEY `marca_id` (`marca_id`),
  CONSTRAINT `carros_ibfk_1` FOREIGN KEY (`marca_id`) REFERENCES `marcas` (`marca_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carros`
--

LOCK TABLES `carros` WRITE;
/*!40000 ALTER TABLE `carros` DISABLE KEYS */;
INSERT INTO `carros` VALUES (1,1,50.00,'2024-10-10 15:20:02',_binary '','2024-10-19 18:40:54',NULL);
/*!40000 ALTER TABLE `carros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `cliente_id` int NOT NULL AUTO_INCREMENT,
  `documento_id` int DEFAULT NULL,
  `cedula` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `celular` varchar(11) NOT NULL,
  `reserva_id` int DEFAULT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`cliente_id`),
  UNIQUE KEY `cedula` (`cedula`),
  UNIQUE KEY `cedula_2` (`cedula`),
  KEY `documento_id` (`documento_id`),
  KEY `reserva_id` (`reserva_id`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`documento_id`) REFERENCES `tipo_documento` (`documento_id`),
  CONSTRAINT `clientes_ibfk_2` FOREIGN KEY (`reserva_id`) REFERENCES `reservas` (`reserva_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,1,'1143224873','PEDRO','PERES','PPEREZ@GMAIL.COM','3007482216',1,_binary '','2024-10-19 18:57:46',NULL);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial`
--

DROP TABLE IF EXISTS `historial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial` (
  `historial_id` int NOT NULL AUTO_INCREMENT,
  `reserva_id` int DEFAULT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`historial_id`),
  KEY `reserva_id` (`reserva_id`),
  CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`reserva_id`) REFERENCES `reservas` (`reserva_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial`
--

LOCK TABLES `historial` WRITE;
/*!40000 ALTER TABLE `historial` DISABLE KEYS */;
/*!40000 ALTER TABLE `historial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas`
--

DROP TABLE IF EXISTS `marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marcas` (
  `marca_id` int NOT NULL AUTO_INCREMENT,
  `modelo_id` int DEFAULT NULL,
  `marca` varchar(50) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`marca_id`),
  KEY `modelo_id` (`modelo_id`),
  CONSTRAINT `marcas_ibfk_1` FOREIGN KEY (`modelo_id`) REFERENCES `modelos` (`modelo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas`
--

LOCK TABLES `marcas` WRITE;
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` VALUES (1,NULL,'CHEVROLET',_binary '','2024-10-19 18:36:12',NULL);
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelos`
--

DROP TABLE IF EXISTS `modelos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelos` (
  `modelo_id` int NOT NULL AUTO_INCREMENT,
  `modelo` varchar(50) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`modelo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelos`
--

LOCK TABLES `modelos` WRITE;
/*!40000 ALTER TABLE `modelos` DISABLE KEYS */;
INSERT INTO `modelos` VALUES (1,'CAMARO',_binary '','2024-10-19 18:35:13',NULL);
/*!40000 ALTER TABLE `modelos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos` (
  `pago_id` int NOT NULL AUTO_INCREMENT,
  `reserva_id` int DEFAULT NULL,
  `fecha_pago` timestamp NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`pago_id`),
  KEY `reserva_id` (`reserva_id`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`reserva_id`) REFERENCES `reservas` (`reserva_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservas` (
  `reserva_id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int DEFAULT NULL,
  `car_id` int DEFAULT NULL,
  `fecha_reserva` date NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_final` date NOT NULL,
  `valor_reserva` decimal(10,2) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`reserva_id`),
  KEY `user_id` (`usuario_id`),
  KEY `car_id` (`car_id`),
  CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `reservas_ibfk_2` FOREIGN KEY (`car_id`) REFERENCES `carros` (`car_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
INSERT INTO `reservas` VALUES (1,1,1,'2024-10-10','2024-10-10','2024-10-30',50000.00,_binary '','2024-10-19 18:56:03',NULL);
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `rol_id` int NOT NULL AUTO_INCREMENT,
  `rol_name` varchar(50) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`rol_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin',_binary '','2024-10-08 21:36:43',NULL),(2,'patio1',_binary '','2024-10-08 21:36:43',NULL),(3,'patio2',_binary '','2024-10-08 21:36:43',NULL),(4,'contabilidad',_binary '','2024-10-08 21:36:43',NULL);
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_documento`
--

DROP TABLE IF EXISTS `tipo_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_documento` (
  `documento_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `sigla` varchar(50) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`documento_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_documento`
--

LOCK TABLES `tipo_documento` WRITE;
/*!40000 ALTER TABLE `tipo_documento` DISABLE KEYS */;
INSERT INTO `tipo_documento` VALUES (1,'Cedula de ciudadania','CC',_binary '','2024-10-08 21:39:08',NULL),(2,'Cedula de extranjeria','CE',_binary '','2024-10-08 21:39:08',NULL),(3,'NIT','NIT',_binary '','2024-10-08 21:39:08',NULL);
/*!40000 ALTER TABLE `tipo_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `rol_id` int DEFAULT NULL,
  `documento_id` int DEFAULT NULL,
  `cedula` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  `celular` varchar(11) NOT NULL,
  `estado_rg` bit(1) DEFAULT b'1',
  `fecha_rg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_md` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  UNIQUE KEY `cedula` (`cedula`),
  UNIQUE KEY `cedula_2` (`cedula`),
  KEY `rol_id` (`rol_id`),
  KEY `documento_id` (`documento_id`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`rol_id`),
  CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`documento_id`) REFERENCES `tipo_documento` (`documento_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,1,1,'2222','aaaa','bbbbb','H@TEST','H123','8888888',_binary '','2024-10-10 15:20:02','2024-10-18 16:08:29');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'rentcar'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-19 14:27:56
