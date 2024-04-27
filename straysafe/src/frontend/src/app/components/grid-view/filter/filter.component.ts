import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-filter',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './filter.component.html',
})
export class FilterComponent {
  newBreed = '';
  selectedOptions: any = {
    lost: true,
    found: true,
    location: '',
    distance: "1",
    published: "1",
    cat: true,
    dog: true,
    other: false,
    breeds: [],
    male: true,
    female: true,
    createdBy: ''
  };

  location = $localize`:@@location:Location`;
  username = $localize`:@@username:Username`;
  breed = $localize`:@@breed:Breed`;


  applyFilter() {
    // console.log('Selected Options:', this.selectedOptions);
  }

  ngOnInit(): void {
    this.applyFilter();
  }

  onCheckboxChange(event: any) {
    const { name, checked } = event.target;
    this.selectedOptions[name] = checked;
  }

  onRangeChange(event: any, name: string) {
    this.selectedOptions[name] = event.target.value;
  }

  onDropdownChange(event: any) {
    this.selectedOptions['breed'] = event.target.value;
  }

  addBreed() {
    if (this.newBreed.trim()) {
      this.selectedOptions.breeds.push(this.newBreed.trim());
      this.newBreed = '';
    }
  }

  removeBreed(breedToRemove: string) {
    const index = this.selectedOptions.breeds.indexOf(breedToRemove);
    if (index > -1) {
      this.selectedOptions.breeds.splice(index, 1);
    }
  }
}
