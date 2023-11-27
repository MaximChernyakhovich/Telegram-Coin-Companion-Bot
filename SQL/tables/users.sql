CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL,
    firstname character varying(64) COLLATE pg_catalog."default",
    lastname character varying(64) COLLATE pg_catalog."default",
    nickname character varying(32) COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT users_pk PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;