CREATE TABLE if not exists "users"(
    id serial PRIMARY KEY,
    email varchar(255) not null UNIQUE ,
    passwd varchar not null,
    name varchar(255) not null,
    state boolean not null DEFAULT TRUE ,
    is_admin boolean not null DEFAULT FALSE
);

CREATE INDEX if not exists user_email ON users(email);


INSERT INTO users (email, passwd, name, state, is_admin) VALUES  ('www.kraken@mail.ru','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','JonnyBoy',TRUE,TRUE),
                                                                 ('alar.studio@gmail.com','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','SomeUserName',TRUE,TRUE),
                                                                 ('test@mail.ru','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','JustUser',TRUE,FALSE);