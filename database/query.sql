-- primary table
CREATE TABLE user (
    id INTEGER primary KEY AutoIncrement,
    email varchar(100) NOT NULL,
    name varchar(100) NOT NULL,
    surname varchar(100) NOT NULL,
    role varchar(100) NOT NULL,
    password varchar(100) NOT NULL
)

-- test
INSERT INTO user(email, name, surname, role, password) values ("vgutierrez@atentus.com", "Vladimir", "Gutierrez", "admin", "Pass.001")

-- validation
SELECT * FROM user 

-- querys test
select * from resultado.resultado_stress_55205
select * from resultado.resultado_stress_66161