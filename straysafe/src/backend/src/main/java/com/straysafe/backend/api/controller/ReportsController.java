package com.straysafe.backend.api.controller;

import com.straysafe.backend.api.model.request.ReportRequest;
import com.straysafe.backend.api.model.response.ReportResponse;
import com.straysafe.backend.service.ReportService;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/reports")
@CrossOrigin("*")
public class ReportsController {

    ReportService reportService;

    public ReportsController(ReportService reportService) {
        this.reportService = reportService;
    }

    @GetMapping()
    public List<ReportResponse> getAllReports() {
        return reportService.getAllReports();
    }

    @PostMapping("/create")
    @ResponseStatus(HttpStatus.CREATED)
    public void createReport(@RequestBody ReportRequest report) {
        reportService.createReport(report);
    }
}
