-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2020 at 01:54 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `upload`
--

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `id` int(11) NOT NULL,
  `filename` text NOT NULL,
  `path` text NOT NULL,
  `counter` int(11) NOT NULL,
  `created` date NOT NULL,
  `last` date NOT NULL,
  `generated_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`id`, `filename`, `path`, `counter`, `created`, `last`, `generated_name`) VALUES
(59, '1.png', 'images/1/', 1, '2020-01-13', '2020-01-13', '96984664.png'),
(60, '1.png', 'images/1/', 1, '2020-01-13', '2020-01-13', '57423941.png'),
(61, '1.png', 'images/3/', 1, '2020-01-13', '2020-01-13', '42841543.png');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`role_id`, `name`) VALUES
(1, 'admin'),
(2, 'user');

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` int(11) NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`session_id`, `data`) VALUES
(39, '{\"user_id\": 25}'),
(40, '{\"user_id\": 26}'),
(41, '{\"user_id\": 27}'),
(42, '{\"user_id\": 28}');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` binary(64) NOT NULL,
  `email` text NOT NULL,
  `secret_question` text NOT NULL,
  `secret_answer` binary(64) NOT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `secret_question`, `secret_answer`, `role_id`) VALUES
(25, 'b', 0x1d69a5e379b3528d05cd9536653819d9384ac627c255dbdee9df79fdeb5d1a9832daf4ce0b457517d413f1d73000b83437405f4ccba2475f915e0d7cf4ddd403, 'b@gmail.com', 'What is your childhood friends name?', 0xe5867f2955b6cc134b4d359481f3dbdbdf9c2dfb67575b270d134c40945c46bc22a816222e1a7b3eb4663ce437bcbeb06f9cda901c46c419073d18fdd888cc0e, NULL),
(26, 'bla', 0x548da1fdd2663f87038ec44ec866e9deed462e64fefd734d141e9b22dee88e72a7bfe8cf643c9d7c2e5adfdcfad92ce49038adf48c3a10974c5bde49884b5319, 'bla@gmail.com', 'What is your childhood friends name?', 0xd3f914186ae5fd21591d8dc76b0483a2692d731fa309e6bd84a4c2b0e443a589a75f7af8441fe772e7034aea4d16110f729f7f162d4121cdf2fadf781df29a7b, 2),
(27, 'ivan', 0x57e9fd52269db6c15d98dc02fb155316ce6c39a9e95fc4fd82b61265ab2701dbaaf05cc721187a25c720a68e768c0fb2340356c5646ed3f11d2a9e9b77071042, 'ivan@gmail.com', 'What is your childhood friends name?', 0x0fcb4d93e9ab3417a2aeb6d547525707a9199d4e26e818d4938b68886be92f3b514779d4c2c6f90cbbdf15adb66589a74a6f7d4de2ae3488aeb56a9fa66a3258, NULL),
(28, 'ivanb', 0xdd22bb48017a458aaacaec9bebecc6ccd59d03af859037a7766337a7a8f834893ed4d61e4063ab5ab5b1ae0d24a9ca1674b3b277de7f5401cee0a83570e33464, 'bb@gmail.com', 'What is your childhood friends name?', 0x338b91857df7d999e28cb7dadfeba8354fce695308be2092289c1968d60f11bade53c479e88e42e173f3e100a45df91c5cf7cad9e1e54a79ee540b5d4d2183b7, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `image`
--
ALTER TABLE `image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
