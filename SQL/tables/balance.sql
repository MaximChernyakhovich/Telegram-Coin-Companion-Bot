CREATE TABLE IF NOT EXISTS public.balance
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id integer NOT NULL,
    money_amount numeric(10,2) NOT NULL DEFAULT 0,
    CONSTRAINT balance_pk PRIMARY KEY (id),
    CONSTRAINT "bal_user_id_FK" FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.balance
    OWNER to postgres;