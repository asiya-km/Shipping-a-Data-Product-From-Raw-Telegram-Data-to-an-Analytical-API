with raw as (
    select * from {{ ref('raw_telegram_messages') }}
)
select
    id as message_id,
    channel_id,
    content,
    date,
    has_image
from raw 