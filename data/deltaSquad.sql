--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

-- ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS pk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.boards
  DROP CONSTRAINT IF EXISTS pk_boards_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.users
  DROP CONSTRAINT IF EXISTS fk_card_status_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.privateBoards
  DROP CONSTRAINT IF EXISTS fk_card_board_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.cards
  DROP CONSTRAINT IF EXISTS pk_cards_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.statuses
  DROP CONSTRAINT IF EXISTS pk_statuses_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.users
  DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;



DROP TABLE IF EXISTS public.boards;
DROP SEQUENCE IF EXISTS public.boards_id_seq;
CREATE TABLE boards
(
  id    serial NOT NULL,
  title text
);

DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_id_seq;
CREATE TABLE users
(
  id        serial NOT NULL,
  user_name varchar(255),
  hashed_pw varchar(255)
);


DROP TABLE IF EXISTS public.privateBoards;
DROP SEQUENCE IF EXISTS public.privateBoards_seq;
CREATE TABLE privateBoards
(
  id         serial NOT NULL,
  board_name varchar(255),
  user_id    int
);


DROP TABLE IF EXISTS public.cards;
DROP SEQUENCE IF EXISTS public.cards_id_seq;
CREATE TABLE cards
(
  id           serial NOT NULL,
  board_id     integer,
  title        text,
  status_id    integer,
  order_number integer
);


DROP TABLE IF EXISTS public.statuses;
DROP SEQUENCE IF EXISTS public.statuses_id_seq;
CREATE TABLE statuses
(
  id    serial NOT NULL,
  title text
);


ALTER TABLE ONLY statuses
  ADD CONSTRAINT pk_statuses_id PRIMARY KEY (id);

ALTER TABLE ONLY users
  ADD CONSTRAINT pk_users_id PRIMARY KEY (id);

ALTER TABLE ONLY boards
  ADD CONSTRAINT pk_boards_id PRIMARY KEY (id);

ALTER TABLE ONLY cards
  ADD CONSTRAINT pk_cards_id PRIMARY KEY (id);

ALTER TABLE ONLY privateBoards
  ADD CONSTRAINT pk_privateBoards_id PRIMARY KEY (id);

ALTER TABLE ONLY cards
  ADD CONSTRAINT fk_card_board_id FOREIGN KEY (board_id) REFERENCES boards (id) ON DELETE CASCADE;

ALTER TABLE ONLY cards
  ADD CONSTRAINT fk_card_status_id FOREIGN KEY (status_id) REFERENCES statuses (id) ON DELETE CASCADE;

ALTER TABLE ONLY privateBoards
  ADD CONSTRAINT fk_userID_id FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE;



INSERT INTO boards
VALUES (1, 'Board 1');
INSERT INTO boards
VALUES (2, 'Board 2');


INSERT INTO statuses
VALUES (0, 'new');
INSERT INTO statuses
VALUES (1, 'in progress');
INSERT INTO statuses
VALUES (2, 'testing');
INSERT INTO statuses
VALUES (3, 'done');


INSERT INTO cards
VALUES (1, 1, 'new card', 0, 0);
INSERT INTO cards
VALUES (2, 1, 'new card', 0, 1);
INSERT INTO cards
VALUES (3, 1, 'in progress card', 1, 0);
INSERT INTO cards
VALUES (4, 1, 'planning', 2, 0);
INSERT INTO cards
VALUES (5, 1, 'planning card', 2, 1);
INSERT INTO cards
VALUES (6, 1, 'done card', 3, 0);
INSERT INTO cards
VALUES (7, 1, 'done card', 3, 1);
INSERT INTO cards
VALUES (8, 1, 'done card', 3, 2);
INSERT INTO cards
VALUES (9, 2, 'done card', 3, 3);


INSERT INTO users
VALUES (0, 'kris', 'astfgl');
INSERT INTO users
VALUES (1, 'nemkris', 'megintastfgl');


INSERT INTO privateBoards
VALUES (0, 'firstBoard', 0);
INSERT INTO privateBoards
VALUES (1, 'thirdBoard', 0);
INSERT INTO privateBoards
VALUES (2, 'secondBoard', 0);



SELECT pg_catalog.setval('statuses_id_seq', 4, true);

SELECT pg_catalog.setval('boards_id_seq', 2, true);

SELECT pg_catalog.setval('cards_id_seq', 6, true);

SELECT pg_catalog.setval('users_id_seq', 2, true);

SELECT pg_catalog.setval('privateBoards_id_seq', 3, true);
