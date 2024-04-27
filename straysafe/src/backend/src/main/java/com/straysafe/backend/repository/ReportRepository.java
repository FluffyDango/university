package com.straysafe.backend.repository;

import com.straysafe.backend.api.model.request.ReportRequest;
import com.straysafe.backend.api.model.response.ReportResponse;
import com.straysafe.backend.domain.ReportDAOResponse;
import com.straysafe.backend.repository.mapper.ReportMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.core.namedparam.SqlParameterSource;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class ReportRepository implements ReportRepositoryInterface {

    private final NamedParameterJdbcTemplate namedParameterJdbcTemplate;

    @Autowired
    public ReportRepository(NamedParameterJdbcTemplate template) {
        this.namedParameterJdbcTemplate = template;
    }

    @Override
    public void createReport(ReportRequest request) {

        String query = """
              INSERT INTO REPORTS(imageUrl, timeAgo, petName, status, authorName, authorNickName, type, posted, animalType, petId, latitude, longtitude, dominantColors, collarColor, breed, size, gender, tel, email, social, note)
              VALUES(:imageUrl, :timeAgo, :petName, :status, :authorName, :authorNickName, :type, :posted, :animalType, :petId, :latitude, :longtitude, :dominantColors, :collarColor, :breed, :size, :gender, :tel, :email, :social, :note);
                  """;
        SqlParameterSource params = new MapSqlParameterSource()
                .addValue("imageUrl", request.imageURL())
                .addValue("timeAgo", request.timeAgo())
                .addValue("petName", request.petName())
                .addValue("status", request.status())
                .addValue("location", request.location())
                .addValue("authorName", request.authorName())
                .addValue("authorNickName", request.authorNickname())
                .addValue("type", request.type())
                .addValue("posted", request.posted())
                .addValue("animalType", request.animalType())
                .addValue("petId", request.pet_id())
                .addValue("latitude", request.latitude())
                .addValue("longtitude", request.longtitude())
                .addValue("dominantColors", request.dominantColors())
                .addValue("collarColor", request.collarColor())
                .addValue("breed", request.breed())
                .addValue("size", request.size())
                .addValue("gender", request.gender())
                .addValue("tel", request.tel())
                .addValue("email", request.email())
                .addValue("social", request.social())
                .addValue("note", request.note());
        namedParameterJdbcTemplate.update(query, params);

    }

    @Override
    public List<ReportDAOResponse> getAllReports() {
        String query = """
                SELECT *
                FROM REPORTS;
                """;
        return namedParameterJdbcTemplate.query(query, new ReportMapper());
    }


}
