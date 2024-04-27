package com.straysafe.backend.service;


import com.straysafe.backend.api.model.request.ReportRequest;
import com.straysafe.backend.api.model.response.ReportResponse;
import com.straysafe.backend.domain.ReportDAOResponse;
import com.straysafe.backend.repository.ReportRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ReportService {
    ReportRepository reportRepository;

    public ReportService(ReportRepository reportRepository) {
        this.reportRepository = reportRepository;
    }

    public List<ReportResponse> getAllReports() {
        List<ReportDAOResponse> reports = reportRepository.getAllReports();
        return reports.stream().map(this::mapDAOtoResponse).toList();
    }

    public void createReport(ReportRequest report) {
        reportRepository.createReport(report);
    }


    private ReportResponse mapDAOtoResponse(ReportDAOResponse dao) {
        return new ReportResponse(
                dao.imageURL(),
                dao.timeAgo(),
                dao.petName(),
                dao.status(),
                dao.location(),
                dao.authorName(),
                dao.authorNickname(),
                dao.type(),
                dao.id(),
                dao.posted(),
                dao.animalType(),
                dao.pet_id(),
                dao.latitude(),
                dao.longtitude(),
                dao.dominantColors(),
                dao.collarColor(),
                dao.breed(),
                dao.size(),
                dao.gender(),
                dao.tel(),
                dao.email(),
                dao.social(),
                dao.note()
        );
    }
}
