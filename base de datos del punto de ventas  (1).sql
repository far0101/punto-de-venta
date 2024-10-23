CREATE TABLE `Productos` (
  `id` integer PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` integer NOT NULL
);

CREATE TABLE `Clientes` (
  `id` integer PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `gmail` varchar(255)
);

CREATE TABLE `Ventas` (
  `id` integer PRIMARY KEY,
  `id_cliente` integer,
  `fecha` datetime NOT NULL,
  `total` decimal(10,2) NOT NULL
);

CREATE TABLE `Detalles_Ventas` (
  `id` integer PRIMARY KEY,
  `id_venta` integer,
  `id_producto` integer,
  `cantidad` integer NOT NULL,
  `precio` decimal(10,2) NOT NULL
);

ALTER TABLE `Ventas` ADD FOREIGN KEY (`id_cliente`) REFERENCES `Clientes` (`id`);

ALTER TABLE `Detalles_Ventas` ADD FOREIGN KEY (`id_venta`) REFERENCES `Ventas` (`id`);

ALTER TABLE `Detalles_Ventas` ADD FOREIGN KEY (`id_producto`) REFERENCES `Productos` (`id`);
