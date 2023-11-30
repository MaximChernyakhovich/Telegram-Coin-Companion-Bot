CREATE OR REPLACE PROCEDURE public.insert_operation(
    IN p_user_id integer,
    IN p_operation_amount numeric,
    IN p_category_id integer,
    IN p_as_name character varying,
    IN p_type_operation integer)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    v_current_balance numeric(10,2);
BEGIN
    -- Начало транзакции
    -- 0 ошибка, 1 успешное выполнение
    BEGIN
        -- try
        BEGIN
            -- Ваш текущий код
            SELECT money_amount INTO v_current_balance
            FROM balance
            WHERE user_id = p_user_id;

            INSERT INTO public.operations (
                event_datetime,
                user_id,
                operation_amount,
                current_balance,
                category_id,
                as_name,
                operation_type_id
            ) VALUES (
                NOW(),
                p_user_id,
                p_operation_amount,
                v_current_balance,
                p_category_id,
                p_as_name,
                p_type_operation
            );

            IF p_type_operation = 1 THEN
                UPDATE balance
                SET money_amount = v_current_balance + p_operation_amount
                WHERE user_id = p_user_id;
            ELSE
                UPDATE balance
                SET money_amount = v_current_balance - p_operation_amount
                WHERE user_id = p_user_id;
            END IF;

        EXCEPTION
            -- Обработка ошибок
            WHEN OTHERS THEN
                -- Откат
                ROLLBACK;

                RAISE NOTICE '0';

                RETURN;
        END;

        COMMIT;

        RAISE NOTICE '1';
    END;
END;
$BODY$;
ALTER PROCEDURE public.insert_operation(integer, numeric, integer, character varying)
    OWNER TO postgres;