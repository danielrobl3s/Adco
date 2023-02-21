-- Table: public.usuarios

-- DROP TABLE IF EXISTS public.usuarios;

CREATE TABLE IF NOT EXISTS public.usuarios
(
    id_usuario integer NOT NULL DEFAULT nextval('usuarios_id_usuario_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default",
    edad integer,
    posicion character varying COLLATE pg_catalog."default",
    telefono numeric(10,0),
    CONSTRAINT usuarios_pk PRIMARY KEY (id_usuario)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;