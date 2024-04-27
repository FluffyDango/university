import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FoundPetPageComponent } from './found-pet-page.component';

describe('FoundPetPageComponent', () => {
  let component: FoundPetPageComponent;
  let fixture: ComponentFixture<FoundPetPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FoundPetPageComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FoundPetPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
