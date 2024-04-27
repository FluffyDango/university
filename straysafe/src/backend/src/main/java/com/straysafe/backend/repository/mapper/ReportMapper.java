package com.straysafe.backend.repository.mapper;

import com.straysafe.backend.api.model.response.ReportResponse;
import com.straysafe.backend.domain.ReportDAOResponse;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;

public class ReportMapper implements RowMapper<ReportDAOResponse> {

    @Override
    public ReportDAOResponse mapRow(ResultSet resultSet, int rowNum) throws SQLException {
        return new ReportDAOResponse(
                resultSet.getString("imageUrl"),
                resultSet.getString("timeAgo"),
                resultSet.getString("petName"),
                resultSet.getInt("status"),
                resultSet.getString("location"),
                resultSet.getString("authorName"),
                resultSet.getString("authorNickName"),
                resultSet.getInt("type"),
                resultSet.getLong("id"),
                resultSet.getTimestamp("posted"),
                resultSet.getString("animalType"),
                resultSet.getLong("petId"),
                resultSet.getBigDecimal("latitude"),
                resultSet.getBigDecimal("longtitude"),
                resultSet.getString("dominantColors"),
                resultSet.getString("collarColor"),
                resultSet.getString("breed"),
                resultSet.getString("size"),
                resultSet.getString("gender"),
                resultSet.getString("tel"),
                resultSet.getString("email"),
                resultSet.getString("social"),
                resultSet.getString("note"));
    }
}

