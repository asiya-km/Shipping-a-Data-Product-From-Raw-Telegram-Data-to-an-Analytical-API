with stg as (
    select * from {{ ref('stg_telegram_messages') }}
),
channels as (
    select * from {{ ref('dim_channels') }}
),
dates as (
    select * from {{ ref('dim_dates') }}
)
select
    stg.message_id,
    channels.id as channel_id,
    dates.id as date_id,
    stg.content,
    stg.has_image
from stg
join channels on stg.channel_id = channels.id
join dates on stg.date::date = dates.date 