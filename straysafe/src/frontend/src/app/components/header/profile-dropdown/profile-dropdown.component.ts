import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { clickedOutside } from '../../../directives/clickedOutside.directive';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-profile-dropdown',
  standalone: true,
  imports: [CommonModule, clickedOutside, FontAwesomeModule],
  templateUrl: './profile-dropdown.component.html'
})
export class ProfileDropdownComponent {
  dropdownOpen: boolean = false;
  faUser = faUser;

  toggleDropdown(): void {
    this.dropdownOpen = !this.dropdownOpen;
  }

  onClickedOutside(): void {
    this.dropdownOpen = false;
  }
}
