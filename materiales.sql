-- Table: public.materiales

-- DROP TABLE IF EXISTS public.materiales;

CREATE TABLE IF NOT EXISTS public.materiales
(
    id_material integer NOT NULL DEFAULT nextval('materiales_id_material_seq'::regclass),
    recurso character varying COLLATE pg_catalog."default",
    cantidad double precision,
    concepto character varying COLLATE pg_catalog."default",
    fecha date,
    CONSTRAINT materiales_pk PRIMARY KEY (id_material)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.materiales
    OWNER to postgres;