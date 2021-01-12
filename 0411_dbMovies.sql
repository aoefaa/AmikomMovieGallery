-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Waktu pembuatan: 12 Jan 2021 pada 14.09
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `0411_dbMovies`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `movies`
--

CREATE TABLE `movies` (
  `id` int(11) NOT NULL,
  `title` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `genre` varchar(50) CHARACTER SET latin1 NOT NULL,
  `image` varchar(15) CHARACTER SET latin1 DEFAULT NULL,
  `poster` varchar(15) CHARACTER SET latin1 COLLATE latin1_spanish_ci DEFAULT NULL,
  `resume` text CHARACTER SET latin1 DEFAULT NULL,
  `rating` float NOT NULL,
  `length` int(11) NOT NULL,
  `premiere` date DEFAULT NULL,
  `directors` varchar(50) NOT NULL,
  `writers` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `stars` varchar(50) CHARACTER SET latin1 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `movies`
--

INSERT INTO `movies` (`id`, `title`, `genre`, `image`, `poster`, `resume`, `rating`, `length`, `premiere`, `directors`, `writers`, `stars`) VALUES
(1, 'Ajisaka: The King and The Flower of Life', 'Animation, Action, Comedy', '1-big.jpg', '1-small.jpg', 'A sacred kid fulfills an old prophecy by fighting against an immortal evil king who rules the world by absorbing magic flowers energy.', 80, 98, '2021-01-13', 'Aryanto Yuniawan', 'M. Suyanto ', '-'),
(2, 'November 10th, Battle of Surabaya', ' Animation, Action, Adventure ', '2-big.jpg', '2-small.jpg', 'Musa, a thirteen-year-old shoe shiner, with Yumna, undergoes destiny through their adventure of waging war during the war time. Will they manage to bring peace among the troops keeping on fighting for nothing?', 72, 100, '2015-08-20', 'Aryanto Yuniawan', 'M. Suyanto, Aryanto Yuniawan', 'Reza Rahadian Keagan Kang Maudy Ayunda'),
(3, 'Petualangan Abdan', 'Animation, Drama', NULL, NULL, 'Petualangan Abdan bercerita tentang anak kecil berumur 4 tahun yang ceria lucu dan sedikit nakal. Abdan tinggal bersama neneknya karena tidak adanya ibu dan ayahnya dan Abdan selalu bertanya kenapa kedua orang tuanya\r\nmeninggalkannya', 77, 74, NULL, 'M. Suyanto', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `0411_dbMovies`
--
ALTER TABLE `movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
