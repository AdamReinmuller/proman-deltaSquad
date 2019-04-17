ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;

DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_id_seq;
CREATE TABLE users (
    id serial NOT NULL,
    user_name varchar(255),
    hashed_pw varchar(255)
);

ALTER TABLE ONLY users
    ADD CONSTRAINT pk_users_id PRIMARY KEY (id);


CREATE TABLE privateBoards (
    id serial NOT NULL,
    board_name varchar(255),
    userID int
);

ALTER TABLE ONLY privateBoards
    ADD CONSTRAINT pk_privateBoards_id PRIMARY KEY (id);

ALTER TABLE ONLY privateBoards
    ADD CONSTRAINT fk_userID_id FOREIGN KEY (userID) REFERENCES users(id) ON DELETE CASCADE;


