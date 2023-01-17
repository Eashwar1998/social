-- FUNCTION: public.createLikes()

-- DROP FUNCTION IF EXISTS public."createLikes"();

CREATE OR REPLACE FUNCTION public."createLikes"()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
	begin
		insert into likes (lcount,messageId) values (0,new.msgId);
		return new;
	END;

$BODY$;

ALTER FUNCTION public."createLikes"()
    OWNER TO postgres;
