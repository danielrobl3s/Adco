-- Table: public.proyectos

-- DROP TABLE IF EXISTS public.proyectos;

CREATE TABLE IF NOT EXISTS public.proyectos
(
    id_proyecto integer NOT NULL,
    proyecto character varying(50) COLLATE pg_catalog."default",
    institucion character varying(20) COLLATE pg_catalog."default",
    fecha_inicio date,
    fecha_termino date,
    telefono integer,
    direccion character varying(50) COLLATE pg_catalog."default",
    ubicacion character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT proyectos_pkey PRIMARY KEY (id_proyecto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.proyectos
    OWNER to postgres;