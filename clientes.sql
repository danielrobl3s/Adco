-- Table: public.clientes

-- DROP TABLE IF EXISTS public.clientes;

CREATE TABLE IF NOT EXISTS public.clientes
(
    id_cliente integer NOT NULL DEFAULT nextval('clientes_id_cliente_seq'::regclass),
    nombre character varying COLLATE pg_catalog."default",
    metodo_pago character varying COLLATE pg_catalog."default",
    fecha date,
    documentos character varying COLLATE pg_catalog."default",
    observaciones character varying COLLATE pg_catalog."default",
    CONSTRAINT clientes_pk PRIMARY KEY (id_cliente)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clientes
    OWNER to postgres;