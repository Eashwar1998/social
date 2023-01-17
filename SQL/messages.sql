-- Table: public.messages

-- DROP TABLE IF EXISTS public.messages;

CREATE TABLE IF NOT EXISTS public.messages
(
    msgid integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 100000 CACHE 1 ),
    message text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT messages_pkey PRIMARY KEY (msgid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.messages
    OWNER to postgres;

-- Trigger: addmsg

-- DROP TRIGGER IF EXISTS addmsg ON public.messages;

CREATE TRIGGER addmsg
    AFTER INSERT
    ON public.messages
    FOR EACH ROW
    EXECUTE FUNCTION public."createLikes"();