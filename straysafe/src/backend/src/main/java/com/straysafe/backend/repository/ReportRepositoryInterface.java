package com.straysafe.backend.repository;

import com.straysafe.backend.api.model.request.ReportRequest;
import com.straysafe.backend.api.model.response.ReportResponse;
import com.straysafe.backend.domain.ReportDAOResponse;

import java.util.List;

public interface ReportRepositoryInterface {
    void createReport(ReportRequest reportRequest);
    List<ReportDAOResponse> getAllReports();
}
