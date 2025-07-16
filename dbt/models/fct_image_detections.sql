select
    d.id as detection_id,
    m.message_id,
    d.detected_object_class,
    d.confidence_score
from {{ ref('image_detections_staging') }} d
join {{ ref('fct_messages') }} m on d.message_id = m.message_id 