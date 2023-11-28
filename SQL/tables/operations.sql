CREATE TABLE IF NOT EXISTS public.operations
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    event_datetime timestamp without time zone NOT NULL,
    user_id integer NOT NULL,
    operation_amount numeric(10,2) NOT NULL,
    current_balance numeric(10,2) NOT NULL,
    category_id integer NOT NULL,
    as_name character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT "id_PK" PRIMARY KEY (id),
    CONSTRAINT "oper_user_id_FK" FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.operations
    OWNER to postgres;