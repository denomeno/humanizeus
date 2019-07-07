-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2019 at 07:32 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homeless_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `name` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`category_id`, `name`) VALUES
(1, 'Living Room'),
(2, 'Bedroom'),
(3, 'Kitchen'),
(4, 'Toiletry'),
(5, 'Clothing'),
(6, 'Education');

-- --------------------------------------------------------

--
-- Table structure for table `categories_have_items`
--

CREATE TABLE `categories_have_items` (
  `item_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `categories_have_items`
--

INSERT INTO `categories_have_items` (`item_id`, `category_id`) VALUES
(1, 1),
(2, 2),
(4, 3),
(3, 4),
(5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `entities`
--

CREATE TABLE `entities` (
  `entity_id` int(11) NOT NULL,
  `email` varchar(44) NOT NULL,
  `name` varchar(44) NOT NULL,
  `address` varchar(44) NOT NULL,
  `phone` varchar(44) NOT NULL,
  `website` varchar(44) NOT NULL,
  `latitude` varchar(44) NOT NULL,
  `longitude` varchar(44) NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `entities`
--

INSERT INTO `entities` (`entity_id`, `email`, `name`, `address`, `phone`, `website`, `latitude`, `longitude`, `type_id`) VALUES
(1, 'hallikdeniz@gmail.com', 'Deniz', '1157 Commonwealth Ave', '8572729210', '', '', '', 1),
(2, 'fred@fred.com', 'Fred', '112 Southampton Street', '', '', '42.332315', '-71.0713258', 2),
(3, 'women@lunch.com', 'Women\'s Lunch Place', '70 Newburry', '', '', '42.352127', '-71.074181', 3),
(4, 'american@redcross.com', 'The American Red Cross  Food Pantry', '', '', '', '42.327107', '-71.067641', 3),
(5, 'boraytoktay@gmail.com', 'Boray', '132 Thomson Street', '', '', '', '', 2),
(16, 'fuck@gmail.com', 'Boray', 'dfbasd', '', '', '', '', 2),
(17, 'trial@gmail.com', 'Trial', 'Trial', '', '', '', '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `entities_need_items`
--

CREATE TABLE `entities_need_items` (
  `entities_need_items_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `quantity_requested` int(11) NOT NULL,
  `quantity_fulfilled` int(11) NOT NULL,
  `description` varchar(1028) NOT NULL,
  `continuous_need_status` varchar(3) NOT NULL COMMENT 'YES = continuously needed item',
  `show_on_map_status` varchar(3) NOT NULL COMMENT 'YES = show on map',
  `time_in_1` varchar(44) NOT NULL,
  `time_out_1` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `entities_need_items`
--

INSERT INTO `entities_need_items` (`entities_need_items_id`, `entity_id`, `item_id`, `quantity_requested`, `quantity_fulfilled`, `description`, `continuous_need_status`, `show_on_map_status`, `time_in_1`, `time_out_1`) VALUES
(1, 5, 1, 2, 0, '    Please', '', '', '', ''),
(2, 5, 3, 3, 0, '    Please', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `entities_supply_items`
--

CREATE TABLE `entities_supply_items` (
  `entities_supply_items_id` int(44) NOT NULL,
  `entity_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `description` varchar(1028) NOT NULL,
  `quantity_requested` int(11) NOT NULL,
  `quantity_fulfilled` int(11) NOT NULL,
  `continuous_supply_status` varchar(3) NOT NULL COMMENT 'YES = continuously supplied item',
  `fulfillment_status` varchar(3) NOT NULL COMMENT 'YES = fulfilled / NO = not fulfilled ',
  `time_in_1` varchar(44) NOT NULL,
  `time_out_1` varchar(44) NOT NULL,
  `time_in_2` varchar(44) NOT NULL,
  `time_out_2` varchar(44) NOT NULL,
  `time_in_3` varchar(44) NOT NULL,
  `time_out_3` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `entities_supply_items`
--

INSERT INTO `entities_supply_items` (`entities_supply_items_id`, `entity_id`, `item_id`, `description`, `quantity_requested`, `quantity_fulfilled`, `continuous_supply_status`, `fulfillment_status`, `time_in_1`, `time_out_1`, `time_in_2`, `time_out_2`, `time_in_3`, `time_out_3`) VALUES
(0, 1, 4, '', 0, 0, '', '', '12:00 PM 5/10/2019', '01:00 PM 5/10/2019', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `entity_types`
--

CREATE TABLE `entity_types` (
  `type_id` int(11) NOT NULL,
  `description` varchar(44) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `entity_types`
--

INSERT INTO `entity_types` (`type_id`, `description`) VALUES
(1, 'Donor'),
(2, 'In Need'),
(3, 'Organization');

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `item_id` int(11) NOT NULL,
  `name` varchar(44) NOT NULL,
  `description` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`item_id`, `name`, `description`) VALUES
(1, 'Chair', ''),
(2, 'Bed', ''),
(3, 'Shower curtain', ''),
(4, 'Plates', ''),
(5, 'Sweater ', ''),
(6, 'Bags', '');

-- --------------------------------------------------------

--
-- Table structure for table `matches`
--

CREATE TABLE `matches` (
  `match_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `supplier_entity_id` int(11) NOT NULL,
  `receiver_entity_id` int(11) NOT NULL,
  `fulfillment_status` varchar(3) NOT NULL COMMENT 'YES = fulfilled / NO = not fulfilled '
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `categories_have_items`
--
ALTER TABLE `categories_have_items`
  ADD KEY `category_id_link` (`category_id`),
  ADD KEY `item_id_link` (`item_id`);

--
-- Indexes for table `entities`
--
ALTER TABLE `entities`
  ADD PRIMARY KEY (`entity_id`),
  ADD UNIQUE KEY `uniqe_email` (`email`),
  ADD KEY `type_id_link` (`type_id`);

--
-- Indexes for table `entities_need_items`
--
ALTER TABLE `entities_need_items`
  ADD PRIMARY KEY (`entities_need_items_id`) USING BTREE,
  ADD KEY `entity_id_link_2` (`entity_id`),
  ADD KEY `item_id_link_2` (`item_id`);

--
-- Indexes for table `entities_supply_items`
--
ALTER TABLE `entities_supply_items`
  ADD PRIMARY KEY (`entities_supply_items_id`) USING BTREE,
  ADD KEY `item_id_link_supply` (`item_id`),
  ADD KEY `entity_id_link_supply` (`entity_id`);

--
-- Indexes for table `entity_types`
--
ALTER TABLE `entity_types`
  ADD PRIMARY KEY (`type_id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`item_id`);

--
-- Indexes for table `matches`
--
ALTER TABLE `matches`
  ADD PRIMARY KEY (`match_id`),
  ADD KEY `supplier_entity_id_link` (`supplier_entity_id`),
  ADD KEY `item_id_link_match` (`item_id`),
  ADD KEY `receiver_entity_id_link` (`receiver_entity_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `entities`
--
ALTER TABLE `entities`
  MODIFY `entity_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `entities_need_items`
--
ALTER TABLE `entities_need_items`
  MODIFY `entities_need_items_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `entity_types`
--
ALTER TABLE `entity_types`
  MODIFY `type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `matches`
--
ALTER TABLE `matches`
  MODIFY `match_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `categories_have_items`
--
ALTER TABLE `categories_have_items`
  ADD CONSTRAINT `category_id_link` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_id_link` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `entities`
--
ALTER TABLE `entities`
  ADD CONSTRAINT `type_id_link` FOREIGN KEY (`type_id`) REFERENCES `entity_types` (`type_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `entities_need_items`
--
ALTER TABLE `entities_need_items`
  ADD CONSTRAINT `entity_id_link_2` FOREIGN KEY (`entity_id`) REFERENCES `entities` (`entity_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_id_link_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `entities_supply_items`
--
ALTER TABLE `entities_supply_items`
  ADD CONSTRAINT `entity_id_link_supply` FOREIGN KEY (`entity_id`) REFERENCES `entities` (`entity_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_id_link_supply` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `matches`
--
ALTER TABLE `matches`
  ADD CONSTRAINT `item_id_link_match` FOREIGN KEY (`item_id`) REFERENCES `items` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `receiver_entity_id_link` FOREIGN KEY (`receiver_entity_id`) REFERENCES `entities` (`entity_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `supplier_entity_id_link` FOREIGN KEY (`supplier_entity_id`) REFERENCES `entities` (`entity_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
