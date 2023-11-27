CREATE OR REPLACE PROCEDURE public.add_user(IN tg_id integer, IN firstname character varying, IN lastname character varying, IN tg_nick character varying)
 LANGUAGE plpgsql
AS $procedure$
BEGIN
    -- try tran
    BEGIN
        IF NOT EXISTS (SELECT id FROM users WHERE id = tg_id) THEN
            -- Вставка строки в таблицу users
            INSERT INTO users (id, firstname, lastname, nickname) 
            VALUES (tg_id, firstname, lastname, tg_nick); 

            -- Вставка строки в таблицу balance
            INSERT INTO balance (user_id) 
            VALUES (tg_id);

            -- Вставка строки в таблицу categories
            INSERT INTO categories (user_id, name_category)
            VALUES (tg_id, 'refill');

            RAISE NOTICE '1'; -- Success notice

        ELSE
            RAISE NOTICE '0'; -- Existing user notice
        END IF;
    EXCEPTION
        -- Ловим ошибку в случае возникновения и откатываем транзакцию
        WHEN OTHERS THEN
            -- Выводим сообщение об ошибке
            -- добавить логгирование в отдельную таблицу RAISE NOTICE 'Ошибка: %', SQLERRM;
            RAISE NOTICE '0'; -- Error notice
    END;

END $procedure$
;
