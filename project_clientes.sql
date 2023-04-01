-- Table: public.project_clientes

-- DROP TABLE IF EXISTS public.project_clientes;

CREATE TABLE IF NOT EXISTS public.project_clientes
(
    id_cliente integer NOT NULL,
    id_proyecto integer NOT NULL,
    nombre character varying(50) COLLATE pg_catalog."default",
    metodo_pago character varying(20) COLLATE pg_catalog."default",
    fecha date,
    documentos character varying(100) COLLATE pg_catalog."default",
    observaciones character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT project_clientes_pkey PRIMARY KEY (id_cliente),
    CONSTRAINT unique_id_proyecto UNIQUE (id_proyecto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.project_clientes
    OWNER to postgres;