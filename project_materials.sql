-- Table: public.project_materials

-- DROP TABLE IF EXISTS public.project_materials;

CREATE TABLE IF NOT EXISTS public.project_materials
(
    id_material integer NOT NULL,
    id_proyecto integer NOT NULL,
    recurso character varying(20) COLLATE pg_catalog."default",
    cantidad double precision,
    concepto character varying(20) COLLATE pg_catalog."default",
    fecha date,
    CONSTRAINT project_materials_pkey PRIMARY KEY (id_material),
    CONSTRAINT fk_proyecto_materials FOREIGN KEY (id_proyecto)
        REFERENCES public.project_clientes (id_proyecto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.project_materials
    OWNER to postgres;