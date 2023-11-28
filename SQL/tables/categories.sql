CREATE TABLE IF NOT EXISTS public.categories
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id integer NOT NULL,
    name_category character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cat_user_id_pk PRIMARY KEY (id),
    CONSTRAINT user_category UNIQUE (user_id, name_category)
        INCLUDE(user_id, name_category),
    CONSTRAINT "user_id_FK" FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.categories
    OWNER to postgres;