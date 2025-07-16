with dates as (
    select distinct date::date as date
    from {{ ref('stg_telegram_messages') }}
)
select
    row_number() over (order by date) as id,
    date
from dates 