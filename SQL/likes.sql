-- Table: public.likes

-- DROP TABLE IF EXISTS public.likes;

CREATE TABLE IF NOT EXISTS public.likes
(
    likeid integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 10000 CACHE 1 ),
    lcount integer NOT NULL DEFAULT 0,
    messageid integer NOT NULL,
    CONSTRAINT likes_pkey PRIMARY KEY (likeid),
    CONSTRAINT "likes_messageId_fkey" FOREIGN KEY (messageid)
        REFERENCES public.messages (msgid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.likes
    OWNER to postgres;