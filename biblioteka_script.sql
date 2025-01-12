-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mylibrary
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mylibrary
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mylibrary` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mylibrary` ;

-- -----------------------------------------------------
-- Table `mylibrary`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC) VISIBLE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `mylibrary`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 69
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`auth_group_permissions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `mylibrary`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `mylibrary`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(150) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`auth_user_groups` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC) VISIBLE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `mylibrary`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`auth_user_user_permissions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `mylibrary`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`authors` (
  `author_id` INT NOT NULL AUTO_INCREMENT,
  `author_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`author_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`books` (
  `book_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `publisher` VARCHAR(45) NOT NULL,
  `published_year` VARCHAR(4) NOT NULL,
  PRIMARY KEY (`book_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`booksauthors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`booksauthors` (
  `book_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `author_id`),
  INDEX `author_id` (`author_id` ASC) VISIBLE,
  CONSTRAINT `booksauthors_ibfk_1`
    FOREIGN KEY (`book_id`)
    REFERENCES `mylibrary`.`books` (`book_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `booksauthors_ibfk_2`
    FOREIGN KEY (`author_id`)
    REFERENCES `mylibrary`.`authors` (`author_id`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`genres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`genres` (
  `genre_id` INT NOT NULL AUTO_INCREMENT,
  `genre_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`booksgenres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`booksgenres` (
  `book_id` INT NOT NULL,
  `genre_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `genre_id`),
  INDEX `genre_id` (`genre_id` ASC) VISIBLE,
  CONSTRAINT `booksgenres_ibfk_1`
    FOREIGN KEY (`book_id`)
    REFERENCES `mylibrary`.`books` (`book_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `booksgenres_ibfk_2`
    FOREIGN KEY (`genre_id`)
    REFERENCES `mylibrary`.`genres` (`genre_id`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) VISIBLE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `mylibrary`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`django_migrations` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`physical_books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`physical_books` (
  `physical_book_id` INT NOT NULL AUTO_INCREMENT,
  `state` TINYINT(1) NOT NULL,
  `book_id` INT NULL,
  PRIMARY KEY (`physical_book_id`, `book_id`),
  INDEX `fk_physical_book_books_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_physical_book_books`
    FOREIGN KEY (`book_id`)
    REFERENCES `mylibrary`.`books` (`book_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `phone_number` VARCHAR(50) NOT NULL,
  `role` VARCHAR(5) NOT NULL,
  `password_hash` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`loans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`loans` (
  `loan_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `physical_book_id` INT NOT NULL,
  `loan_date` DATE NOT NULL,
  `return_date` DATE NOT NULL,
  `status` TINYINT(1) NOT NULL,
  PRIMARY KEY (`loan_id`, `user_id`, `physical_book_id`),
  INDEX `fk4_user_id` (`user_id` ASC) VISIBLE,
  INDEX `fk_loan_physical_idx` (`physical_book_id` ASC) VISIBLE,
  CONSTRAINT `fk_loan_physical`
    FOREIGN KEY (`physical_book_id`)
    REFERENCES `mylibrary`.`physical_books` (`physical_book_id`),
  CONSTRAINT `fk_loan_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`fines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`fines` (
  `fine_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(4,2) NOT NULL,
  `issued_date` DATE NOT NULL,
  `status` TINYINT(1) NOT NULL,
  `loans_loan_id` INT NOT NULL,
  PRIMARY KEY (`fine_id`, `user_id`, `loans_loan_id`),
  INDEX `fk_fines_user` (`user_id` ASC) VISIBLE,
  INDEX `fk_fines_loans1_idx` (`loans_loan_id` ASC) VISIBLE,
  CONSTRAINT `fk_fines_loans`
    FOREIGN KEY (`loans_loan_id`)
    REFERENCES `mylibrary`.`loans` (`loan_id`),
  CONSTRAINT `fk_fines_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`holds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`holds` (
  `hold_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `physical_book_id` INT NOT NULL,
  `hold_date` DATE NOT NULL,
  `release_date` DATE NOT NULL,
  `status` TINYINT(1) NOT NULL,
  PRIMARY KEY (`hold_id`, `user_id`, `physical_book_id`),
  INDEX `fk_hold_user` (`user_id` ASC) VISIBLE,
  INDEX `fk_hold_physical_idx` (`physical_book_id` ASC) VISIBLE,
  CONSTRAINT `fk_hold_physical`
    FOREIGN KEY (`physical_book_id`)
    REFERENCES `mylibrary`.`physical_books` (`physical_book_id`),
  CONSTRAINT `fk_hold_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mylibrary`.`notifictions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mylibrary`.`notifictions` (
  `notification_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `message` VARCHAR(255) NOT NULL,
  `sent_date` DATE NOT NULL,
  `notification_read` TINYINT(1) NOT NULL,
  `loan_id` INT NULL DEFAULT NULL,
  `fines_id` INT NULL DEFAULT NULL,
  `hold_id` INT NULL DEFAULT NULL,
  `notifiction_type` ENUM('loan', 'fine', 'hold') NOT NULL,
  PRIMARY KEY (`notification_id`),
  INDEX `fk_notif_user` (`user_id` ASC) VISIBLE,
  INDEX `fk_notif_loan_idx` (`loan_id` ASC) VISIBLE,
  INDEX `fk_notif_hold_idx` (`hold_id` ASC) VISIBLE,
  INDEX `fk_notif_fines_idx` (`fines_id` ASC) VISIBLE,
  CONSTRAINT `fk_notif_fines`
    FOREIGN KEY (`fines_id`)
    REFERENCES `mylibrary`.`fines` (`fine_id`),
  CONSTRAINT `fk_notif_hold`
    FOREIGN KEY (`hold_id`)
    REFERENCES `mylibrary`.`holds` (`hold_id`),
  CONSTRAINT `fk_notif_loan`
    FOREIGN KEY (`loan_id`)
    REFERENCES `mylibrary`.`loans` (`loan_id`),
  CONSTRAINT `fk_notif_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mylibrary`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
