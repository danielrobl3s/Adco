-- Table: public.prospectos

-- DROP TABLE IF EXISTS public.prospectos;

CREATE TABLE IF NOT EXISTS public.prospectos
(
    id_prospecto integer NOT NULL,
    nombre character varying(30) COLLATE pg_catalog."default",
    apellido character varying(30) COLLATE pg_catalog."default",
    telefono integer,
    observaciones character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT prospectos_pkey PRIMARY KEY (id_prospecto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.prospectos
    OWNER to postgres;