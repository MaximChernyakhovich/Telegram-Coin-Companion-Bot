--нужно добавить транзацию в процедуру
CREATE OR REPLACE PROCEDURE public.insert_categories_for_user(
    IN p_user_id integer,
    IN p_category_string character varying)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    categories_array text[];
    category_value text;
BEGIN
    -- Временная таблица
    CREATE TEMP TABLE temp_t (
        user_id integer,
        name_category text
    );

    -- Преобразование в массив
    categories_array := STRING_TO_ARRAY(p_category_string, ',');

    -- Цикл
    FOR category_value IN SELECT UNNEST(categories_array)
    LOOP
        INSERT INTO temp_t (user_id, name_category) VALUES (p_user_id, category_value);
    END LOOP;
	
	delete from public.categories
	where user_id = p_user_id and name_category != 'refill';
	
    INSERT INTO public.categories (user_id, name_category)
    SELECT * FROM temp_t;

    RAISE NOTICE '1'; -- Success
    
    DROP TABLE IF EXISTS temp_t;
EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE '0'; -- Error
END;
$BODY$;
ALTER PROCEDURE public.insert_categories_for_user(integer, character varying)
    OWNER TO postgres;