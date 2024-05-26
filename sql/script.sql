-- create tables
CREATE TABLE IF NOT EXISTS dish_list
(
    dish_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name  TEXT    NOT NULL UNIQUE,
    dish_price NUMERIC NOT NULL,
    dish_cost  NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS table_list
(
    table_id       INTEGER PRIMARY KEY,
    table_capacity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS table_in_use
(
    table_id   INTEGER  NOT NULL,
    date       DATE     NOT NULL,
    start_time TIME     NOT NULL,
    end_time   TIME     NOT NULL
);

CREATE TABLE IF NOT EXISTS reservation
(
    id           INTEGER  PRIMARY KEY AUTOINCREMENT,
    name         TEXT     NOT NULL,
    datetime     DATETIME NOT NULL DEFAULT (DATETIME('now', 'localtime')),
    reserve_date DATE     NOT NULL,
    reserve_time TIME     NOT NULL,
    table_id     INTEGER  NOT NULL,
    dish_bool    BOOLEAN           DEFAULT (0) NOT NULL
);

CREATE TABLE IF NOT EXISTS reserve_dish
(
    reserve_id      INTEGER                 NOT NULL,
    dish_id         INTEGER                 NOT NULL,
    dish_unit_price NUMERIC                 NOT NULL,
    dish_amount     INTEGER                 NOT NULL,
    payment_status  TEXT DEFAULT 'NOT PAID' NOT NULL
);

CREATE TABLE IF NOT EXISTS dineIn_cashier
(
    order_id       INTEGER  NOT NULL,
    datetime       DATETIME NOT NULL DEFAULT (DATETIME('now', 'localtime')),
    table_id       INTEGER  NOT NULL,
    dish_id        INTEGER  NOT NULL,
    dish_price     NUMERIC  NOT NULL,
    dish_amount    INTEGER  NOT NULL,
    payment_status TEXT              DEFAULT 'NOT PAID' NOT NULL
);

CREATE TABLE IF NOT EXISTS dineIn_kitchen
(
    order_id     INTEGER                NOT NULL,
    time         TIME                   NOT NULL,
    dish_id      INTEGER                NOT NULL,
    dish_amount  INTEGER                NOT NULL,
    serving_stat TEXT DEFAULT 'PENDING' NOT NULL
);

CREATE TABLE IF NOT EXISTS reserve_kitchen
(
    reserve_id   INTEGER                NOT NULL,
    time         TIME                   NOT NULL,
    dish_id      INTEGER                NOT NULL,
    dish_amount  INTEGER                NOT NULL,
    serving_stat TEXT DEFAULT 'PENDING' NOT NULL
);

-- create views
CREATE VIEW IF NOT EXISTS kitchen_view AS
SELECT dineIn.time,
       DATE(SUBSTR(dineIn.time, 1, 10)) AS date,
       'DINE IN'                        AS serve_type,
       dineIn.order_id                  AS ID,
       dineIn.dish_id,
       dish.dish_name,
       dineIn.dish_amount,
       dish.dish_price,
       dish.dish_cost,
       dineIn.serving_stat
FROM dinein_kitchen dineIn
     JOIN dish_list dish ON dinein.dish_id = dish.dish_id

UNION ALL

SELECT reserve.time,
       DATE(SUBSTR(reserve.time, 1, 10)) AS date,
       'RESERVE'                         AS serve_type,
       reserve.reserve_id                AS ID,
       reserve.dish_id,
       dish.dish_name,
       reserve.dish_amount,
       dish.dish_price,
       dish.dish_cost,
       reserve.serving_stat
FROM reserve_kitchen reserve
     JOIN dish_list dish ON reserve.dish_id = dish.dish_id
ORDER BY time;


CREATE VIEW IF NOT EXISTS table_inUse_view AS
SELECT inUse.date,
       inUse.start_time AS time,
       inUse.end_time,
       inUse.table_id,
       list.table_capacity
FROM table_in_use inUse
     JOIN table_list list ON inUse.table_id = list.table_id
ORDER BY inUse.date;