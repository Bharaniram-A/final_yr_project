-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 12, 2025 at 04:18 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `appointment_scheduling`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `available_slots` text,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`id`, `name`, `available_slots`) VALUES
(1, 'Dr. A', '09:00,09:30,10:00,10:30,11:00,11:30'),
(2, 'Dr. B', '09:00,09:30,10:00,10:30,11:00,11:30');

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
(1, 'Dr. S. Divahar M.S', 'GH001', 'General Physician', 8956564121, 'divahar121@gmail.com', '10am to 5pm', 'D1', '12345', '03-01-2023', 0),
(2, 'Dr. Krishnan MBBS, MS', 'GH002', 'General Physician', 7995945456, 'krishnan45@gmail.com', '10am to 5pm', 'D2', '12345', '03-01-2023', 0),
(3, 'Dr. S.Vijay, MBBS', 'GH003', 'General Physician', 9654254885, 'vijay1214@gmail.com', '10am to 5pm', 'D3', '1234', '09-05-2025', 1);

-- --------------------------------------------------------

--
-- Table structure for table `ho_entry`
--

CREATE TABLE `ho_entry` (
  `id` int(11) NOT NULL,
  `patient_id` varchar(20) NOT NULL,
  `hospital` varchar(20) NOT NULL,
  `docid` varchar(20) NOT NULL,
  `doctor` varchar(20) NOT NULL,
  `token_no` int(11) NOT NULL,
  `reason` varchar(200) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `rtime` varchar(20) NOT NULL,
  `month` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `staff_id` varchar(20) NOT NULL,
  `entry_type` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `temp` double NOT NULL,
  `pulse` varchar(20) NOT NULL,
  `bp` varchar(20) NOT NULL,
  `height` double NOT NULL,
  `weight` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_entry`
--

INSERT INTO `ho_entry` (`id`, `patient_id`, `hospital`, `docid`, `doctor`, `token_no`, `reason`, `rdate`, `rtime`, `month`, `year`, `staff_id`, `entry_type`, `status`, `temp`, `pulse`, `bp`, `height`, `weight`) VALUES
(1, 'PT3', 'GH001', 'D1', 'Dr. S. Divahar M.S', 1, 'health checkup', '12-05-2025', '09:02', 5, 2025, 'S1', 'entry', 2, 99, '70', '125/85', 172, 76),
(2, 'PT2', 'GH001', 'D1', 'Dr. S. Divahar M.S', 2, 'Fever and cough', '12-05-2025', '09:09', 5, 2025, '', 'booked', 3, 98, '68', '123/84', 171, 75),
(3, 'PT4', 'GH001', 'D1', 'Dr. S. Divahar M.S', 3, 'Fever', '12-05-2025', '09:11', 5, 2025, 'S1', 'entry', 1, 98, '75', '129/89', 164, 80),
(4, 'PT5', 'GH001', 'D1', 'Dr. S. Divahar M.S', 4, 'Skin Allergy', '12-05-2025', '09:13', 5, 2025, 'S1', 'entry', 0, 97, '71', '121/81', 165, 78),
(5, 'PT6', 'GH001', 'D1', 'Dr. S. Divahar M.S', 5, 'Back pain', '12-05-2025', '09:14', 5, 2025, 'S1', 'entry', 0, 97, '79', '121/81', 169, 78),
(6, 'PT1', 'GH001', 'D1', 'Dr. S. Divahar M.S', 6, 'Fever', '12-05-2025', '09:15', 5, 2025, '', 'booked', 0, 98, '82', '122/81', 169, 75);

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
(1, 'GH-Ghandhi Hospital', 'Woraiyur', 'Trichy', 9723015655, 'gh001try@gmail.com', '10.807032', '78.71113', 'cancer, knee replacements, liver transplant, heart, general treatments', 'GH001', '123456', '03-03-2025', 1),
(2, 'GH-Periyar Hospital', 'Old Bus Stand', 'Thanjavur', 7995945456, 'gh002tnj@gmail.com', '10.816845', '78.680995', 'cancer, knee replacements, liver transplant, heart, general treatments', 'GH002', '123456', '03-03-2025', 0),
(3, 'GH-Rajaji Hospital', ' Alwarpuram', 'Madurai', 6321544545, 'gh003mdi@gmail.com', '10.992231', '77.085786', 'Women Care, Fertility Hospitals, child treatments', 'GH003', '123456', '05-03-2025', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ho_medicine`
--

CREATE TABLE `ho_medicine` (
  `id` int(11) NOT NULL,
  `docid` varchar(20) NOT NULL,
  `patient_id` varchar(20) NOT NULL,
  `medicine` varchar(100) NOT NULL,
  `details` varchar(200) NOT NULL,
  `rdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_medicine`
--

INSERT INTO `ho_medicine` (`id`, `docid`, `patient_id`, `medicine`, `details`, `rdate`) VALUES
(1, 'D1', 'PT3', 'Acetaminophen', '250mg, morning,night', '11-05-2025'),
(2, 'D1', 'PT2', 'Acetaminophen', '600mg, night', '12-05-2025'),
(3, 'D1', 'PT3', 'Acetaminophen', '250mg, Morning, Night', '12-05-2025'),
(4, 'D1', 'PT3', 'Paracetamol', '500mg, Morning, Night', '12-05-2025');

-- --------------------------------------------------------

--
-- Table structure for table `ho_nurse`
--

CREATE TABLE `ho_nurse` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `hospital` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_nurse`
--

INSERT INTO `ho_nurse` (`id`, `name`, `hospital`, `mobile`, `email`, `uname`, `pass`) VALUES
(1, 'Rekha', 'GH001', 8856977415, 'rekha@gmail.com', 'N1', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `ho_staff`
--

CREATE TABLE `ho_staff` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `hospital` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_staff`
--

INSERT INTO `ho_staff` (`id`, `name`, `hospital`, `mobile`, `email`, `uname`, `pass`) VALUES
(1, 'Sudha', 'GH001', 8956741455, 'sudha@gmail.com', 'S1', '1234');

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
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `stype` varchar(20) NOT NULL,
  UNIQUE KEY `aadhar` (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ho_user`
--

INSERT INTO `ho_user` (`id`, `name`, `gender`, `dob`, `mobile`, `email`, `address`, `parent_mobile`, `aadhar`, `blood_grp`, `uname`, `pass`, `rdate`, `stype`) VALUES
(1, 'Kumar', 'Male', '1980-05-04', 9894442716, 'kumar@gmail.com', '56,BS Nagar, Salem', 8859622546, '234479841145', '', 'PT1', '123456', '11-05-2025', 'register'),
(3, 'Usha', 'Female', '1975-08-05', 7586512121, 'usha@gmail.com', '25,SM Colony', 8954545452, '254477861164', '', 'PT3', '', '12-05-2025', 'entry'),
(5, 'Nimala', 'Female', '1980-08-07', 8545421565, 'nirmala@gmail.com', '11,NS Nagar', 8854521212, '257849955211', '', 'PT5', '', '12-05-2025', 'entry'),
(4, 'Gokul', 'Male', '1999-08-04', 7852455256, 'gokul@gmail.com', '43,RR Nagar', 8545754212, '258544756618', '', 'PT4', '', '12-05-2025', 'entry'),
(6, 'Vetri', 'Male', '1978-04-11', 7345485522, 'vetri@gmail.com', '12,SS Road', 6354821221, '258854519674', '', 'PT6', '', '12-05-2025', 'entry'),
(2, 'Vijay', 'Male', '1995-05-04', 9894442716, 'vijay@gmail.com', '44,FG Nagar', 8859622546, '315484545454', '', 'PT2', '1234', '11-05-2025', 'register');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `priority` int(11) default NULL,
  `estimated_duration` int(11) default NULL,
  `preferred_time` varchar(20) default NULL,
  `doctor_preference` int(11) default NULL,
  `status` varchar(20) default 'waiting',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`id`, `name`, `priority`, `estimated_duration`, `preferred_time`, `doctor_preference`, `status`) VALUES
(1, 'Raja', 2, 15, '10:30', 1, 'scheduled'),
(2, 'Kumar', 2, 15, '10:30', 1, 'scheduled'),
(3, 'Ajay', 3, 15, '11:00', 1, 'scheduled');

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE `schedule` (
  `id` int(11) NOT NULL auto_increment,
  `patient_id` int(11) default NULL,
  `doctor_id` int(11) default NULL,
  `time_slot` varchar(20) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`id`, `patient_id`, `doctor_id`, `time_slot`) VALUES
(1, 1, 1, '09:00'),
(2, 2, 1, '09:00'),
(3, 3, 1, '09:00');
