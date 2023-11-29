CREATE TABLE IF NOT EXISTS public.operation_types
(
    id integer NOT NULL DEFAULT nextval('operation_types_id_seq'::regclass),
    type_name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "operation_types_PK" PRIMARY KEY (id),
    CONSTRAINT "operation_types_type_name_Unique" UNIQUE (type_name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.operation_types
    OWNER to postgres;