CREATE TABLE if not exists "users"(
    id serial PRIMARY KEY,
    email varchar(255) not null ,
    passwd varchar not null,
    name varchar(255) not null,
    state boolean not null DEFAULT TRUE ,
    is_admin boolean not null DEFAULT FALSE
);

CREATE INDEX if not exists user_email ON users(email);


INSERT INTO users (email, passwd, name, state, is_admin) VALUES  ('www.kraken@mail.ru','1','JonnyBoy',TRUE,TRUE),
                                                                 ('altar.studio@gmail.com','2','SomeUserName',TRUE,TRUE),
                                                                 ('test@mail.ru','3','JustUser',TRUE,FALSE);