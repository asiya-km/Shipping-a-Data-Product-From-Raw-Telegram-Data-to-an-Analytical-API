-- Raw Telegram messages model
select * from {{ source('raw', 'telegram_messages') }} 