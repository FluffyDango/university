import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchReportsComponent } from './search-reports.component';

describe('SearchReportsComponent', () => {
  let component: SearchReportsComponent;
  let fixture: ComponentFixture<SearchReportsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchReportsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SearchReportsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
