package com.straysafe.backend.api.model.request;

import java.math.BigDecimal;
import java.sql.Timestamp;

public record ReportRequest(
        String imageURL,
        String timeAgo,
        String petName,
        int status,
        String location,
        String authorName,
        String authorNickname,
        int type,
        long id,
        Timestamp posted,
        String animalType,
        long pet_id,
        BigDecimal latitude,
        BigDecimal longtitude,
        String dominantColors,
        String collarColor,
        String breed,
        String size,
        String gender,
        String tel,
        String email,
        String social,
        String note
) {
}
