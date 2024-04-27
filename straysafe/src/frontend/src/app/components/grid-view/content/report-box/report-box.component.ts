import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-report-box',
  standalone: true,
  imports: [],
  templateUrl: './report-box.component.html',
})
export class ReportBoxComponent {
  @Input() report: any;

  lost = $localize`:@@lost:LOST`;
  found = $localize`:@@found:FOUND`;
  constructor() { }
}
