-- Database: adco

-- DROP DATABASE IF EXISTS adco;

CREATE DATABASE adco
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
-- Table: public.project_proveedores_trabajadores

-- DROP TABLE IF EXISTS public.project_proveedores_trabajadores;

CREATE TABLE IF NOT EXISTS public.project_proveedores_trabajadores
(
    id integer NOT NULL,
    nombre character varying(50) COLLATE pg_catalog."default",
    telefono integer,
    correo character varying(50) COLLATE pg_catalog."default",
    direccion character varying(50) COLLATE pg_catalog."default",
    especialidad character varying(20) COLLATE pg_catalog."default",
    concepto character varying(20) COLLATE pg_catalog."default",
    archivos character varying(100) COLLATE pg_catalog."default",
    contratos character varying(50) COLLATE pg_catalog."default",
    monto_contrato double precision,
    abonos double precision,
    saldo double precision,
    CONSTRAINT project_proveedores_trabajadores_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.project_proveedores_trabajadores
    OWNER to postgres;
	
-- Table: public.proyectos

-- DROP TABLE IF EXISTS public.proyectos;

CREATE TABLE IF NOT EXISTS public.proyectos
(
    id_proyecto integer NOT NULL,
    proyecto character varying(30) COLLATE pg_catalog."default",
    institucion character varying(20) COLLATE pg_catalog."default",
    fecha_inicio date,
    fecha_termino date,
    telefono integer,
    direccion character varying(50) COLLATE pg_catalog."default",
    ubicacion character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT proyectos_pkey PRIMARY KEY (id_proyecto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.proyectos
    OWNER to postgres;
	
-- Table: public.trabajadores_proveedores

-- DROP TABLE IF EXISTS public.trabajadores_proveedores;

CREATE TABLE IF NOT EXISTS public.trabajadores_proveedores
(
    id integer NOT NULL,
    nombre character varying(50) COLLATE pg_catalog."default",
    telefono integer,
    correo character varying(50) COLLATE pg_catalog."default",
    direccion character varying(50) COLLATE pg_catalog."default",
    especialidad character varying(20) COLLATE pg_catalog."default",
    concepto character varying(20) COLLATE pg_catalog."default",
    archivos character varying(100) COLLATE pg_catalog."default",
    contratos character varying(50) COLLATE pg_catalog."default",
    monto_contrato double precision,
    abonos double precision,
    saldo double precision,
    CONSTRAINT trabajadores_proveedores_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.trabajadores_proveedores
    OWNER to postgres;