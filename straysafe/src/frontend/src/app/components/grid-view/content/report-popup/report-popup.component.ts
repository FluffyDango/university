import { CommonModule } from '@angular/common';
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-report-popup',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './report-popup.component.html'
})
export class ReportPopupComponent {
  @Input() report: any;
  @Output() closeModal: EventEmitter<void> = new EventEmitter<void>();

  lost = $localize`:@@lost:LOST`;
  found = $localize`:@@found:FOUND`;
  active = $localize`:@@active:ACTIVE`;
  nonActive = $localize`:@@nonActive:NON-AKTIVE`;

  constructor() { }
  
  close() {
    this.closeModal.emit();
  }
}
