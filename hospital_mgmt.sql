-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 05, 2023 at 01:06 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hospital_mgmt`
--

-- --------------------------------------------------------

--
-- Table structure for table `ho_admin`
--

CREATE TABLE `ho_admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `latitude` varchar(20) NOT NULL,
  `longitude` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_admin`
--

INSERT INTO `ho_admin` (`username`, `password`, `latitude`, `longitude`) VALUES
('admin', 'admin', '10.999375	', '77.084344');

-- --------------------------------------------------------

--
-- Table structure for table `ho_ambulance`
--

CREATE TABLE `ho_ambulance` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `hospital` varchar(20) NOT NULL,
  `ambno` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `latitude` varchar(20) NOT NULL,
  `longitude` varchar(20) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_ambulance`
--

INSERT INTO `ho_ambulance` (`id`, `name`, `hospital`, `ambno`, `mobile`, `latitude`, `longitude`, `status`) VALUES
(1, 'Ramesh', 'apollo', '1101', 9612565484, '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ho_appoint`
--

CREATE TABLE `ho_appoint` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `hospital` varchar(20) NOT NULL,
  `doctor_id` varchar(20) NOT NULL,
  `ap_date` varchar(20) NOT NULL,
  `ap_time` varchar(20) NOT NULL,
  `details` varchar(100) NOT NULL,
  `book_date` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_appoint`
--

INSERT INTO `ho_appoint` (`id`, `uname`, `hospital`, `doctor_id`, `ap_date`, `ap_time`, `details`, `book_date`) VALUES
(1, 'mohan', 'apollo', 'D1', '01/23/2023', '11:30 AM', 'Back Pain', '22-01-2023');

-- --------------------------------------------------------

--
-- Table structure for table `ho_doctor`
--

CREATE TABLE `ho_doctor` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `hospital` varchar(30) NOT NULL,
  `speciality` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `av_time` varchar(30) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_doctor`
--

INSERT INTO `ho_doctor` (`id`, `name`, `hospital`, `speciality`, `mobile`, `email`, `av_time`, `uname`, `pass`, `rdate`, `status`) VALUES
(1, 'Dr. S. Divahar M.S', 'apollo', 'Orthopedic Surgeon (Bone)', 8956564121, 'divahar.apollo@gmail.com', '10am to 5pm', 'D1', '12345', '03-01-2023', 0),
(2, 'Dr. Krishnan MBBS, MS', 'sengs', 'Cardiology (Heart)', 7995945456, 'krishnan@gmail.com', '10am to 5pm', 'D2', '12345', '03-01-2023', 0),
(3, 'Santhosh', 'apollo', 'ddd', 8526974552, 'santhosh@gmail.com', '10-5', 'D3', '123456', '31-03-2023', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ho_emergency`
--

CREATE TABLE `ho_emergency` (
  `id` int(11) NOT NULL,
  `hospital` varchar(20) NOT NULL,
  `details` varchar(100) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `dtime` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_emergency`
--

INSERT INTO `ho_emergency` (`id`, `hospital`, `details`, `rdate`, `status`, `dtime`) VALUES
(1, 'rkv', 'elder person, heart attack', '09-01-2023', 1, '2023-01-09 17:15:57');

-- --------------------------------------------------------

--
-- Table structure for table `ho_hospital`
--

CREATE TABLE `ho_hospital` (
  `id` int(11) NOT NULL,
  `hospital` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(30) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `latitude` varchar(20) NOT NULL,
  `longitude` varchar(20) NOT NULL,
  `speciality` varchar(200) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_hospital`
--

INSERT INTO `ho_hospital` (`id`, `hospital`, `address`, `city`, `mobile`, `email`, `latitude`, `longitude`, `speciality`, `uname`, `pass`, `rdate`, `status`) VALUES
(1, 'Apollo', 'Chennai Bypass Road Ariyamangalam Area, Old Palpan', 'Trichy', 9723015655, 'apollo@gmail.com', '10.807032', '78.71113', 'cancer, knee replacements, liver transplant, heart, general treatments', 'apollo', '123456', '03-01-2023', 1),
(2, 'KMC', 'No.1, K.C.Road, Tennur', 'Trichy', 7995945456, 'kmc@gmail.com', '10.816845', '78.680995', 'cancer, knee replacements, liver transplant, heart, general treatments', 'kmc', '123456', '03-01-2023', 0),
(3, 'RKV Hospital', 'Udumalaipet Road, X3RP+V8V, Rajiv Gandhi Nagar, Pa', 'Coimbatore', 6321544545, 'rkvcare@gmail.com', '10.992231', '77.085786', 'Kidney Treatment, Fertility Hospitals, child treatments', 'rkv', '123456', '05-01-2023', 0),
(4, 'Coimbatore Medical College Hos', 'No.1619 A, Trichy Rd, Gopalapuram', 'Coimbatore', 9825498455, 'cmc@gmail.com', '10.995437', '76.970276', 'general treatments', 'cmc', '123456', '05-01-2023', 0),
(5, 'NG Hospital & Research Centre', '577, Trichy Rd, Near B-5 Police Station, Agraharam', 'Coimbatore', 8865485642, 'nghospital@gmail.com', '11.000408', '77.02929', 'General Treatments', 'ng', '123456', '05-01-2023', 0),
(6, 'Sengs ENT Care', '24GC+6Q8, Nagapattinam - Coimbatore - Gundlupet Hw', 'Coimbatore', 7354987512, 'sengs@gmail.com', '11.025531', '77.121942', 'ENT treatments', 'sengs', '123456', '05-01-2023', 0),
(7, 'Vasan Eye Hospital', 'No. 81/83, West Thiruvenkatasamy Road, 80-92, W TV', 'Coimbatore', 8814843212, 'vasan@gmail.com', '11.009138', '76.945452', 'Eye care, eye treatments, eye hospitals', 'vasan', '123456', '05-01-2023', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ho_user`
--

CREATE TABLE `ho_user` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(50) NOT NULL,
  `parent_mobile` bigint(20) NOT NULL,
  `aadhar` varchar(20) NOT NULL,
  `blood_grp` varchar(20) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `latitude` varchar(20) NOT NULL,
  `longitude` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  UNIQUE KEY `aadhar` (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_user`
--

INSERT INTO `ho_user` (`id`, `name`, `gender`, `dob`, `mobile`, `email`, `address`, `parent_mobile`, `aadhar`, `blood_grp`, `filename`, `latitude`, `longitude`, `uname`, `pass`, `rdate`) VALUES
(2, 'Dharun', 'Male', '1998-07-05', 9874563214, 'dharun@gmail.com', 'DD', 8956322554, '258933665422', 'A+ve', '', '', '', 'dharun', '1234', '31-03-2023'),
(1, 'Mohan', 'Male', '1975-08-14', 9895548941, 'mohan@gmail.com', '45,FG, Salem', 8954654512, '564532312154', '', '', '10.836323', '78.689367', 'mohan', '123456', '03-01-2023');
