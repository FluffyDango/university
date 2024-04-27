import { Component } from '@angular/core';
import { FilterComponent } from './filter/filter.component';
import { ContentComponent } from './content/content.component';

@Component({
  selector: 'app-grid-view',
  standalone: true,
  imports: [
    FilterComponent,
    ContentComponent
  ],
  templateUrl: './grid-view.component.html',
})
export class GridViewComponent {
  enterSearchRegion = $localize`:@@enterSearchRegionHere:Enter search region here`;
}
