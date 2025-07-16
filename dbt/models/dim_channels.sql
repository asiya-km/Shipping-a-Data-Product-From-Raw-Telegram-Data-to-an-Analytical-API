select distinct
    channel_id as id,
    channel_name as name
from {{ ref('stg_telegram_messages') }} 