-- Table: public.gastos

-- DROP TABLE IF EXISTS public.gastos;

CREATE TABLE IF NOT EXISTS public.gastos
(
    id_gasto integer NOT NULL DEFAULT nextval('gastos_id_gasto_seq'::regclass),
    concepto character varying COLLATE pg_catalog."default",
    monto double precision,
    metodo_pago character varying COLLATE pg_catalog."default",
    cobrador character varying COLLATE pg_catalog."default",
    fecha date,
    CONSTRAINT gastos_pk PRIMARY KEY (id_gasto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.gastos
    OWNER to postgres;