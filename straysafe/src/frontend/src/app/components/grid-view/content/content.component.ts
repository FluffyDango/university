import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ReportBoxComponent } from './report-box/report-box.component';
import { ReportPopupComponent } from './report-popup/report-popup.component';
import { ApiService } from '../../../services/api-service.service';

@Component({
  selector: 'app-content',
  standalone: true,
  imports: [
    CommonModule,
    ReportBoxComponent,
    ReportPopupComponent
  ],
  templateUrl: './content.component.html',
})
export class ContentComponent implements OnInit {
  reportData: any;
  selectedReport: any;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.getReports().subscribe((data: any) => {
      this.reportData = data;
      console.log(this.reportData)
    });
  }

  openModal(report: any) {
    this.selectedReport = report;
  }

  onCloseModal() {
    this.selectedReport = null;
  }
}
