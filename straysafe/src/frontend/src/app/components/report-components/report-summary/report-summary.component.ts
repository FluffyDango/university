import { CommonModule } from '@angular/common';
import { Component, HostListener, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { SharedService } from '../../../services/shared.service';
import { ApiService } from '../../../services/api-service.service';
// import { HttpClientModule } from '@angular/common/http';
// import { ReportService } from '../../../services/report.service';


@Component({
  selector: 'app-report-summary',
  standalone: true,
  imports: [RouterLink, FormsModule, CommonModule],
  templateUrl: './report-summary.component.html'
})
export class ReportSummaryComponent {
  breeds: string[] = ['Labrador', 'Beagle', 'Bulldog', 'Poodle', 'Boxer'];
  filteredBreeds: string[] = [];
  inputValue: string = '';
  highlightedIndex: number = -1;
  isInputFocused: boolean = false;

  selectedType: string = "";
  selectedSize: string = "";
  reportSummary: any = {
    imageURL: "https://friconix.com/jpg/fi-cnsuxl-question-mark.jpg", 
    timeAgo: "just now", 
    petName: "",  
    status: 0, 
    location: "",
    authorName: "USER",
    authorNickname: "@username",
    type: 0,
    id: 1,
    posted: "1997-03-05T22:00:00.000Z",
    animalType: "",
    pet_id: "123",
    latitude: 0,
    longtitude: 0,
    dominantColors: "-",
    collarColor: "-",
    breed: "",
    size: "",
    gender: "-",
    tel: "",
    email: "",
    social: "-",
    note: "",
    comments: []
  };

  constructor(private sharedService: SharedService, private apiService: ApiService) {
    this.reportSummary.location = this.sharedService.getSharedVariable();
  }

  reportSubmition() {
    this.reportSummary.animalType = this.selectedType;
    this.reportSummary.animalSize = this.selectedSize;
    console.log(this.reportSummary);
    this.apiService.postReport(this.reportSummary).subscribe(
      (response) => {
        console.log('Report submitted successfully!', response);
      },
      (error) => {
        console.error('Error submitting report:', error);
      }
    );
  }

  @HostListener('window:keydown', ['$event'])
  handleKeyboardEvent(event: KeyboardEvent) {
    if (event.key === 'ArrowDown') {
      if (this.highlightedIndex < this.filteredBreeds.length - 1) {
        this.highlightedIndex++;
      }
      event.preventDefault();
    } else if (event.key === 'ArrowUp') {
      if (this.highlightedIndex > 0) {
        this.highlightedIndex--;
      }
      event.preventDefault();
    } else if (event.key === 'Enter' && this.highlightedIndex >= 0) {
      this.selectBreed(this.filteredBreeds[this.highlightedIndex]);
      event.preventDefault(); 
    } else if (event.key === 'Escape') {
      this.filteredBreeds = [];
      this.highlightedIndex = -1;
      event.preventDefault();
    }
  }

  selectBreed(breed: string): void {
    this.inputValue = breed;
    this.filteredBreeds = [];
    this.highlightedIndex = -1;
  }

  filterBreeds(event: Event): void {
    const input = (event.target as HTMLInputElement).value.toLowerCase();
    this.inputValue = input;
    this.filteredBreeds = this.breeds.filter(breed => 
      breed.toLowerCase().includes(input)
    );
  }

  // Don't show the dropdown when the input is not focused
  onFocus(): void {
    this.isInputFocused = true;
  }

  onBlur(): void {
    setTimeout(() => {
      if (!this.isInputFocused) {
        this.filteredBreeds = [];
        this.highlightedIndex = -1;
        this.isInputFocused = false;
      }
    }, 150);
  }
}
