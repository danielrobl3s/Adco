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