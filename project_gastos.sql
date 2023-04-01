-- Table: public.project_gastos

-- DROP TABLE IF EXISTS public.project_gastos;

CREATE TABLE IF NOT EXISTS public.project_gastos
(
    id_gasto integer NOT NULL,
    id_proyecto integer NOT NULL,
	concepto character varying(20) COLLATE pg_catalog."default",
    monto double precision,
	metodo_pago character varying(20) COLLATE pg_catalog."default",
	cobrador character varying(20) COLLATE pg_catalog."default",
    fecha date,
    CONSTRAINT project_gastos_pkey PRIMARY KEY (id_gasto)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.project_gastos
    OWNER to postgres;