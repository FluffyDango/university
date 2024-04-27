import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AddressInputComponent } from '../address-input/address-input.component';
import { ImageUploadComponent } from '../image-upload/image-upload.component';
import { CommonModule } from '@angular/common';
import { ReportSummaryComponent } from '../report-summary/report-summary.component';

@Component({
  selector: 'app-lost-pet-page',
  standalone: true,
  imports: [CommonModule, AddressInputComponent, ImageUploadComponent, ReportSummaryComponent],
  templateUrl: './lost-pet-page.component.html'
})
export class LostPetPageComponent implements OnInit {
  currentStep: string = 'location';

  constructor(private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.currentStep = params['step'] || 'location';
    });
  }
}
